#!/usr/bin/env python3
"""One combat round in initiative order: listed party fighters attack living foes (spread); each foe attacks one listed fighter with each of its attacks. Usage: melee2.py FIGHTERS_CSV [id:NAME:+N ...]"""
import json, subprocess, sys
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
fighters=sys.argv[1].split(","); mods={}
for a in sys.argv[2:]:
    i,rest=a.split(":",1); mods.setdefault(i,[]).append(rest)
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True); o=(r.stdout+r.stderr).strip(); return o.splitlines()[-1] if o else ""
def st(): return json.load(open(ST))
def conds(c): return [x["name"] if isinstance(x,dict) else x for x in (c.get("conditions") or [])]
def alive(c): return c.get("hp",0)>0 and c.get("status","active")=="active"
run("round-start"); i=0
while True:
    l=run("round-next")
    if "acts" not in l: break
    s=st(); who=s["order"][s["count_index"]] if s.get("count_index") is not None else None
    if isinstance(who,dict): who=who.get("id")
    if not who or who not in s["combatants"]: continue
    c=s["combatants"][who]
    if not alive(c) or set(conds(c))&{"cowering","surprised","unconscious","slumbering","paralyzed"}: continue
    foes=[k for k,v in s["combatants"].items() if v["side"]!=c["side"] and alive(v)]
    if not foes: break
    i+=1
    if c["side"]=="party":
        if who not in fighters: continue
        t=foes[i%len(foes)]; run("state","engage",who,t)
        args=["attack",who,t]
        for m in mods.get(who,[]): args+=["--mod",m]
        print("  "+run(*args).split(" (src")[0][:140])
    else:
        tg=[k for k in fighters if alive(s["combatants"].get(k,{}))]
        if not tg: break
        t=tg[i%len(tg)]; run("state","engage",who,t)
        for ai in range(2 if "Prawn" in c.get("name","") else 1):
            print("  "+run("attack",who,t,"--attack",str(ai)).split(" (src")[0][:140])
print(run("round-end").split(" (src")[0][:160])
