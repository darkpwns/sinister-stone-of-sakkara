#!/usr/bin/env python3
"""play.py : routine sequences of play in one call (the engine runs in this process: no new process per step).

  play.py walk N [--rest-every 5] [--relight ID,ID] [--kind torch]
      Advance N turns of exploration one turn at a time, as the Judge does by hand: rest a turn when the next turn
      would pass the rest interval (RR p. 271: 1 turn in 6), relight when no light is lit (a torch from the first of
      the --relight carriers who has one; with the engine's `light auto on` the engine does it), and STOP, saying why,
      at anything that needs the Judge: an encounter, a character down or dead, no light left, a refusal, anything the
      engine leaves to the Judge. A timer that runs out is reported and the walk goes on. Every turn's line is printed
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
    for c in carriers:
        code, out = E.run("light", "on", "--kind", kind, "--carrier", c)
        if code == 0:
            return short(out, 80)
    return None


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
    for aid, an in (tv.get("animals") or {}).items():
        feed = float(an.get("food") or 0)
        out("OK" if feed or an.get("grazer") else "WARN",
            f"feed: {aid} ({an.get('kind')}) {feed:g} day(s) of feed, {float(an.get('water') or 0):g} of water")
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("walk")
    p.add_argument("turns", type=int)
    p.add_argument("--rest-every", type=int, default=5, help="turns of exploration before a turn of rest (RR p. 271)")
    p.add_argument("--relight", help="carriers to take a new light from, in order (ID,ID)")
    p.add_argument("--kind", default="torch")
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
            "depart": depart}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
