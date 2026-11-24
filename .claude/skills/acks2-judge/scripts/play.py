#!/usr/bin/env python3
"""play.py : routine sequences of play in one call (the engine runs in this process: no new process per step).

  play.py walk N [--rest-every 5] [--relight ID,ID] [--kind torch]
      Advance N turns of exploration one turn at a time, as the Judge does by hand: rest a turn when the next turn
      would pass the rest interval (RR p. 271: 1 turn in 6), relight when no light is lit (a torch from the first of
      the --relight carriers who has one; with the engine's `light auto on` the engine does it), and STOP, saying why,
      at anything that needs the Judge: an encounter, a character down or dead, no light left, a refusal, anything the
      engine leaves to the Judge, a timer that runs out (`--past-timers` walks on). A carrier's burnt-out lantern is
      refuelled and lit when he has oil (`light refuel ID --light`). Every turn's line is printed
      (sources stripped). Exit code 0: all N turns walked; 3: stopped early.
  play.py supplies [ID ...]
      Torches, oil, rations, holy water and gold of each party member (default: the exploration party).
  play.py bank --to HOLDER [--keep 150] [--day N] [ID ...]
      Each member's gold above --keep goes to the bank holder (`inv give`, cause "banks coin above N gp (day D)").
  play.py payout [payout options …]
      The payout's Ledger rows (`payout … --ledger`) are read, the payout is applied (`payout … --apply`), and the
      rows are appended to the matching sections of the Ledger note (rows already there are not repeated).
      `--rows-only` writes the rows without applying (the payout was applied by hand).
  play.py bank-balances --bank HOLDER [--day N]
      Each member's balance with a bank holder, from the inventory log (who gave, or who the cause names).

  play.py depart --route A,B,C --return-day N [--resupply] [--ids ID,…]
      The pre-march checklist in one call (C1): wages through the return plus a month (what to pay, who pays), food
      and water days per member as the travel block holds them (rations packed but not provisioned are named),
      waterskins per member, feed and water per animal, metamphora carried, the column's speed and who sets it,
      light (torches, oil), spells not yet regained, and the schedule's items that fall on the road. Every line is
      OK, WARN or FAIL; it ends READY only when no line fails (exit 0), else NOT READY (exit 3).

  play.py march DAYS --route A,B,C [--hours-per-day N] [--watches "A,B;C,D"] [--camp-hours 12] [--dusk 18]
      Days of march in one process (C2): each day travel along the route (the hours given, else the engine's day),
      the evening wait to dusk, water at the day's river or lake (`water`), camp with the watches. It stops, saying
      why, at an encounter (a civilized or herd encounter is passed by after its reaction, unless the reaction is
      hostile), a refusal, the party lost, CON lost, a missed wage or a loyalty roll, a death, starvation or
      dehydration, or a schedule item due. Territory classifications come from the campaign data (hexes block), never
      per call. Exit 0: the days marched or the route's end reached; 3: stopped.

  play.py city-week [--day N] [--item weekly-secret] [--world "Campaign/World State.md"]
      The week's city block (C3): finds the week's secret entry in World State ("- **Day N weekly: the week's
      secrets** (S##; entries written before the roll): 1 …; … 6 …."); when it is missing or not six entries, prints
      its template and refuses (exit 3). With the six entries written it runs the week's due schedule items (the
      lesson secret-entries-first acknowledged by the entries' presence) and writes "**rolled N**" and each item's
      result into that line (the Judge adds the narrative); exit 0.

  play.py month-end [--day N] [--administered DOMAIN] [--adventured DOMAIN] [--investment DOMAIN:GP] [--overseen
                   DOMAIN] [--dry-run]
      The month's end in one call (C4), from campaign.yaml `month_end`: the schedule's month-end item, each domain's
      month (`domain month … --apply`), the bank's storage fee per member (`bank: {holder, fee_pct}`), the incomes
      (`incomes: [{to, gp, label, half_when_away: {who, place}, usurpation: "1d6:1"}]`: full while `who` is at
      `place`, half away with the usurpation roll), training progress (`train show`, when the engine has it), and
      the World State and Rulings lines. --dry-run rolls nothing and writes nothing: it lists what would run.

  play.py cond add ID "TEXT" [--cause WHY]   |   play.py cond remove ID "TEXT" [--cause WHY]   |   play.py cond list ID
      One condition added to or taken off an actor's `state.conditions` (the engine's `actor set` takes the whole
      list: this reads it, changes one entry and writes it back with the cause). `remove` matches the exact text or,
      when no entry equals it, the one entry that contains it.

Nothing here decides a rule: every number comes from the engine's own commands, run through jacks.py exactly as
`acks.sh` runs them (same log, same states, same refusals).
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jacks  # noqa: E402
import jlib  # noqa: E402

SRC = re.compile(r" *\(src:[^)]*(?:\([^)]*\)[^)]*)*\)")
STOP = re.compile(r"ENCOUNTER|unconscious|\bdies\b|\bDIES\b|is dead|NO LIGHT LEFT|NO TORCH", re.I)


def short(line, n=260):
    return SRC.sub("", line.strip().splitlines()[-1] if line.strip() else "")[:n]


class Engine:
    def __init__(self):
        self.ctx = jacks.context()

    def run(self, *argv):
        return jacks.run(list(argv), self.ctx)

    def data(self, *argv):
        code, out = jacks.run(list(argv) + ["--json"], self.ctx)
        i = out.find("{")
        try:
            return code, (json.loads(out[i:]) if i >= 0 else {})
        except ValueError:
            return code, {}


def lit(E):
    code, d = E.data("light", "show")
    ls = (d.get("data") or {}).get("lights") or []
    return any(l.get("lit") and (l.get("rounds_left") or 0) > 0 for l in ls)


def since_rest(E):
    """Rounds of exploration since the last rest (the exploration state's own counter)."""
    with open(E.ctx["xstate"], encoding="utf-8") as f:
        return (json.load(f).get("rest") or {}).get("rounds_since_rest", 0)


def relight(E, carriers, kind):
    """A new light from the first carrier who can: his own burnt-out lantern refuelled and lit when he has oil (D8:
    `light refuel ID --light`), else a new light of --kind."""
    code, d = E.data("light", "show", "--all")
    ls = (d.get("data") or {}).get("lights") or []
    for c in carriers:
        for l in ls:
            if l.get("kind") == "lantern" and l.get("carrier") == c and not l.get("lit") and (l.get("rounds_left") or 0) > 0:
                code, out = E.run("light", "on", l["id"])          # his own lantern, put out with oil still in it
                if code == 0:
                    return short(out, 120)
        for l in ls:
            if l.get("kind") == "lantern" and l.get("carrier") == c and (l.get("rounds_left") or 0) <= 0:
                code, out = E.run("light", "refuel", l["id"], "--light")
                if code == 0:
                    return short(out, 120)
        code, out = E.run("light", "on", "--kind", kind, "--carrier", c)
        if code == 0:
            return short(out, 80)
    return None


TIMER = re.compile(r"timer '([^']+)' \(([^)]+)\) expires")


def walk(a):
    E = Engine()
    carriers = [c for c in (a.relight or "").split(",") if c]
    walked = 0

    def ensure_light():
        if lit(E):
            return True
        if not carriers:
            print("-- stop: no light is lit (give --relight ID,ID or `light auto on`)")
            return False
        got = relight(E, carriers, a.kind)
        if not got:
            print("-- stop: NO LIGHT LEFT (no carrier has a " + a.kind + ")")
            return False
        print("relit: " + got)
        return True

    for i in range(1, a.turns + 1):
        if not ensure_light():
            return 3
        if since_rest(E) + 10 > a.rest_every * 10:
            code, out = E.run("rest")
            print("REST: " + short(out, 200))
            if code or STOP.search(out) or " | JUDGE: " in out:
                print(f"-- stop (during the rest before turn {i}): {'refused' if code else 'needs the Judge'}")
                return 3
            if not ensure_light():
                return 3
        code, out = E.run("turn", "1")
        print(short(out))
        if code:
            print(f"-- stop: turn {i} refused")
            return 3
        walked += 1
        if STOP.search(out) or " | JUDGE: " in out:
            print(f"-- stop after turn {i} of {a.turns}: needs the Judge")
            return 3
        tm = TIMER.search(out)
        if tm and not a.past_timers:
            # D8 (S33): an unsettling event's timer ran out inside the walk and the walk went on
            print(f"-- stop after turn {i} of {a.turns}: timer '{tm.group(1)}' ({tm.group(2)}) expired "
                  "(--past-timers to walk on)")
            return 3
    ensure_light()
    print(f"walked {walked} turn{'s' if walked != 1 else ''}")
    return 0


def party_ids(E):
    with open(E.ctx["xstate"], encoding="utf-8") as f:
        return list((json.load(f).get("party") or {}))


def supplies(a):
    E = Engine()
    keys = (("torch", "torches"), ("oil", "oil"), ("rations", "rations"), ("holy water", "holy water"))
    for i in a.ids or party_ids(E):
        code, d = E.data("inv", "show", i)
        d = d.get("data") or {}
        hold = next(iter((d.get("holdings") or {}).values()), {}) or {}
        cnt = {}
        for slot, items in hold.items():
            for name, n in (items or {}).items():
                for k, lab in keys:
                    if k in name.lower():
                        cnt[lab] = cnt.get(lab, 0) + n
                        break
        coins = next(iter((d.get("coins") or {}).values()), {}) or {}
        print(f"{i}: " + ", ".join(f"{v} {k}" for k, v in cnt.items()) + f"{'; ' if cnt else ''}{int(coins.get('gp', 0))} gp")
    return 0


def bank(a):
    E = Engine()
    day = a.day
    if day is None:
        with open(E.ctx["xstate"], encoding="utf-8") as f:
            day = json.load(f)["clock"]["day"]
    rc = 0
    for i in a.ids or party_ids(E):
        code, d = E.data("inv", "show", i)
        coins = next(iter(((d.get("data") or {}).get("coins") or {}).values()), {}) or {}
        gp = int(coins.get("gp", 0))
        if gp > a.keep:
            code, out = E.run("inv", "give", i, a.to, f"{gp - a.keep}gp", "--cause",
                              f"{i} banks coin above {a.keep}gp (day {day})")
            print(short(out, 120))
            rc = rc or code
    return rc


def ledger_rows(text):
    """{section: [rows]} of a `payout --ledger` printout."""
    secs, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"## (.+)", line)
        if m:
            cur = m.group(1).strip()
            secs.setdefault(cur, [])
        elif cur and line.startswith("| ") and not re.match(r"\|\s*-+", line):
            secs[cur].append(SRC.sub("", line).rstrip())
    return secs


