#!/usr/bin/env python3
"""S28 ward fight driver: the party inside the Underwatch shield's ward (Rulings S14: enchanted creatures cannot touch
anyone within; the barrier against one creature falls for the rest of the turn once anyone inside attacks it).
Run after round-start: steps round-next; party ids in FIGHT attack the first standing foe of PREFIX; REBUKER rebukes;
a foe whose barrier has fallen attacks a random party member among those who struck it (hidden 1dN); others are barred.
Felled undead are set destroyed (judge-notes S27). Usage: s28_ward.py PREFIX "fight ids" [rebuker] [first_actor]"""
import json, subprocess, sys
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True); o=(r.stdout+r.stderr).strip(); return (o.splitlines()[-1] if o else "").split(" (src")[0]
def runj(*a):
    r=subprocess.run(A+list(a)+["--json"],capture_output=True,text=True); t=r.stdout; i=t.find("{"); return json.loads(t[i:]) if i>=0 else {}
def cs():
    c=json.load(open(ST))["combatants"]; return c if isinstance(c,dict) else {x["id"]:x for x in c}
def standing(prefix): return [k for k,v in cs().items() if k.startswith(prefix) and v["hp"]>0 and v.get("status","active") not in ("destroyed","dead")]
def fell(prefix):
    for k,v in cs().items():
        if k.startswith(prefix) and v["hp"]<=0 and v.get("status")!="destroyed": run("state","set",k,"status=destroyed")
prefix=sys.argv[1]; fight=sys.argv[2].split(); reb=sys.argv[3] if len(sys.argv)>3 and sys.argv[3] else None
struck={}; pending=[sys.argv[4]] if len(sys.argv)>4 else []
while True:
    if pending: who=pending.pop(0)
    else:
        d=runj("round-next"); who=(d.get("data") or {}).get("next")
        if not who: print("round done"); break
    c=cs().get(who,{})
    if c.get("hp",0)<=0 or c.get("status") not in (None,"active"): continue
    if any(x.get("name") in ("surprised",) for x in c.get("conditions",[])): continue
    if c.get("side")=="party":
        st=standing(prefix)
        if not st: continue
        if who==reb: print("REBUKE", run("rebuke",who)[:300]); fell(prefix); continue
        if who in fight:
            t=st[0]; o=run("attack",who,t); print(o[:260]); struck.setdefault(t,[]).append(who); fell(prefix)
    else:
        if who in struck and c["hp"]>0 and c.get("status","active")=="active" and not any(x.get("name") in ("frightened","cowering") for x in c.get("conditions",[])):
            al=[p for p in struck[who] if cs()[p]["hp"]>0]
            if al:
                n=len(al); r=run("roll","--hidden",f"{who}'s target among those who struck it:1d{n}"); i=int(r.rsplit("=",1)[1].split()[0]) if "=" in r else 1
                print("FOE", run("attack",who,al[i-1])[:260])
print("standing:", standing(prefix))
