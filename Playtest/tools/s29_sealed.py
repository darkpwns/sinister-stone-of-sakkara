#!/usr/bin/env python3
"""S29 sealed rest: `rest` one turn at a time until the clock reaches HH:MM (same day, or next day with --next-day).
Hub rule (SOTN p. 18): a party sealed in a temple or tomb meets only entries marked "enters a sealed temple or tomb";
any other wandering encounter found by a rest turn's check is ended at once (it does not reach the party) and the
rest goes on. Stops (exit 3) at a sealed-entry encounter, a refusal, or anything else the Judge must see.
Usage: s29_sealed.py HH:MM [--next-day]"""
import json, re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
XS = "Campaign/exploration-state.json"
target = sys.argv[1]
next_day = "--next-day" in sys.argv


def clock():
    x = json.load(open(XS))
    c = x["clock"]
    return int(c["day"]), int(c["round_of_day"])


d0, _ = clock()
hh, mm = map(int, target.split(":"))
goal = (d0 + (1 if next_day else 0), hh * 60 + mm)
ignored = 0
while True:
    if clock() >= goal:
        break
    code, out = jacks.run(["rest"])
    line = out.strip().splitlines()[-1] if out.strip() else ""
    if code != 0:
        print("STOP (refusal/error):", line[:400]); sys.exit(3)
    if "ENCOUNTER" in line:
        m = re.search(r"encounter (enc\d+): (.*?) x(\d+)", line)
        x = json.load(open(XS))
        entry = (x.get("encounter") or {}).get("entry", "")
        if "enters a sealed" in entry:
            print("SEALED-ENTRY ENCOUNTER:", re.sub(r" \(src: .*", "", line)[:500]); sys.exit(3)
        jacks.run(["encounter", "end"])
        ignored += 1
        print("ignored (does not enter a sealed temple):", entry[:120], "at", clock())
print("rested to", clock(), "; ignored wanderers:", ignored)