def append_rows(ledger_path, secs):
    s = open(ledger_path, encoding="utf-8").read()
    done = {}
    for name, rows in secs.items():
        i = s.find("## " + name)
        if i < 0 or not rows:
            if rows:
                print(f"Ledger: no section '## {name}' ({len(rows)} rows not written)")
            continue
        j = s.find("\n## ", i + 1)
        j = len(s) if j < 0 else j
        block = s[i:j]
        have = set(block.splitlines())
        new = [r for r in rows if r not in have]
        if not new:
            done[name] = 0
            continue
        block = block.rstrip("\n") + "\n" + "\n".join(new) + "\n"
        s = s[:i] + block + ("\n" + s[j + 1:] if j < len(s) else "")
        done[name] = len(new)
    with open(ledger_path, "w", encoding="utf-8") as f:
        f.write(s)
    return done


def payout(a, rest):
    E = Engine()
    code, out = E.run("payout", *rest, "--ledger")          # the rows, read before the payout closes the adventure
    if code:
        print(short(out, 600))
        return code
    rows = ledger_rows(out)
    if not a.rows_only:
        code, out = E.run("payout", *rest, "--apply")
        print(short(out, 2000))
        if code:
            return code
    led = jlib.path(E.ctx["cfg"]["paths"]["state"].get("ledger", "Campaign/Ledger.md"))
    done = append_rows(led, rows)
    print("Ledger: " + (", ".join(f"{n} rows -> {k}" for k, n in done.items()) or "nothing to write"))
    return 0


