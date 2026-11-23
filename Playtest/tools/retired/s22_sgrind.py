#!/usr/bin/env python3
"""S1/S4 lizardman-skeleton grind (S22): the party inside a holy circle; each round 2d10 rise from S1 (56) and from
round 2 another 2d10 from S4 (64); Iulia rebukes every round; area spells on given rounds (VESTUS_FB=r1,r2; FANS=r:caster,...).
Skeletons are barred by the circle (no attacks). Prints one line per round. Usage: s22_sgrind.py MAXROUNDS FB_ROUNDS FAN_SPEC"""
import json, subprocess, sys
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True); o=(r.stdout+r.stderr).strip(); return o.splitlines()[-1] if o else ""
def runj(*a):
    r=subprocess.run(A+list(a)+["--json"],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return {}
def roll(label,spec):
    d=runj("roll","--hidden",f"{label}:{spec}"); 
    try: return d["rolls"][0]["total"]
    except Exception:
        l=run("roll","--hidden",f"{label}:{spec}"); return int(l.rsplit("=",1)[1].split()[0])
def alive():
    s=json.load(open(ST)); return [k for k,v in s["combatants"].items() if v["side"]!="party" and v["hp"]>0 and v.get("status","active")=="active"]
maxr=int(sys.argv[1]); fb=[int(x) for x in sys.argv[2].split(",") if x]; fans={}
for x in sys.argv[3].split(","):
    if x: r,c=x.split(":"); fans.setdefault(int(r),[]).append(c)
pool={"s1":56,"s4":64}; n=0; killed=0; wc=4
for r in range(1,maxr+1):
    add=0
    for g,k in (("s1",1),("s4",2)):
        if r>=k and pool[g]>0:
            c=min(pool[g],roll(f"{g.upper()} skeletons climbing out, round {r}","2d10")); pool[g]-=c
            for i in range(c):
                n+=1; run("state","add",f"sk{n}","--monster","Skeleton","--group","skel","--perceived","a lizard-man skeleton with a curved bronze sword")
                run("state","set",f"sk{n}","hd=2","hp=9","hp_max=9","ac=3","rebuke_as=skeleton","attack_throw=8")
            add+=c
    dec=[]
    if r in fb: dec+=["--declare","vestus-the-unlikely:spell"]
    for c in fans.get(r,[]): dec+=["--declare",f"{c}:spell"]
    run("round-start",*dec)
    word=""
    if r>=2 and wc>0:
        wc-=1; sv=run("save","iulia","spells"); word="Word of Command on Iulia: "+("saved" if "SUCCESS" in sv else "HALTED (no rebuke)")
    before=len(alive())
    reb=runj("rebuke","iulia") if "HALTED" not in word else {}; dest=len([c for c in (reb.get("changes") or []) if "destroyed" in c])
    area=[]
    if r in fb:
        t=alive()[:14]; dmg=roll(f"Vestus' Fireball round {r}","6d6"); k=0
        for x in t:
            sv=run("save",x,"blast"); half=["--half"] if "SUCCESS" in sv else []
            o=run("damage",x,"--dice",str(dmg),"--type","fire","--extraordinary",*half)
            if "-> 0" in o or "-> -" in o: k+=1
        area.append(f"Fireball {dmg} on {len(t)}: {k} down")
    for c in fans.get(r,[]):
        t=alive()[:16]; dmg=roll(f"{c}'s Fan of Flames round {r}","1d8"); k=0
        for x in t:
            sv=run("save",x,"blast"); half=["--half"] if "SUCCESS" in sv else []
            o=run("damage",x,"--dice",str(dmg),"--type","fire","--extraordinary",*half)
            if "-> 0" in o or "-> -" in o: k+=1
        area.append(f"{c} Fan {dmg} on {len(t)}: {k} down")
    run("round-end")
    left=len(alive()); killed=n-left
    print(f"R{r}: +{add} risen (S1 left {pool['s1']}, S4 left {pool['s4']}); rebuke destroyed {dest}; {'; '.join(area)}; {word}; standing {left}; destroyed so far {killed}",flush=True)
    if pool["s1"]==0 and pool["s4"]==0 and left==0: print("ALL DESTROYED",flush=True); break
