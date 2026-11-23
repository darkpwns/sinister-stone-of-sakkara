#!/usr/bin/env python3
"""S28 G25 faewyrd round (run after round-start): the party holds inside the Underwatch ward (Rulings S14: the faewyrd
cannot touch anyone within while nobody attacks them). Iulia rebukes at her initiative; each standing, unfrightened
faewyrd whispers at its initiative to 2 party members beside the ward's edge (hidden pick): save vs Death or maddened
(SOTN; +1 for the ward against an evil effect, -1 per extra faewyrd heard, net 0: plain save). Prints maddened ids."""
import json, subprocess, random
A=["bash",".claude/skills/acks2-judge/scripts/acks.sh"]; ST="Campaign/combat-state.json"
def run(*a):
    r=subprocess.run(A+list(a),capture_output=True,text=True); o=(r.stdout+r.stderr).strip(); return (o.splitlines()[-1] if o else "").split(" (src")[0]
def runj(*a):
    r=subprocess.run(A+list(a)+["--json"],capture_output=True,text=True); t=r.stdout; i=t.find("{"); return json.loads(t[i:]) if i>=0 else {}
def cs():
    c=json.load(open(ST))["combatants"]; return c if isinstance(c,dict) else {x["id"]:x for x in c}
def total(l): return int(l.rsplit("=",1)[1].split()[0])
P=["vettius","neris","iulia","varro","hrodvar","brennus","phaedra","marcellus","vestus-the-unlikely","cotta","lucilla","aelia"]
mad=[]
while True:
    d=runj("round-next"); who=(d.get("data") or {}).get("next")
    if not who: break
    c=cs()[who]
    if c["hp"]<=0 or c.get("status")!="active" or any(x.get("name")=="surprised" for x in c.get("conditions",[])): continue
    if who=="iulia":
        if any(v["side"]!="party" and v["hp"]>0 and v.get("status")=="active" for v in cs().values()): print("Iulia:", run("rebuke","iulia")[:300])
    elif c["side"]!="party":
        if any(x.get("name") in ("frightened","cowering") for x in c.get("conditions",[])): continue
        for k in range(2):
            i=total(run("roll","--hidden",f"{who}'s whisper reaches (1d12, party order)","--",)) if False else total(run("roll","--hidden",f"{who}'s whisper reaches:1d12"))
            v=P[i-1]; s=run("save",v,"death"); print(f"whisper ({who}) -> {s[:90]}")
            if "FAIL" in s and v not in mad: mad.append(v)
run("round-end"); print("MADDENED:", mad)
print("standing:", [(k,v["hp"],v.get("status"),[x["name"] for x in v.get("conditions",[])]) for k,v in cs().items() if v["side"]!="party"])