def bank_balances(a):
    E = Engine()
    with open(E.ctx["istate"], encoding="utf-8") as f:
        x = json.load(f)
    upto = a.day if a.day is not None else 10 ** 9
    V = {"pp": 5.0, "gp": 1.0, "ep": 0.5, "sp": 0.1, "cp": 0.01}

    def val(c):
        return sum(V[k] * c.get(k, 0) for k in V)
    ids = sorted(x["holders"], key=len, reverse=True)
    bal, unknown, tot = {}, [], 0.0
    for e in x["log"]:
        if (e.get("day") or 0) > upto:
            continue
        cs = e.get("coins", [])
        g = [c for c in cs if c.get("who") == a.bank]
        if not g:
            continue
        d = sum(val(c) for c in g)
        tot += d
        others = [c["who"] for c in cs if c.get("who") != a.bank]
        who = others[0] if others else None
        if not who:
            m = [i for i in ids if re.search(r"\b" + re.escape(i) + r"\b", e.get("cause", ""), re.I)]
            who = m[0] if m else None
        if who is None:
            unknown.append((e.get("n"), round(d, 2), e.get("cause", "")[:80]))
            continue
        bal[who] = bal.get(who, 0) + d
    for k, v in sorted(bal.items()):
        if abs(v) > 0.005:
            print(f"{k}: {v:,.2f}")
    print(f"sum {sum(bal.values()):,.2f}; bank holds {tot:,.2f}; unattributed {unknown}")
    return 0


