"""Choke-point round driver (S09): foes queue to SLOTS doorway places; entering or starting in the burning patch costs
1d8 fire (while patch rounds remain); foes in a slot attack the party member named for that slot; party melee
attackers hit foes in slots, the archer shoots the next foe in the queue. usage: choke.py ROUND_PATCH_LEFT"""
import json, subprocess, sys
A = ["bash", ".claude/skills/acks2-judge/scripts/acks.sh"]; ST = "Campaign/combat-state.json"
def run(*a):
    o = subprocess.run(A + list(a), capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
    return (o[-1] if o else "").split(" (src:")[0].split(" | NOTE")[0]
def st(): return json.load(open(ST))
patch = int(sys.argv[1]) > 0
import os
SLOTW = json.load(open("Campaign/.slotw.json")) if os.path.exists("Campaign/.slotw.json") else {"s1": "brennus", "s2": "quirinus"}
SKIP = set(os.environ.get("SKIP","").split(","))
HOOK = dict(x.split("=",1) for x in os.environ.get("HOOK","").split(";") if "=" in x)
MELEE = {"brennus": "s1", "quirinus": "s2", "lucilla": "s1", "hrodvar": "s2", "vettius": "s1", "varro": "s2"}
if os.path.exists("Campaign/.melee.json"): MELEE = json.load(open("Campaign/.melee.json"))
ARCHER = "septima"
slots = json.load(open("Campaign/.slots.json")) if __import__("os").path.exists("Campaign/.slots.json") else {"s1": None, "s2": None}
def alive(c): return c["hp"] > 0 and c.get("status", "active") == "active"
print(run("round-start", *(sys.argv[2:])).split("order:")[0][:40])
s = st()
# foes already in a slot burn at the start of their initiative: handled when they act
while True:
    line = run("round-next")
    if "acts" not in line: print(line[:120]); break
    s = st(); k = s["order"][s["count_index"]]; c = s["combatants"][k]
    if not alive(c): continue
    for sl, f in list(slots.items()):
        if f and not alive(s["combatants"][f]): slots[sl] = None
    if c["side"] == "foe":
        if any(x.get("name") in ("frightened", "cowering") for x in c["conditions"]): continue
        mine = [sl for sl, f in slots.items() if f == k]
        if not mine:
            free = [sl for sl, f in slots.items() if f is None]
            if not free: continue
            sl = free[0]; slots[sl] = k
        else:
            sl = mine[0]
        if patch:
            o = run("damage", k, "--dice", "1d8", "--type", "fire", "--mundane"); print(f"  {k} burns: {o[:110]}")
            if not alive(st()["combatants"][k]): slots[sl] = None; continue
        t = SLOTW[sl]
        if not alive(st()["combatants"][t]):
            alt = [p for p in ("lucilla", "hrodvar", "varro", "vettius") if alive(st()["combatants"][p])]
            if not alt: continue
            t = alt[0]
        run("state", "distance", k, t, "5"); run("state", "engage", k, t)
        print(f"  {k}: " + run("attack", k, t, "--weapon", "short sword")[:170])
    else:
        if k in HOOK:
            print(f"  {k}: " + run(*HOOK[k].split("|"))[:200]); continue
        if k in SKIP: continue
        if k == ARCHER:
            q = [f for f, v in s["combatants"].items() if v["side"] == "foe" and alive(v) and f not in slots.values()]
            if q:
                run("state", "distance", k, q[0], "20"); print(f"  {k}: " + run("attack", k, q[0], "--range", "short")[:170])
            continue
        if k not in MELEE: continue
        sl = MELEE[k]; f = slots.get(sl) or next((x for x in slots.values() if x), None)
        if not f or not alive(s["combatants"][f]): continue
        run("state", "distance", k, f, "5"); run("state", "engage", k, f)
        o = run("attack", k, f); print(f"  {k}: " + o[:170])
        if "may cleave" in o:
            other = [x for x in slots.values() if x and x != f and alive(st()["combatants"][x])]
            if other:
                run("state", "engage", k, other[0]); print(f"  {k} cleave: " + run("attack", k, other[0], "--cleave")[:170])
        for sl2, f2 in list(slots.items()):
            if f2 and not alive(st()["combatants"][f2]): slots[sl2] = None
json.dump(slots, open("Campaign/.slots.json", "w"))
print(run("round-end")[:200])
s = st()
print("party hp:", {k: v["hp"] for k, v in s["combatants"].items() if v["side"] == "party" and v["hp"] < v["hp_max"]},
      "| foes left:", len([1 for v in s["combatants"].values() if v["side"] == "foe" and alive(v)]), "| slots", slots)
