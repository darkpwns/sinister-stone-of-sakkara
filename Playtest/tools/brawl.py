"""Melee driver (S09): FOE attacks (all its attack routines) the first living target in TARGETS each round;
MELEE party ids attack FOE (berserk ids keep the berserk condition). One round per call. usage:
brawl.py FOE TARGETS(csv) MELEE(csv) [--weapon W] [--declare id:spell]"""
import json, subprocess, sys
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
def run(*a):
    o=subprocess.run(A+list(a),capture_output=True,text=True,timeout=120).stdout.strip().splitlines()
    return (o[-1] if o else "").split(" (src:")[0].split(" | NOTE")[0]
def st(): return json.load(open(ST))
foe=sys.argv[1]; targets=sys.argv[2].split(","); melee=sys.argv[3].split(",")
extra=sys.argv[4:]; weapon=None; decl=[]
i=0
while i<len(extra):
    if extra[i]=="--weapon": weapon=extra[i+1]; i+=2
    elif extra[i]=="--declare": decl+=["--declare",extra[i+1]]; i+=2
    else: i+=1
print(run("round-start",*decl)[:30])
def alive(c): return c["hp"]>0 and c.get("status","active")=="active"
nat=len([r for r in st()["combatants"][foe].get("monster",{}) ])
while True:
    line=run("round-next")
    if "acts" not in line: break
    s=st(); k=s["order"][s["count_index"]]; c=s["combatants"][k]
    if not alive(s["combatants"][foe]): continue
    if not alive(c): continue
    if k==foe:
        tl=[t for t in targets if t in s["combatants"] and alive(s["combatants"][t])]
        if not tl: continue
        t=tl[0]; run("state","distance",foe,t,"5"); run("state","engage",foe,t)
        for n in range(4):
            args=["attack",foe,t,"--attack",str(n)]+(["--weapon",weapon] if weapon else [])
            o=run(*args)
            if not o or "NOT ALLOWED" in o or "no attack" in o: break
            print(f"  {foe}->{t}: {o[:150]}")
            if not alive(st()["combatants"][t]):
                tl=[x for x in targets if alive(st()["combatants"][x])]
                if not tl: break
                t=tl[0]; run("state","distance",foe,t,"5"); run("state","engage",foe,t)
    elif k in melee:
        run("state","distance",k,foe,"5"); run("state","engage",k,foe)
        print(f"  {k}: "+run("attack",k,foe)[:170])
print(run("round-end")[:150])
s=st(); print("foe hp",s["combatants"][foe]["hp"],"| hurt:",{k:v["hp"] for k,v in s["combatants"].items() if v["side"]=="party" and v["hp"]<v["hp_max"]})