def cond(a):
    E = Engine()
    from jlib import actor_dirs, load_actor
    path = next((os.path.join(d, a.id + ".json") for d in actor_dirs(E.ctx["cfg"])
                 if os.path.exists(os.path.join(d, a.id + ".json"))), None)
    if not path:
        print(f"no actor {a.id}")
        return 1
    cur = list((load_actor(path).get("state") or {}).get("conditions") or [])
    if a.action == "list":
        print(json.dumps(cur, ensure_ascii=False))
        return 0
    if a.action == "add":
        if a.text in cur:
            print(f"{a.id} already has: {a.text}")
            return 0
        new = cur + [a.text]
    else:
        hit = [c for c in cur if c == a.text] or [c for c in cur if a.text.lower() in str(c).lower()]
        if len(hit) != 1:
            print(f"{a.id}: {len(hit)} conditions match {a.text!r}: {json.dumps(cur, ensure_ascii=False)[:400]}")
            return 1
        new = [c for c in cur if c != hit[0]]
    code, out = E.run("actor", "set", a.id, "state.conditions", json.dumps(new, ensure_ascii=False), "--cause",
                      a.cause or ("condition" if a.action == "add" else "condition ends"))
    print(short(out, 200))
    return code


def _held_counts(st, I, hid, words):
    out = {w: 0 for w in words}
    for key, q in (I.held(st, hid) or {}).items():
        low = key.lower()
        for w in words:
            if w in low:
                out[w] += q
    return out


def depart(a):
    """C1: the pre-march checklist. Nothing is changed: it reads the states and asks the engine (travel-show,
    schedule due) through jacks.py."""
    from acks import hire as H
    from acks import inventory as I
    E = Engine()
    ctx = E.ctx
    with open(ctx["xstate"], encoding="utf-8") as f:
        xs = json.load(f)
    day = xs["clock"]["day"]
    ids = [x for x in (a.ids or "").split(",") if x] or list(xs.get("party") or {})
    route = [x for x in (a.route or "").split(",") if x]
    ret = int(a.return_day)
    trip = max(0, ret - day)
    lines, fails = [], 0

    def out(kind, text):
        nonlocal fails
        fails += kind == "FAIL"
        lines.append(f"{kind:4} {text}")

    # wages through the return plus a month
    if os.path.exists(ctx["rstate"]):
        rs = H.load(ctx["rstate"])
        md = int(rs.get("month_days") or 30)
        horizon = ret + md
        for m in H.active_members(rs):
            if m.get("wage_per") != "month" or not m.get("wage_gp"):
                continue
            k = m["periods_paid"]
            dues = []
            while H.due_day(rs, m, k) <= horizon:
                dues.append(H.due_day(rs, m, k))
                k += 1
            amt = m["wage_gp"] * m.get("count", 1)
            if dues:
                out("FAIL", f"wages: {m['id']} {m['name']} ({m['employer']} pays) due day {', '.join(map(str, dues))}: "
                            f"`wages pay {m['id']} --payer {m['employer']} --months {len(dues)}` ({len(dues) * amt:g} gp)")
            else:
                out("OK", f"wages: {m['id']} {m['name']} paid through day {H.due_day(rs, m, m['periods_paid']) - 1}")
    # the travel block: food, water, speed
    code, tv = E.data("travel-show")
    tv = tv.get("data") or {}
    mem = tv.get("members") or {}
    st = I.load(ctx["istate"]) if os.path.exists(ctx["istate"]) else None
    meta = 0
    for i in ids:
        m = mem.get(i) or {}
        if m.get("dead"):
            continue
        food = sum(float(x.get("days") or 0) for x in m.get("food") or [])
        water = float(m.get("water") or 0)
        cnt = _held_counts(st, I, i, ("ration", "waterskin", "metamphora", "torch", "oil")) if st and i in st["holders"] \
            else {}
        meta += cnt.get("metamphora", 0)
        need = trip
        if food + 1e-9 < need:
            hint = f"; {cnt.get('ration', 0)} ration item(s) packed: `inv provision`" if cnt.get("ration") else ""
            out("WARN" if a.resupply else "FAIL", f"food: {i} {food:g} day(s) provisioned for {trip} day(s) out{hint}")
        else:
            out("OK", f"food: {i} {food:g} day(s)")
        if not cnt.get("waterskin") and water < 1:
            out("FAIL", f"water: {i} {water:g} day(s), no waterskins")
        else:
            out("OK", f"water: {i} {water:g} day(s), {cnt.get('waterskin', 0)} waterskin(s)")
        if cnt:
            out("OK", f"light: {i} {cnt.get('torch', 0)} torch(es), {cnt.get('oil', 0)} oil")
    from acks import travel as TV
    for aid, an in (tv.get("animals") or {}).items():
        feed = float(an.get("food") or 0) + float(an.get("feed_inv") or 0)
        row, _r = TV.animal_food_row(an.get("kind") or "")
        days = feed / row[0] if row and row[0] else 0
        grazer = TV.is_grazer(an.get("kind") or "")
        kind = "OK" if grazer or days >= max(1, trip) else ("WARN" if days >= 1 else "FAIL")
        out(kind, f"feed: {aid} ({an.get('kind')}) {feed:g} st = {days:.1f} day(s)" + (" (grazes)" if grazer else "")
            + f"; water {float(an.get('water') or 0):g} st")
    out("OK", f"metamphora carried: {meta}")
    sp = tv.get("speed") or {}
    if sp.get("error"):
        out("FAIL", f"speed: {sp['error']}")
    elif sp:
        days = (6 * len(route) / sp["miles_per_day"]) if route and sp.get("miles_per_day") else None
        out("OK", f"speed: {sp['miles_per_day']:g} mi/day, set by {sp['slowest']}"
            + (f"; the route ({len(route)} hexes) about {days:.1f} day(s)" if days else ""))
        if days and days > trip:
            out("FAIL", f"route: about {days:.1f} day(s) out but the return is day {ret} ({trip} days)")
    # spells not regained
    for i in ids:
        p = jlib.actor_path(i) if hasattr(jlib, "actor_path") else None
        if not p:
            for d in jlib.actor_dirs(jlib.config()):
                q = os.path.join(d, f"{i}.json")
                if os.path.exists(q):
                    p = q
                    break
        if p and os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                used = ((json.load(f).get("state") or {}).get("spells_used") or [])
            if used:
                out("WARN", f"spells: {i} has not regained {', '.join(map(str, used))} (a night's rest first)")
    # the schedule's items on the road
    if trip:
        code, sd = E.data("schedule", "due", "--ahead", str(trip))
        d = sd.get("data") or {}
        for x in d.get("due") or []:
            out("FAIL", f"schedule: {x['id']} due day {x['due_day']} (before leaving: `schedule run --due`)")
        for x in d.get("ahead") or []:
            out("WARN", f"schedule: {x['id']} falls on day {x['day']} on the road")
    for ln in lines:
        print(ln)
    print("READY" if not fails else f"NOT READY: {fails} line(s) fail")
    return 0 if not fails else 3


