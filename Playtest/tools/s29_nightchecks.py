#!/usr/bin/env python3
"""S29: N wandering checks for a sealed night (2 an hour, SOTN p. 18), before `camp` advances the clock; only entries
marked "enters a sealed temple or tomb" reach the party (others ended at once). Stops at the first that does, printing
which half-hour of the night it falls in. Usage: s29_nightchecks.py N"""
import json, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
n = int(sys.argv[1])
for i in range(n):
    code, out = jacks.run(["wander-check"])
    if "ENCOUNTER" in out:
        entry = (json.load(open("Campaign/exploration-state.json")).get("encounter") or {}).get("entry", "")
        if "enters a sealed" in entry:
            print(f"check {i+1} of {n} (half-hour {i+1} of the night): SEALED-ENTRY:", entry); sys.exit(3)
        jacks.run(["encounter", "end"]); print(f"check {i+1}: ignored:", entry[:80])
print(n, "checks: nothing reached the party")
