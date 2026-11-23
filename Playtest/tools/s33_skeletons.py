"""S33 R3/R4 tunnel driver: ONE round from round-start, the company inside the Underwatch shield and Neris' Holy
Circle (Sustained) at R4's base, the risen R3 skeletons filling the 10' tunnel and spilling back into R3.
Args (all optional): declare:ID,...  fire:CASTER (Fireball, 7d6; caught: 8 = a 20' sphere in a 10' tunnel)
bolt:CASTER (Thunderbolt, 6d6; caught: 4 in the tunnel's file + hidden 1d6+2 in R3's crowd beyond)
smite:CASTER=N (Smite Undead: N skeletons destroyed, no save: skeletons, RR p. 246)
melee:ID,...  (attack a skeleton at the rim; cleaves on kills) shoot:ID,... (bow at a skeleton beyond the rim).
Skeletons: at most two at the rim (tunnel 10' wide, two abreast; judge-screen §3). A barred one waits; one whose
barrier fell (it was struck from within) attacks a front-liner engaged with it. Stops (exit 3) when a party member falls.
Every attack, save and damage goes through the engine (jacks.run), stepped by round-next."""
import json, os, random, re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
SP = "/tmp/claude-0/s33_fallen.json"
ARGS = {a.split(":", 1)[0]: a.split(":", 1)[1] for a in sys.argv[1:] if ":" in a}
L = lambda k: [x for x in ARGS.get(k, "").split(",") if x]
DECL, MELEE, SHOOT = L("declare"), L("melee"), L("shoot")
FIRE, BOLT = ARGS.get("fire"), ARGS.get("bolt")
SMITE = dict(p.split("=") for p in L("smite"))
FALLEN = set(json.load(open(SP))) if os.path.exists(SP) else set()
def save_fallen(): json.dump(sorted(FALLEN), open(SP, "w"))
def run(*a):
    code, out = jacks.run(list(a))
    line = out.strip().splitlines()[-1] if out.strip() else ""
    print("  $", " ".join(a)[:60], "->", re.sub(r" \(src: .*", "", line)[:190])
    return code, out
def cs():
    c = json.load(open("Campaign/combat-state.json")); cb = c["combatants"]
    return c, (cb if isinstance(cb, dict) else {x["id"]: x for x in cb})
def alive(x): return x.get("status", "active") == "active" and x["hp"] > 0
def skels(cb): return sorted([k for k in cb if k.startswith("skel") and alive(cb[k])], key=lambda k: int(k[4:]))
def rim(cb): return skels(cb)[:2]
def fall(t):
    for b in ("iulia", "neris"): run("state", "ward", "fall", b, t)
    FALLEN.add(t); save_fallen()
def blast(who, dice, kind, ids):
    code, o = run("roll", f"{who}: {kind} ({dice}):{dice}"); dmg = int(re.search(r"= (\d+)", o).group(1))
    for s in ids:
        code, o = run("save", s, "blast"); h = ["--half"] if "SUCCESS" in o else []
        run("damage", s, "--dice", str(dmg), "--type", "fire" if kind == "Fireball" else "electrical", "--extraordinary", *h, "--attacker", who)
        fall(s)
_c0, _cb0 = cs()
DOWN0 = {k for k, v in _cb0.items() if v["side"] == "party" and v["hp"] <= 0}
run(*(["round-start"] + sum([["--declare", f"{d}:spell"] for d in DECL], [])))
while True:
    code, out = run("round-next")
    if "round-end" in out or code != 0: break
    m = re.search(r"count -?\d+: (.+?) (acts|is )", out)
    if not m or "cannot act" in out: continue
    who = m.group(1); c, cb = cs()
    ci = c.get("count_index") or 0; od = c.get("order") or []
    pick = [od[i] for i in (ci, ci - 1) if 0 <= i < len(od) and who in (cb[od[i]].get("perceived"), cb[od[i]].get("name"))]
    pid = pick[0] if pick else None
    if pid is None: continue
    if pid.startswith("skel"):
        if not alive(cb[pid]): continue
        if pid not in rim(cb): continue                       # in the press beyond the rim
        if pid not in FALLEN: print(f"  {pid} presses at the ward (barred)"); continue
        foes = [t for t in ("brennus", "lucilla") if t in cb and alive(cb[t])]
        if not foes: continue
        t = random.choice(foes); run("state", "engage", pid, t); run("attack", pid, t)
    elif pid == FIRE:
        live = skels(cb); ids = live[2:10] if len(live) > 2 else live
        blast(pid, "7d6", "Fireball", ids)
    elif pid == BOLT:
        live = skels(cb); code, o = run("roll", "--hidden", f"{pid}'s Thunderbolt: skeletons caught in R3's crowd beyond the tunnel:1d6+2")
        k = 4 + int(re.search(r"= (-?\d+)", o).group(1)); blast(pid, "6d6", "Thunderbolt", live[:k])
    elif pid in SMITE:
        live = skels(cb)[: int(SMITE[pid])]
        print(f"  {pid}: Smite Undead destroys {len(live)} skeletons (no save, RR p. 246)")
        for s in live: run("state", "set", s, "hp=0"); FALLEN.add(s)
        save_fallen()
    elif pid in MELEE and alive(cb[pid]):
        flags = []
        for _ in range(8):
            c, cb = cs(); r = rim(cb)
            if not r: break
            t = r[0]; run("state", "engage", pid, t); fall(t)
            code, o = run("attack", pid, t, *flags)
            if "may cleave" not in o: break
            flags = ["--cleave"]
    elif pid in SHOOT and alive(cb[pid]):
        live = skels(cb)
        if len(live) > 2:
            t = live[2]; fall(t); run("attack", pid, t, "--range", "short")
    c, cb = cs()
    if any(v["side"] == "party" and v["hp"] <= 0 and k not in DOWN0 for k, v in cb.items()):
        print("STOP: a party member is down"); sys.exit(3)
c, cb = cs(); print("skeletons standing:", len(skels(cb)))
