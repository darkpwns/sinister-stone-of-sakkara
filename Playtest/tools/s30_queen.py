"""S30 queen driver: ONE round. Melee party attack the queen; Vestus' Mage Missile (concentration); the queen bites a
random engaged foe (hidden 1d); stops (exit 3) when a party member falls or the queen is down. Run from the repo root."""
import json, re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
Q = "giant-ant-queen1"
MELEE = ["brennus", "iulia", "vettius", "hrodvar", "lucilla"]
def run(*a, env_ack=None):
    import os
    if env_ack: os.environ["ACKS_ACK"] = env_ack
    code, out = jacks.run(list(a))
    if env_ack: os.environ.pop("ACKS_ACK", None)
    print("  $", " ".join(a), "->", re.sub(r" \(src: .*", "", out.strip().splitlines()[-1] if out.strip() else "")[:240])
    return code, out
def st():
    c = json.load(open("Campaign/combat-state.json")); cb = c["combatants"]
    return cb if isinstance(cb, dict) else {x["id"]: x for x in cb}
run("round-start", "--declare", "vestus-the-unlikely:spell")
while True:
    code, out = run("round-next")
    if "round-end" in out or code != 0: break
    m = re.search(r"count \d+: (.+?) acts", out)
    if not m: break
    who = m.group(1)
    cb = st()
    if cb[Q]["hp"] <= 0: break
    ids = {v.get("name", k): k for k, v in cb.items()}
    pid = next((k for k, v in cb.items() if v.get("name") == who or v.get("perceived") == who), None)
    if who.startswith("Giant Ant Queen") or pid == Q:
        targets = [t for t in MELEE if cb[t]["hp"] > 0 and cb[t].get("status", "active") == "active"]
        code, out = run("roll", "--hidden", f"queen's target ({', '.join(targets)}):1d{len(targets)}")
        n = int(re.search(r"= (\d+)", out).group(1))
        run("attack", Q, targets[n - 1], env_ack="initiative-order")
    elif pid in MELEE and cb[pid]["hp"] > 0:
        run("attack", pid, Q)
    elif pid == "vestus-the-unlikely":
        code, out = run("roll", "Vestus: Mage Missile (1d4):1d4")
        n = int(re.search(r"= (\d+)", out).group(1))
        run("damage", Q, "--dice", str(n), "--type", "arcane", "--extraordinary", "--attacker", "vestus-the-unlikely")
    cb = st()
    if any(v["side"] == "party" and v["hp"] <= 0 for v in cb.values()):
        print("STOP: a party member is down"); sys.exit(3)
    if cb[Q]["hp"] <= 0:
        print("STOP: the queen is down"); sys.exit(3)
run("round-end")
