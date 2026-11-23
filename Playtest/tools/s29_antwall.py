#!/usr/bin/env python3
"""S29 the L5 tunnel mouth: Vestus' web fills the mouth (10' cube); the ants in it are webbed and fight the two front-
liners; the rest press behind and cannot reach the line (Judge's call). Each round, while fewer than WEB ants are in
the web, the next ants from the arrived pool push into it and are caught (webbed). Runs rounds (round-end, round-start,
fill, s29_melee.py) until no foe is left and the pool is empty, a party member falls, or the ants break (any foe
frightened, fleeing, retreating). Usage: s29_antwall.py ROUNDS "fight:…" "front:…" — pool in POOL below."""
import json, subprocess, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
ST = "Campaign/combat-state.json"
WEB = 3
# (round it reaches L5, id, how to bring it in)
POOL = [(3, "giant-ant-worker4", "return"), (3, "giant-ant-worker6", "return")] + \
       [(3, f"ant-l15-{i}", "add") for i in range(1, 7)] + [(3, f"ant-l16-{i}", "add") for i in range(1, 7)] + \
       [(4, "giant-ant-worker5", "return")] + [(4, f"ant-l14-{i}", "add") for i in range(1, 7)]
STATE_POOL = "Playtest/tools/.s29_antwall_pool.json"


def run(*a):
    code, out = jacks.run(list(a))
    return code, out.strip().splitlines()[-1] if out.strip() else ""


def cs():
    c = json.load(open(ST)); cb = c["combatants"]
    return c, (cb if isinstance(cb, dict) else {x["id"]: x for x in cb})


def active(x):
    return x.get("status", "active") == "active" and x["hp"] > 0


try:
    used = set(json.load(open(STATE_POOL)))
except Exception:
    used = set()
rounds = int(sys.argv[1]); rest = sys.argv[2:]
for _ in range(rounds):
    print(run("round-end")[1][:300])
    c, cb = cs()
    rnd = c["round"] + 1
    front = [x for x in rest if x.startswith("front:")][0].split(":", 1)[1].split(",")
    inweb = [k for k, v in cb.items() if v["side"] != "party" and active(v) and any(q.get("name") == "webbed" for q in v.get("conditions", []))]
    for (r, fid, how) in POOL:
        if len(inweb) >= WEB:
            break
        if r > rnd or fid in used:
            continue
        if how == "return":
            print(" ", run("state", "return", fid)[1][:150])
        else:
            print(" ", run("state", "add", fid, "--monster", "Giant Ant Worker", "--group", fid.rsplit("-", 1)[0],
                           "--perceived", "ants as big as men", "--set", "morale=4")[1][:150])
        run("state", "cond", fid, "webbed")
        live_front = [p for p in front if p in cb and active(cb[p])]
        for p in live_front:
            run("state", "engage", fid, p)
        used.add(fid); inweb.append(fid)
    json.dump(sorted(used), open(STATE_POOL, "w"))
    c, cb = cs()
    if not any(v["side"] != "party" and active(v) for v in cb.values()) and len(used) == len(POOL):
        print("no ants left"); break
    print(run("round-start")[1][:120])
    r = subprocess.run([sys.executable, "Playtest/tools/s29_melee.py"] + rest, capture_output=True, text=True)
    out = r.stdout + r.stderr
    print("\n".join(l[:230] for l in out.splitlines()[-4:]))
    if r.returncode == 3 or "PARTY DOWN" in out or "Traceback" in out:
        print("STOP"); sys.exit(3)
    c, cb = cs()
    broke = [k for k, v in cb.items() if v["side"] != "party" and active(v) and any(q.get("name") in ("frightened", "fleeing", "retreating", "cowering") for q in v.get("conditions", []))]
    if broke:
        print("ANTS BREAK:", broke); sys.exit(4)
    print("party:", [(k, v["hp"]) for k, v in cb.items() if v["side"] == "party" and v["hp"] < 99 and k in ("marcellus", "varro", "iulia", "brennus")])