MARCH_STOP = re.compile(r"loses \d+ CON|\bCON\b[^;|]{0,20}lost|DEHYDRATED|STARVING|missed|not paid|calamity|loyalty roll|"
                        r"\bdies\b|is dead|DUE day|NOT ALLOWED", re.I)
BENIGN = re.compile(r"herd|commoner|merchant|pilgrim|peasant|caravan|patrol", re.I)


def _facts(out):
    """The engine's own lines, without lesson reminders and notes (their words must not stop a march)."""
    return " | ".join(p for p in SRC.sub("", out).split(" | ") if not p.strip().startswith(("REMINDER", "NOTE")))


def _xs(E):
    with open(E.ctx["xstate"], encoding="utf-8") as f:
        return json.load(f)


def _enc_open(x):
    e = x.get("encounter") or {}
    return e if e and e.get("status") not in ("ended", "no encounter", "evaded") else None


def _benign_pass(E, e):
    """A civilized or herd encounter passed by after its reaction: (passed, text)."""
    kind = ((e.get("wilderness") or {}).get("kind") or "")
    name = str(e.get("monster_name") or e.get("entry") or "")
    if not (kind == "civilized" or BENIGN.search(name)):
        return False, f"encounter {e.get('id')}: {name} ({kind or 'monster'})"
    code, out = E.run("reaction")
    if code or re.search(r"hostile|attacks", out, re.I):
        return False, f"encounter {e.get('id')}: {name}: {short(out, 200)}"
    E.run("encounter", "end")
    return True, f"{name}: {short(out, 120)}; passed by"


