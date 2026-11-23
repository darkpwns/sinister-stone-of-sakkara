"""S34 O1 statue driver (copy of s32_statues.py: ward falls on blasts, Striking on Brennus): ONE round already started. Party melee hit the weakest statue whose barrier fell; Vestus'
Fireball / Phaedra's Thunderbolt (if 'fire' / 'bolt' given) on a hidden 1d3+1 / 1d3 of the live statues; Cotta shoots;
a statue whose barrier fell slams a front-liner (5d4 at 6+, engine); barred statues wait. Stops on a fallen member."""
import json, os, re, sys, random
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
FIRE = "fire" in sys.argv; BOLT = "bolt" in sys.argv
MELEE = ["brennus", "iulia", "lucilla", "vettius"]
EXTRA = {"brennus": ["--extra-dice", "Striking:1d6:luminous"]}
def run(*a, ack=None):
    if ack: os.environ["ACKS_ACK"] = ack
    code, out = jacks.run(list(a)); os.environ.pop("ACKS_ACK", None)
    line = out.strip().splitlines()[-1] if out.strip() else ""
    print("  $", " ".join(a)[:60], "->", re.sub(r" \(src: .*", "", line)[:170]); return code, out
def cs():
    c = json.load(open("Campaign/combat-state.json")); cb = c["combatants"]
    return c, (cb if isinstance(cb, dict) else {x["id"]: x for x in cb})
def alive(x): return x.get("status", "active") == "active" and x["hp"] > 0
def statues(cb): return [k for k in sorted(cb) if k.startswith("statue") and alive(cb[k])]
FALLEN = set(json.load(open("/tmp/claude-0/s34_fallen.json"))) if os.path.exists("/tmp/claude-0/s34_fallen.json") else set()
def blast(who, dice, kind, n):
    c, cb = cs(); live = statues(cb); random.shuffle(live)
    code, o = run("roll", "--hidden", f"{who}'s {kind}: statues caught:{n}"); k = int(re.search(r"= (-?\d+)", o).group(1))
    code, o = run("roll", f"{who}: {kind} ({dice}):{dice}"); dmg = int(re.search(r"= (\d+)", o).group(1))
    for s in live[:k]:
        code, o = run("save", s, "blast"); h = ["--half"] if "SUCCESS" in o else []
        run("damage", s, "--dice", str(dmg), "--type", "fire" if kind == "Fireball" else "electrical", "--extraordinary", *h, "--attacker", who)
        FALLEN.add(s)
        for b in ("iulia", "neris"): run("state", "ward", "fall", b, s)
while True:
    code, out = run("round-next")
    if "round-end" in out or code != 0: break
    m = re.search(r"count -?\d+: (.+?) (acts|is )", out)
    if not m or "cannot act" in out: continue
    who = m.group(1); c, cb = cs(); ci = c.get("count_index") or 0; od = c.get("order") or []
    pick = [od[i] for i in (ci, ci - 1) if 0 <= i < len(od) and who in (cb[od[i]].get("perceived"), cb[od[i]].get("name"))]
    pid = pick[0] if pick else None
    if not pid or not alive(cb[pid]): continue
    live = statues(cb)
    if not live: break
    if pid.startswith("statue"):
        if pid not in FALLEN: print(f"  {pid} waits (barred)"); continue
        t = random.choice([x for x in ["brennus", "iulia", "lucilla"] if alive(cb[x])])
        run("state", "engage", pid, t); run("attack", pid, t, ack="initiative-order")
    elif pid in MELEE:
        tg = sorted([s for s in live if s in FALLEN], key=lambda s: cb[s]["hp"])
        if tg: run("state", "engage", pid, tg[0]); run("attack", pid, tg[0], *EXTRA.get(pid, []))
    elif pid == "cotta":
        tg = sorted([s for s in live if s in FALLEN], key=lambda s: cb[s]["hp"])
        if tg: run("attack", "cotta", tg[0], "--kind", "missile", "--range", "short", "--through-melee")
    elif pid == "vestus-the-unlikely" and FIRE: blast(pid, "7d6", "Fireball", "1d3+1")
    elif pid == "phaedra" and BOLT: blast(pid, "6d6", "Thunderbolt", "1d3")
    c, cb = cs()
    if any(v["side"] == "party" and v["hp"] <= 0 for v in cb.values()): print("STOP: a member is down"); break
    if not statues(cb): print("STOP: no statues left"); break
json.dump(sorted(FALLEN), open("/tmp/claude-0/s34_fallen.json", "w"))
