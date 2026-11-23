#!/usr/bin/env python3
"""S28 G13 driver (s27_g10.py with the S27 fixes): the party inside the Underwatch shield's ward at the G8 junction.
Skeletons are barred until struck (Rulings S14: the barrier falls against a creature for the rest of the turn once
anyone inside attacks or casts on it); struck ones then fight. Each round in initiative order: REB rebukes; Vestus casts
Fireball on FB rounds (one 7d6, Blast save each, up to 12 standing); FAN casters (round:id) fan up to 16 (1d8 each);
fighters attack a struck skeleton; a struck standing skeleton attacks a random fighter (hidden). Felled undead are set
destroyed at once (judge-notes S27). Usage: s28_g13.py ROUND FB_ROUNDS FAN_SPEC FIGHTERS"""
import json, subprocess, sys, os
struck_by={}
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True); o=(r.stdout+r.stderr).strip(); return (o.splitlines()[-1] if o else "").split(" (src")[0]
def runj(*a):
    r=subprocess.run(A+list(a)+["--json"],capture_output=True,text=True); t=r.stdout; i=t.find("{"); return json.loads(t[i:]) if i>=0 else {}
def total(line): return int(line.rsplit("=",1)[1].split()[0])
def cs():
    c=json.load(open(ST))["combatants"]; return c if isinstance(c,dict) else {x["id"]:x for x in c}
def standing(): return [k for k,v in cs().items() if v["side"]!="party" and v["hp"]>0 and v.get("status","active") not in ("destroyed","dead")]
def fell():
    n=0
    for k,v in cs().items():
        if v["side"]!="party" and v["hp"]<=0 and v.get("status")!="destroyed": run("state","set",k,"status=destroyed"); n+=1
    return n
SF="Playtest/tools/.s28_struck.json"
try: struck=set(json.load(open(SF)))
except Exception: struck=set()
r=int(sys.argv[1]); fb=[int(x) for x in sys.argv[2].split(",") if x]; fans={}
for x in sys.argv[3].split(","):
    if x: a,b=x.split(":"); fans.setdefault(int(a),[]).append(b)
fighters=sys.argv[4].split(); out=[]
dec=[]
if r in fb: dec+=["--declare","vestus-the-unlikely:spell"]
for c in fans.get(r,[]): dec+=["--declare",f"{c}:spell"]
print(run("round-start",*dec)[:400])
while True:
    d=runj("round-next"); who=(d.get("data") or {}).get("next")
    if not who: break
    c=cs().get(who,{})
    if c.get("hp",0)<=0 or c.get("status") not in (None,"active"): continue
    if any(x.get("name")=="surprised" for x in c.get("conditions",[])): continue
    sk=standing()
    if not sk: continue
    if c["side"]=="party":
        if who=="iulia":
            o=run("rebuke","iulia"); f=fell(); out.append(f"Iulia rebuke: {o[:200]} -> {f} destroyed")
        elif who=="vestus-the-unlikely" and r in fb:
            T=total(run("roll",f"Vestus' Fireball round {r}:7d6")); hit=sk[:12]; sv=[]
            for k in hit:
                s=run("save",k,"blast"); dmg=T//2 if "SUCCESS" in s else T
                run("damage",k,"--dice",f"{dmg}d1","--type","fire","--extraordinary"); struck.add(k); sv.append("S" if "SUCCESS" in s else "F")
            f=fell(); out.append(f"Vestus Fireball {T} on {len(hit)} ({''.join(sv)}) -> {f} destroyed")
        elif who in fans.get(r,[]):
            hit=sk[:16]
            for k in hit:
                s=run("save",k,"blast"); run("damage",k,"--dice","1d8","--type","fire","--extraordinary",*(["--half"] if "SUCCESS" in s else [])); struck.add(k)
            f=fell(); out.append(f"{who} Fan of Flames on {len(hit)} -> {f} destroyed")
        elif who in fighters:
            tg=[k for k in sk if k in struck]
            if tg:
                # Vettius takes the rear of a foe already engaged by others: vulnerable to him, backstab (RR Thief: +4, +2 dice at 8th; S17 routine)
                # backstab is the engine's (7.15.0): automatic on a vulnerable target or one engaged by two allies (rear)
                o=run("attack",who,tg[0]); f=fell(); out.append(o[:240]+(f" -> destroyed" if f else ""))
    else:
        if who in struck and not any(x.get("name") in ("frightened","cowering") for x in c.get("conditions",[])):
            al=[p for p in fighters if cs()[p]["hp"]>0]
            i=total(run("roll","--hidden",f"{who}'s target among the front:1d{len(al)}"))
            import os; wpn=os.environ.get("FOEWEAPON",""); out.append("FOE "+run("attack",who,al[i-1],*(["--weapon",wpn] if wpn else []))[:220])
run("round-end"); json.dump(sorted(struck),open(SF,"w"))
print("\n".join(out)); print(f"round {r} end: standing {len(standing())}")
