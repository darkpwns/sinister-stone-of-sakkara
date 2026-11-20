#!/usr/bin/env python3
"""dice.py [--open|--hidden] "label:NdS+M[xK]" ...   (cryptographically random; every roll is logged)

--open   : shown to the player (default).  --hidden : Judge-only.
Each roll is appended to the roll log (campaign.yaml paths.state.roll_log) with the current session
number from Campaign State. snapshot.py publishes this session's open rolls; hidden rolls never leave
the log except into the session log's collapsed Judge block (`dice.py --dump hidden`).
--dump open|hidden : print this session's rolls of that kind as markdown lines, roll nothing.
"""
import json, random, re, sys, time
sys.path.insert(0, __import__("os").path.dirname(__file__))
import jlib

rng = random.SystemRandom()
args = sys.argv[1:]
vis = "open"
if args and args[0] in ("--open", "--hidden"):
    vis = args.pop(0)[2:]
cfg = jlib.config()
log = jlib.path(cfg["paths"]["state"]["roll_log"])
fm, _ = jlib.read_note(cfg["paths"]["state"]["campaign_state"])
session = fm.get("session", 0)

if args and args[0] == "--dump":
    want = args[1] if len(args) > 1 else "hidden"
    try:
        for line in open(log, encoding="utf-8"):
            r = json.loads(line)
            if r["session"] == session and r["vis"] == want:
                print(f"- {r['label']}: {r['spec']} → {r['rolls']}{r['mod_txt']} = {r['total']}")
    except FileNotFoundError:
        pass
    sys.exit(0)

out = open(log, "a", encoding="utf-8")
for expr in args:
    label, _, spec = expr.rpartition(":")
    m = re.fullmatch(r"(\d*)d(\d+|%)([+-]\d+)?(?:x(\d+))?", spec.replace(" ", "").lower())
    if not m:
        print(f"{expr}: BAD EXPRESSION"); continue
    n = int(m.group(1) or 1); s = 100 if m.group(2) == "%" else int(m.group(2))
    mod = int(m.group(3) or 0); times = int(m.group(4) or 1)
    for _ in range(times):
        rolls = [rng.randint(1, s) for _ in range(n)]
        tot = sum(rolls) + mod
        mod_txt = f" {mod:+d}" if mod else ""
        print(f"{'[H] ' if vis == 'hidden' else ''}{label or spec}: {spec} -> {rolls}{mod_txt} = {tot}")
        out.write(json.dumps({"session": session, "t": int(time.time()), "vis": vis, "label": label or spec,
                              "spec": spec, "rolls": rolls, "mod_txt": mod_txt, "total": tot}) + "\n")
