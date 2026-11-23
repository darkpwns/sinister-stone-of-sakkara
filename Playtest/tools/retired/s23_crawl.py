#!/usr/bin/env python3
"""S23 driver for the day-440 carrion horror fight: one round per call (round-start .. round-end).
Foes: 8 stinger attacks each on an engaged, able target (re-target when the target is paralyzed or down); a damaging
hit: Paralysis save, fail = paralyzed 2d4 turns. Party: melee on the foe each engages; Vestus (2) and Phaedra (1)
cast Fan of Flames (caster's choice: both foes, Blast save half) while their counts last."""
import json, subprocess, os
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"; FF="Campaign/.fan.json"
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True,timeout=120); o=(r.stdout+r.stderr).strip()
    return (o.splitlines()[-1] if o else "").split(" (src")[0]
def st():
    cs=json.load(open(ST))['combatants']; return {c['id']:c for c in (cs if isinstance(cs,list) else cs.values())}
def cn(c): return [(x.get('name') if isinstance(x,dict) else x) for x in (c.get('conditions') or [])]
def ok(c): return c.get('hp',0)>0 and c.get('status','active')=='active' and not set(cn(c))&{'paralyzed','surprised','unconscious'}
ENG={'carrion-horror1':[],'carrion-horror2':['iulia','marcellus','brennus','varro','vettius','lucilla']}
FAN=json.load(open(FF)) if os.path.exists(FF) else {'vestus-the-unlikely':2,'phaedra':1}
def act(cid):
    s=st(); c=s[cid]; who=c.get('name',cid)
    if not ok(c): print(f"  {who}: cannot act"); return
    if c['side']=='party':
        if FAN.get(cid,0)>0 and cid in DEC:
            FAN[cid]-=1; print(f"  {who} casts Fan of Flames")
            for f in ENG:
                if s[f].get('hp',0)>0:
                    sv=run("save",f,"blast"); print("    ",sv)
                    print("    ",run("damage",f,"--dice","1d8","--type","fire","--extraordinary",*(["--half"] if "SUCCESS" in sv else [])))
            return
        t=next((f for f,e in ENG.items() if cid in e and s[f].get('hp',0)>0),None)
        if t: print("  ",run("attack",cid,t))
        return
    for k in range(8):
        s=st()
        if s[cid].get('hp',0)<=0: return
        t=next((p for p in ENG[cid] if ok(s[p])),None)
        if not t: print(f"  {who}: no able foe in reach"); return
        o=run("attack",cid,t,"--attack","0"); print("  ",o)
        if "HIT" in o:
            sv=run("save",t,"paralysis"); print("     ",sv)
            if "FAIL" in sv:
                r=run("roll","--hidden","paralysis turns:2d4"); n=int(r.split("=")[-1].strip())
                print("     ",run("state","cond",t,"paralyzed","--rounds",str(n*10)),f"({n} turns)")
s=st(); DEC=[c for c,n in FAN.items() if n>0 and ok(s[c])]
import sys
if "--continue" not in sys.argv: print(run("round-start",*sum([["--declare",f"{x}:spell"] for x in DEC],[])))
seen=0
for _ in range(40):
    l=run("round-next")
    if "all combatants" in l or "round-end" in l: break
    d=json.load(open(ST)); o=d['order']; ci=d['count_index']
    e=o[ci] if ci is not None and ci<len(o) else None
    ids=[e]
    print(l[:70])
    for i in ids:
        if i: act(i)
json.dump(FAN,open(FF,'w')); print(run("round-end"))
