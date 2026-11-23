"""S31 K4 bone-golem driver: ONE round from round-start. Args: declare:ID,... smite:CASTER=G1+G2,... rebuke:ID
Party melee (MELEE) attack a golem whose barrier has fallen and which is engaged with them; Vestus' Mage Missile
on a fallen-barrier golem (if declared); Cotta shoots one. Golems: a golem still barred waits at the rim; one whose
barrier fell engages up to two front-liners and makes 4 sword attacks (masterwork +1/+1), split 2+2.
Smite Undead: one Death save per target; failure: destroyed (hp 0). The barrier falls against each target.
Stops (exit 3) when a party member falls."""
import json, os, random, re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
G = "greater-undead-bone-golem-sotn"
MELEE = ["brennus", "iulia", "lucilla"]
FRONT = ["brennus", "iulia", "lucilla"]
ARGS = {a.split(":", 1)[0]: a.split(":", 1)[1] for a in sys.argv[1:] if ":" in a}
DECL = [x for x in ARGS.get("declare", "").split(",") if x]
SMITE = {}
for part in [x for x in ARGS.get("smite", "").split(",") if x]:
    c, ts = part.split("="); SMITE[c] = [f"{G}{t[1:]}" for t in ts.split("+")]
REBUKE = ARGS.get("rebuke")
def run(*a, ack=None):
    if ack: os.environ["ACKS_ACK"] = ack
    code, out = jacks.run(list(a))
    os.environ.pop("ACKS_ACK", None)
    line = out.strip().splitlines()[-1] if out.strip() else ""
    print("  $", " ".join(a)[:70], "->", re.sub(r" \(src: .*", "", line)[:200])
    return code, out
def cs():
    c = json.load(open("Campaign/combat-state.json")); cb = c["combatants"]
    return c, (cb if isinstance(cb, dict) else {x["id"]: x for x in cb})
def alive(x): return x.get("status", "active") == "active" and x["hp"] > 0
def fallen(c, g):
    for w in (c.get("wards") or {}).values() if isinstance(c.get("wards"), dict) else (c.get("wards") or []):
        if g in (w.get("fallen") or w.get("fallen_for") or []): return True
        if w.get("fallen") is True: return True
    return bool(c.get("_s31_fallen", {}).get(g))
FALLEN = set(json.load(open("/tmp/claude-0/s31_fallen.json"))) if os.path.exists("/tmp/claude-0/s31_fallen.json") else set()
def save_fallen(): json.dump(sorted(FALLEN), open("/tmp/claude-0/s31_fallen.json", "w"))
def golems(cb): return [k for k, v in cb.items() if k.startswith(G) and alive(v)]
def engaged(c, a):
    return [x for e in (c.get("engaged") or []) if a in e for x in e if x != a]
_c0, _cb0 = cs(); DOWN0 = {k for k, v in _cb0.items() if v["side"] == "party" and v["hp"] <= 0}
MELEE = [m for m in MELEE if m not in DOWN0]; FRONT = [m for m in FRONT if m not in DOWN0]
args = ["round-start"] + sum([["--declare", f"{d}:spell"] for d in DECL], [])
run(*args)
while True:
    code, out = run("round-next")
    if "round-end" in out or code != 0: break
    m = re.search(r"count \d+: (.+?) (acts|is )", out)
    if not m or " is " in out[m.start():m.end()+3] and "cannot act" in out: continue
    who = m.group(1); c, cb = cs()
    ci = c.get("count_index") or 0; od = c.get("order") or []
    pick = [od[i] for i in (ci, ci - 1) if 0 <= i < len(od) and who in (cb[od[i]].get("perceived"), cb[od[i]].get("name"))]
    pid = pick[0] if pick else None
    if pid is None: continue
    if pid.startswith(G):
        if not alive(cb[pid]): continue
        if pid not in FALLEN: print(f"  {pid} waits at the rim (barred)"); continue
        tg = [t for t in engaged(c, pid) if t in cb and alive(cb[t])]
        for t in FRONT:
            if len(tg) >= 2: break
            if t not in tg and alive(cb[t]): run("state", "engage", pid, t); tg.append(t)
        for i in range(4):
            t = tg[i // 2] if len(tg) > 1 else tg[0]
            if not alive(cs()[1][t]): continue
            run("attack", pid, t, "--mod", "masterwork:+1", "--damage-mod", "1", ack="initiative-order")
    elif pid in SMITE:
        for g in SMITE[pid]:
            if g not in cb or not alive(cb[g]): continue
            code, o = run("save", g, "death", "--vs-effect", "Smite Undead")
            for b in ("iulia", "neris"): run("state", "ward", "fall", b, g)
            FALLEN.add(g)
            if "FAIL" in o: run("state", "set", g, "hp=0")
        save_fallen()
    elif pid == REBUKE:
        run("rebuke", pid)
    elif pid in MELEE:
        tg = [g for g in engaged(c, pid) if g in cb and alive(cb[g])]
        if not tg:
            cand = [g for g in golems(cb) if g in FALLEN]
            if cand and pid in FRONT: run("state", "engage", pid, cand[0]); tg = cand[:1]
        if tg: run("attack", pid, tg[0])
    elif pid == "vestus-the-unlikely" and pid in DECL:
        cand = [g for g in golems(cb) if g in FALLEN]
        if cand:
            code, o = run("roll", "Vestus: Mage Missile (1d4):1d4"); n = int(re.search(r"= (\d+)", o).group(1))
            run("damage", cand[0], "--dice", str(n), "--type", "arcane", "--extraordinary", "--attacker", pid)
    elif pid == "cotta":
        cand = [g for g in golems(cb) if g in FALLEN]
        if cand: run("attack", "cotta", cand[-1], "--kind", "missile", "--range", "short", "--through-melee")
    c, cb = cs()
    if any(v["side"] == "party" and v["hp"] <= 0 and k not in DOWN0 for k, v in cb.items()):
        print("STOP: a party member is down"); save_fallen(); sys.exit(3)
    if not golems(cb): print("STOP: no golems left"); save_fallen(); sys.exit(3)
save_fallen()
run("round-end")
