#!/usr/bin/env python3
"""One combat round with the engine: party melee engages and attacks living foes, missile users shoot unengaged foes,
foes attack whoever they are engaged with (else the nearest front-liner). Usage: fight.py ROUNDS [--front a,b,..]
[--missile a,b] [--hold a,b] [--foe-weapon NAME] [--declare id:spell ...]"""
import json, subprocess, sys, argparse, random

ap = argparse.ArgumentParser()
ap.add_argument("rounds", type=int)
ap.add_argument("--front", default="aulus,tarq,sabina,quintus-the-rager,zaira-the-beautiful,thorwell")
ap.add_argument("--missile", default="vettius,gallus,thorcigar")
ap.add_argument("--hold", default="")
ap.add_argument("--foe-weapon", default="")
ap.add_argument("--declare", action="append", default=[])
ap.add_argument("--latch", default="", help="foe damage die once a hit latches on (stirge: 1d3)")
ap.add_argument("--first-strike", type=int, default=0)
a = ap.parse_args()
ST = "Campaign/combat-state.json"
LATCH = "Campaign/.latched.json"
import os
latched = json.load(open(LATCH)) if os.path.exists(LATCH) else {}
struck = set(latched)
A = ["bash", ".claude/skills/acks2-judge/scripts/acks.sh"]


def run(*args):
    o = subprocess.run(A + list(args), capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
    line = (o[-1] if o else "").split(" (src:")[0]
    return line


def st():
    return json.load(open(ST))


front = [x for x in a.front.split(",") if x]
missile = [x for x in a.missile.split(",") if x]
hold = set(x for x in a.hold.split(",") if x)


def alive(c):
    return c["hp"] > 0 and c.get("status", "active") == "active"


def foes(s):
    return [k for k, c in s["combatants"].items() if c["side"] != "party" and alive(c)]


def engaged_with(s, k):
    return [x for x in (s["combatants"][k].get("engaged") or [])]


for rnd in range(a.rounds):
    s = st()
    if not foes(s):
        print("no foes left"); break
    if a.foe_weapon:
        for f in foes(s):
            if not s["combatants"][f].get("weapon"):
                run("state", "set", f, f"weapon={a.foe_weapon}")
    decl = []
    for d in a.declare:
        decl += ["--declare", d]
    print(run("round-start", *decl)[:160])
    for _ in range(40):
        line = run("round-next")
        if "acts" not in line:
            break
        s = st()
        who = next((k for k, c in s["combatants"].items() if c.get("name") and f"{c['name']} acts" in line), None)
        if who is None:
            continue
        c = s["combatants"][who]
        if not alive(c) or "cannot act" in line:
            continue
        fl = foes(s)
        if not fl:
            break
        if c["side"] == "party":
            if who in hold:
                continue
            eng = [x for x in engaged_with(s, who) if x in fl]
            if who in front:
                t = eng[0] if eng else min(fl, key=lambda f: len(engaged_with(s, f)))
                if not eng:
                    run("state", "engage", who, t)
                out = run("attack", who, t, *(["--weapon", c["weapon"]] if c.get("weapon") else []))
                n = 0
                while "may cleave" in out and n < 6:
                    print(out[:230]); n += 1
                    s2 = st(); fl2 = [f for f in foes(s2) if f != t]
                    if not fl2:
                        break
                    t = min(fl2, key=lambda f: len(engaged_with(s2, f)))
                    run("state", "engage", who, t)
                    out = run("attack", who, t, "--cleave", *(["--weapon", c["weapon"]] if c.get("weapon") else []))
            elif who in missile and not eng:
                free = [f for f in fl if not [x for x in engaged_with(s, f) if s["combatants"][x]["side"] == "party"]]
                if not free:
                    continue
                out = run("attack", who, free[0], "--range", "short")
            else:
                continue
        else:
            eng = [x for x in engaged_with(s, who) if alive(s["combatants"][x])]
            if not eng:
                tgt = [x for x in front if x in s["combatants"] and alive(s["combatants"][x])]
                if not tgt:
                    continue
                t = min(tgt, key=lambda x: len([y for y in engaged_with(s, x) if alive(s['combatants'][y])]))
                run("state", "engage", who, t)
            else:
                t = eng[0]
            if a.latch and latched.get(who) and alive(s["combatants"].get(latched[who], {"hp": 0, "status": "x"})):
                out = run("damage", latched[who], "--dice", a.latch, "--type", "piercing") + " (latched: blood drain)"
                print(out[:230]); continue
            args = ["attack", who, t]
            if c.get("weapon"):
                args += ["--weapon", c["weapon"]]
            if a.first_strike and who not in struck:
                args += ["--mod", f"first strike:+{a.first_strike}"]
                struck.add(who)
            out = run(*args)
            if a.latch and " HIT" in out:
                latched[who] = t
        print(out[:230])
    print(run("round-end")[:260])
    json.dump(latched, open(LATCH, "w"))
s = st()
print({k: c["hp"] for k, c in s["combatants"].items() if c["side"] == "party" and c["hp"] < (c.get("hp_max") or c["hp"])})
print("foes left:", foes(s))