def march(a):
    E = Engine()
    route = [x for x in a.route.split(",") if x]
    watches = a.watches
    for n in range(a.days):
        x = _xs(E)
        here = x["travel"]["hex"]
        if here in route:
            route = route[route.index(here) + 1:]
        if not route:
            print(f"arrived at {here}")
            return 0
        day = x["clock"]["day"]
        argv = ["travel", "--route", ",".join(route)] + (["--hours", str(a.hours_per_day)] if a.hours_per_day else [])
        code, out = E.run(*argv)
        print(f"day {day}: {short(out, 300)}")
        if code and "travel is used up" in out:
            out = ""                                     # today's travel was done before the march: camp first
        elif code:
            print("STOP: travel refused")
            return 3
        x = _xs(E)
        e = _enc_open(x)
        while e:
            ok, why = _benign_pass(E, e)
            print(f"  {why}")
            if not ok:
                print("STOP: encounter")
                return 3
            x = _xs(E)
            here = x["travel"]["hex"]
            rest = [h for h in route if h != here]
            code, out = E.run("travel", "--route", ",".join(rest[rest.index(here) + 1:] if here in rest else rest),
                              *(["--hours", str(a.hours_per_day)] if a.hours_per_day else []))
            print(f"  on: {short(out, 200)}")
            x = _xs(E)
            e = _enc_open(x) if not code else None
        pend = x["travel"].get("pending_enc")
        if pend:
            # an encounter met partway into the hex where the day's travel ended (S47 day 675: it lapsed)
            code, out2 = E.run("encounter", "start", "--wild", "--kind", "pending")
            print(f"  pending: {short(out2, 200)}")
            x = _xs(E)
            e = _enc_open(x)
            ok, why = _benign_pass(E, e) if e else (False, "the pending encounter could not begin")
            print(f"  {why}")
            if not ok:
                print("STOP: encounter")
                return 3
            x = _xs(E)
        if (x["travel"].get("lost") or {}):
            print(f"STOP: the party is lost (true {x['travel']['hex']}, believed {x['travel']['believed']})")
            return 3
        if MARCH_STOP.search(_facts(out)):
            print("STOP: " + MARCH_STOP.search(_facts(out)).group(0))
            return 3
        hr = x["clock"]["round_of_day"] / 60.0
        if int(a.dusk - hr) >= 1:
            E.run("wait", "--hours", str(int(a.dusk - hr)))
        code, wout = E.run("water")
        if code == 0 and "nothing" not in wout.lower():
            print(f"  water: {short(wout, 160)}")
        argv = ["camp", "--hours", str(a.camp_hours)] + (["--watches", watches] if watches else [])
        code, out = E.run(*argv)
        print(f"  night: {short(out, 300)}")
        if code:
            print("STOP: camp refused")
            return 3
        x = _xs(E)
        if _enc_open(x):
            print("STOP: night encounter")
            return 3
        if MARCH_STOP.search(_facts(out)):
            m = MARCH_STOP.search(_facts(out))
            print("STOP: " + _facts(out)[max(0, m.start() - 80):m.end() + 80])
            return 3
    return 0


WEEK_RE = r"^- \*\*Day {day} weekly: the week's secrets\*\* \(([^)]*)\): (.*)$"


def city_week(a):
    E = Engine()
    ctx = E.ctx
    world = jlib.path(a.world)
    with open(world, encoding="utf-8") as f:
        text = f.read()
    with open(ctx["xstate"], encoding="utf-8") as f:
        xs = json.load(f)
    day = a.day
    if day is None:
        code, d = E.data("schedule", "due", "--ahead", "7")
        d = d.get("data") or {}
        due = [x for x in (d.get("due") or []) if x["id"] == a.item] or \
            [x for x in (d.get("ahead") or []) if x["id"] == a.item]
        if not due:
            print(f"nothing of {a.item} due now or in the coming week")
            return 3
        day = due[0].get("due_day") or due[0].get("day")
    sess = ctx.get("session") or "?"
    pat = re.compile(WEEK_RE.format(day=day), re.M)
    m = pat.search(text)
    entries = re.findall(r"(?:^|; )(\d) ", m.group(2)) if m else []
    if not m or [e for e in entries] != ["1", "2", "3", "4", "5", "6"]:
        print(f"NOT RUN: the six entries of day {day} are not in {a.world} yet. Write this line (in ## Scheduled "
              f"events, above the last week's), then run again:")
        print(f"- **Day {day} weekly: the week's secrets** (S{sess}; entries written before the roll): 1 …; 2 …; 3 …; "
              f"4 …; 5 …; 6 ….")
        return 3
    if "rolled" in m.group(1):
        print(f"day {day}: the week's secret is rolled already ({m.group(1)})")
        return 3
    os.environ["ACKS_ACK"] = ",".join(x for x in [os.environ.get("ACKS_ACK", ""), "secret-entries-first"] if x)
    code, out = E.run("schedule", "run", "--due", "--day", str(day))
    print(short(out, 2000))
    if code:
        print("STOP: the schedule run was refused")
        return 3
    res = []
    rolled = None
    for part in SRC.sub("", out).split(" | ")[0].split("; "):
        part = part.replace("[H] ", "").strip()
        mm = re.match(r"(.+?): (\d+d\d+.*?) = (-?\d+)(?:: (.*))?$", part)
        if mm:
            if a.item in part or "the secret" in mm.group(1):
                rolled = mm.group(3)
            res.append(f"{mm.group(1)} {mm.group(3)}" + (f" ({mm.group(4)})" if mm.group(4) else ""))
    head = m.group(1) + (f"; **rolled {rolled}**" if rolled else "") + ("; " + "; ".join(r for r in res if "the secret" not in r) if res else "")
    new = f"- **Day {day} weekly: the week's secrets** ({head}): {m.group(2)}"
    text = text[:m.start()] + new + text[m.end():]
    with open(world, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"written into {a.world}: day {day} weekly, rolled {rolled}")
    return 0


