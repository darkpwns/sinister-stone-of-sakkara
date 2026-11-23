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
    return {"walk": walk, "supplies": supplies, "bank": bank, "bank-balances": bank_balances, "cond": cond}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
