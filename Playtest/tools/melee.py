"""Simple melee driver for the playtest: runs one round in initiative order. Each living party combatant in PLAN
attacks its engaged foe (or the first living foe it is told); each foe attacks the party member it is engaged with,
or engages a front-liner with room (CAP foes per front-liner). Prints one line per action. Usage:
  python3 melee.py '{"plan": {"aulus": "attack", ...}, "front": ["tarq","aulus","sabina"], "cap": 2, "declare": []}'"""
import json, subprocess, sys
A = ["bash", ".claude/skills/acks2-judge/scripts/acks.sh"]
cfg = json.loads(sys.argv[1])
def run(*args):
    p = subprocess.run(A + list(args), capture_output=True, text=True)
    return (p.stdout.strip().splitlines() or [p.stderr.strip()])[-1]
def st():
    return json.load(open("Campaign/combat-state.json"))
decl = []
for d in cfg.get("declare", []):
    decl += ["--declare", d]
print(run("round-start", *decl)[:120])
def alive(s, c):
    x = s["combatants"][c]
    return x["hp"] > 0 and x.get("status", "active") == "active"
def engaged_with(s, c):
    return [b if a == c else a for a, b in (tuple(p) for p in s["engaged"]) if c in (a, b)]
order = [o[0] if isinstance(o, list) else o for o in st()["order"]]
for c in order:
    s = st()
    if c not in s["combatants"] or not alive(s, c):
        continue
    me = s["combatants"][c]
    if "surprised" in (me.get("conditions") or []) and s["round"] == 1:
        continue
    foes = [k for k, v in s["combatants"].items() if v["side"] != me["side"] and alive(s, k)]
    if not foes:
        break
    eng = [e for e in engaged_with(s, c) if alive(s, e)]
    if me["side"] == "party":
        act = cfg["plan"].get(c)
        if not act or act == "hold":
            continue
        if act.startswith("treat:"):
            pid = act.split(":", 1)[1]
            if s["combatants"].get(pid, {}).get("hp", 1) <= 0:
                print(c, "treats", pid, "->", run("mortal-wounds", pid, "--healing-ranks", "1")[:400])
            continue
        tgt = eng[0] if eng else None
        if tgt is None and act == "attack" and c in cfg.get("front", []):
            # step up to the nearest foe not yet at its cap
            tgt = foes[0]
            run("state", "engage", c, tgt)
        if tgt is None:
            continue
        print(c, "->", run("attack", c, tgt)[:170])
    else:
        tgt = eng[0] if eng else None
        if tgt is None:
            front = [f for f in cfg.get("front", []) if f in s["combatants"] and alive(s, f)]
            load = {f: len([e for e in engaged_with(s, f) if alive(s, e)]) for f in front}
            room = [f for f in front if load[f] < cfg.get("cap", 2)]
            if not room:
                continue
            tgt = min(room, key=lambda f: load[f])
            run("state", "engage", c, tgt)
        print(c, "->", run("attack", c, tgt)[:170])
print(run("round-end")[:300])