def _balances(ctx, bank, upto):
    with open(ctx["istate"], encoding="utf-8") as f:
        x = json.load(f)
    V = {"pp": 5.0, "gp": 1.0, "ep": 0.5, "sp": 0.1, "cp": 0.01}
    ids = sorted(x["holders"], key=len, reverse=True)
    bal = {}
    for e in x["log"]:
        if (e.get("day") or 0) > upto:
            continue
        g = [c for c in e.get("coins", []) if c.get("who") == bank]
        if not g:
            continue
        d = sum(V[k] * c.get(k, 0) for c in g for k in V)
        others = [c["who"] for c in e.get("coins", []) if c.get("who") != bank]
        who = others[0] if others else next((i for i in ids if re.search(r"\b" + re.escape(i) + r"\b",
                                                                              e.get("cause", ""), re.I)), None)
        if who:
            bal[who] = bal.get(who, 0) + d
    return {k: v for k, v in bal.items() if v > 0.005}


def _where(xs, who):
    """The settlement a character is in: the party's location, or where he stays behind."""
    if who in (xs.get("staying") or {}):
        return str((xs["staying"][who] or {}).get("place") or "")
    if who in (xs.get("party") or {}):
        loc = xs.get("location") or {}
        return str(loc.get("site") or "") if loc.get("kind") == "settlement" else ""
    return ""


