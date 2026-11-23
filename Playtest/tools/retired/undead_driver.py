#!/usr/bin/env python3
# Playtest helper (S07): drives round-next for mindless foes with per-foe target lists (JSON {foe_id: [targets...]}); resolves cleaves. Usage: undead_driver.py STOP_IDS GROUPS.json
"""Round driver with position groups. usage: und2.py STOP_IDS GROUPS_JSON
GROUPS_JSON: {"undead_id": ["target", ...] (in priority order: standing first, then helpless)}. Undead with no
reachable target do nothing (Judge moves them). Cleaves on the next target of the same list."""
import json, subprocess, sys
A = ["bash", ".claude/skills/acks2-judge/scripts/acks.sh"]
ST = "Campaign/combat-state.json"
stop = set(sys.argv[1].split(",")); G = json.load(open(sys.argv[2]))
def run(*a):
    o = subprocess.run(A + list(a), capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
    return (o[-1] if o else "").split(" (src:")[0]
def st(): return json.load(open(ST))
def ok(c): return c.get("status") not in ("dead", "slain", "destroyed") and c["hp"] > -1000
def alive(c): return c["hp"] > 0 and c.get("status", "active") == "active"
while True:
    line = run("round-next")
    if "acts" not in line: print(line[:200]); break
    s = st(); k = s["order"][s["count_index"]]; c = s["combatants"][k]
    if c["side"] == "party":
        if k in stop: print(line[:120]); print("STOP", k); break
        continue
    if not alive(c) or k not in G: continue
    tl = [t for t in G[k] if t in s["combatants"] and ok(s["combatants"][t])]
    if not tl: continue
    t = tl[0]; run("state", "distance", k, t, "5"); run("state", "engage", k, t)
    o = run("attack", k, t); print(f"  {k}: " + o[:190])
    if "may cleave" in o and len(tl) > 1:
        run("state", "engage", k, tl[1]); print(f"  {k} CLEAVE: " + run("attack", k, tl[1], "--cleave")[:190])
