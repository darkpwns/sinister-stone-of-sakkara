#!/usr/bin/env python3
"""S27 G10 grind: the party inside Iulia's sustained holy circle at the G8 junction; G10's skeletons (and any summoned
berserkers) are barred (no attacks). Each round: Iulia rebukes (engine: all undead; skeletons destroyed at 8th level);
area spells on given rounds: FB rounds (Vestus, 7d6 rolled once, Blast save each, up to 12 targets in the burst),
FAN rounds:caster (1d8 each, up to 16 caster-chosen, Blast save each). Usage: s27_g10.py MAXROUNDS FB_ROUNDS FAN_SPEC"""
import json, subprocess, sys
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True); o=(r.stdout+r.stderr).strip(); return (o.splitlines()[-1] if o else "").split(" (src")[0]
def total(line): return int(line.rsplit("=",1)[1].split()[0])
def st():
    cs=json.load(open(ST))["combatants"]; return cs if isinstance(cs,dict) else {c["id"]:c for c in cs}
def alive(grp=None): return [k for k,v in st().items() if v["side"]!="party" and v["hp"]>0 and v.get("status","active")=="active" and (grp is None or v.get("group")==grp)]
maxr=int(sys.argv[1]); fb=[int(x) for x in sys.argv[2].split(",") if x]; fans={}
for x in (sys.argv[3] if len(sys.argv)>3 else "").split(","):
    if x: r,c=x.split(":"); fans.setdefault(int(r),[]).append(c)
for r in range(1,maxr+1):
    sk=[k for k in alive() if k.startswith("sk")]
    if not sk: print(f"round {r}: no skeleton stands"); break
    dec=[]; 
    if r in fb: dec+=["--declare","vestus-the-unlikely:spell"]
    for c in fans.get(r,[]): dec+=["--declare",f"{c}:spell"]
    run("round-start",*dec)
    reb=run("rebuke","iulia"); before=len(sk); sk=[k for k in alive() if k.startswith("sk")]
    msg=f"round {r}: rebuke {reb[:60]} -> {before-len(sk)} destroyed"
    if r in fb and sk:
        T=total(run("roll","--hidden",f"Vestus' Fireball round {r}:7d6")); hit=0
        for k in sk[:12]:
            sv=run("save",k,"blast"); d=T//2 if "SUCCESS" in sv else T
            run("state","set",k,f"hp={st()[k]['hp']-d}"); hit+=1
        run("actor","set","vestus-the-unlikely","state.spells_used",json.dumps(["Fireball"]*(sum(1 for x in fb if x<=r))),"--cause","Fireballs in the G10 grind, day 467")
        msg+=f"; Fireball {T} on {hit}"
    for c in fans.get(r,[]):
        sk=[k for k in alive() if k.startswith("sk")]
        for k in sk[:16]:
            sv=run("save",k,"blast"); run("damage",k,"--dice","1d8","--type","fire","--extraordinary",*(["--half"] if "SUCCESS" in sv else []))
        msg+=f"; {c} Fan on {min(16,len(sk))}"
    for i in range(40):
        l=run("round-next")
        if "all combatants" in l or "round-end" in l: break
    run("round-end")
    print(msg+f"; standing {len([k for k in alive() if k.startswith('sk')])}")