def month_end(a):
    E = Engine()
    ctx = E.ctx
    cfg = ctx["cfg"].get("month_end") or {}
    with open(ctx["xstate"], encoding="utf-8") as f:
        xs = json.load(f)
    md = int((ctx["cfg"].get("tools") or {}).get("month_days") or 30)
    day = a.day or ((xs["clock"]["day"] + md - 1) // md) * md
    month = day // md
    sess = ctx.get("session") or "?"
    lines, plan = [], []
    item = cfg.get("schedule_item", "month-end")
    plan.append(f"schedule run {item} --due-day {day}")
    for did in (cfg.get("domains") or []):
        plan.append(f"domain month {did} --apply")
    bank = cfg.get("bank") or {}
    if bank.get("holder"):
        plan.append(f"bank fee {bank.get('fee_pct', 0.25)}% from {bank['holder']}")
    for inc in cfg.get("incomes") or []:
        plan.append(f"income {inc['label']} -> {inc['to']}")
    if a.dry_run:
        print("month's end, day %d (month %d): %s" % (day, month, "; ".join(plan)))
        return 0
    code, out = E.run("schedule", "run", item, "--due-day", str(day), "--day", str(day))
    print(short(out, 600))
    if code:
        print("STOP: the month-end item was refused")
        return 3
    lines.append("schedule: " + "; ".join(p.replace("[H] ", "") for p in SRC.sub("", out).split(" | ")[0].split("; ")[1:]))
    invest = dict(x.split(":", 1) for x in (a.investment or []))
    for did in (cfg.get("domains") or []):
        argv = ["domain", "month", did, "--apply", "--day", str(day)]
        if did in (a.administered or []):
            argv.append("--administered")
        if did in (a.adventured or []):
            argv.append("--adventured")
        if did in invest:
            argv += ["--investment", invest[did]] + (["--overseen"] if did in (a.overseen or []) else [])
        code, out = E.run(*argv)
        print(short(out, 600))
        if code:
            print(f"STOP: domain {did}: refused")
            return 3
        fam = re.search(r"= (\d+)$", SRC.sub("", out).split(" | ")[0].split("; families ")[-1].split(";")[0])
        lines.append(f"domain {did}: " + "; ".join(p for p in SRC.sub("", out).split(" | ")[0].replace("[H] ", "").split("; ")
                                                   if p.startswith(("families", "morale roll", did)) or "revenue" in p))
    if bank.get("holder"):
        bal = _balances(ctx, bank["holder"], day)
        pct = float(bank.get("fee_pct", 0.25))
        for who, v in sorted(bal.items()):
            fee = round(v * pct / 100, 2)
            if fee < 0.01:
                continue
            code, out = E.run("inv", "pay", bank["holder"], f"{fee:g}gp", "--to", "the bank's storage fee",
                              "--cause", f"storage fee {pct:g}% of {who}'s balance {v:,.0f}gp (month {month})")
            print(short(out, 200))
        lines.append(f"bank fee {pct:g}% on {len(bal)} balance(s)")
    for inc in cfg.get("incomes") or []:
        gp = float(inc["gp"])
        note = ""
        away = inc.get("half_when_away")
        if away and away.get("place", "").lower() not in _where(xs, away["who"]).lower():
            gp = gp / 2
            note = f" (half: {away['who']} away)"
            if inc.get("usurpation"):
                die, _, hit = inc["usurpation"].partition(":")
                code, out = E.run("roll", "--hidden", f"{inc['label']}: usurpation while {away['who']} is away:{die}")
                r = int(re.search(r"= (\d+)", out).group(1))
                if r <= int(hit or 1):
                    print(f"STOP: {inc['label']}: a lieutenant makes himself boss ({die} {r}): the take stops (Judge)")
                    lines.append(f"{inc['label']}: USURPED ({die} {r}): stopped")
                    continue
                note += f"; usurpation {die} {r}: holds"
        code, out = E.run("inv", "receive", inc["to"], f"{gp:.0f}gp", "--from", inc["label"], "--cause",
                          f"{inc['label']}, month {month}{note}")
        print(short(out, 200))
        lines.append(f"{inc['label']} {gp:,.0f}gp to {inc['to']}{note}")
    code, out = E.run("train", "show") if "train" in (cfg.get("extras") or ["train"]) else (1, "")
    if code == 0:
        lines.append("training: " + short(out, 300))
    text = "; ".join(lines)
    world = jlib.path("Campaign/World State.md")
    with open(world, encoding="utf-8") as f:
        w = f.read()
    entry = f"- **Day {day} (S{sess}): month {month}'s end.** {text}\n"
    w = w.replace("## Scheduled events\n", "## Scheduled events\n" + entry, 1)
    with open(world, "w", encoding="utf-8") as f:
        f.write(w)
    rul = jlib.path("Campaign/Rulings.md")
    import datetime
    with open(rul, "a", encoding="utf-8") as f:
        f.write(f"| {datetime.date.today().isoformat()} | S{sess} | Month {month}'s end (day {day}) | "
                f"{text.replace('|', '/')} | play.py month-end (engine) |\n")
    print(f"written: World State and Rulings (month {month}'s end)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("walk")
    p.add_argument("turns", type=int)
    p.add_argument("--rest-every", type=int, default=5, help="turns of exploration before a turn of rest (RR p. 271)")
    p.add_argument("--relight", help="carriers to take a new light from, in order (ID,ID)")
    p.add_argument("--kind", default="torch")
    p.add_argument("--past-timers", action="store_true", help="walk on when a timer runs out (default: stop)")
    p = sub.add_parser("supplies")
    p.add_argument("ids", nargs="*")
    p = sub.add_parser("bank")
    p.add_argument("ids", nargs="*")
    p.add_argument("--to", required=True)
    p.add_argument("--keep", type=int, default=150)
    p.add_argument("--day", type=int)
    p = sub.add_parser("payout")
    p.add_argument("--rows-only", action="store_true")
    p = sub.add_parser("bank-balances")
    p.add_argument("--bank", required=True)
    p.add_argument("--day", type=int)
    p = sub.add_parser("depart")
    p.add_argument("--route", default="")
    p.add_argument("--return-day", required=True, type=int)
    p.add_argument("--resupply", action="store_true", help="food short of the whole trip is a warning (resupply on "
                                                           "the way)")
    p.add_argument("--ids", help="the members who go (default: the exploration party)")
    p = sub.add_parser("march")
    p.add_argument("days", type=int)
    p.add_argument("--route", required=True)
    p.add_argument("--hours-per-day", type=float)
    p.add_argument("--watches")
    p.add_argument("--camp-hours", type=float, default=12)
    p.add_argument("--dusk", type=float, default=18)
    p = sub.add_parser("city-week")
    p.add_argument("--day", type=int)
    p.add_argument("--item", default="weekly-secret")
    p.add_argument("--world", default="Campaign/World State.md")
    p = sub.add_parser("month-end")
    p.add_argument("--day", type=int)
    p.add_argument("--administered", action="append")
    p.add_argument("--adventured", action="append")
    p.add_argument("--investment", action="append", help="DOMAIN:GP")
    p.add_argument("--overseen", action="append")
    p.add_argument("--dry-run", action="store_true")
    p = sub.add_parser("cond")
    p.add_argument("action", choices=["add", "remove", "list"])
    p.add_argument("id")
    p.add_argument("text", nargs="?")
    p.add_argument("--cause")
    a, rest = ap.parse_known_args(argv)
    if a.cmd == "payout":
        return payout(a, rest)
    if rest:
        ap.error("unrecognized arguments: " + " ".join(rest))
    return {"walk": walk, "supplies": supplies, "bank": bank, "bank-balances": bank_balances, "cond": cond,
            "depart": depart, "march": march, "city-week": city_week, "month-end": month_end}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
