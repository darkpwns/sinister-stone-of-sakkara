#!/usr/bin/env python3
"""brief.py : everything the resume step reads, in one print — Campaign State, World State, Rulings,
the tail of the latest session log, the handoff (its generated block made fresh from the state files: date, party,
adventure, wages, what the schedule holds due, the standing reminders of the lessons index, lessons to escalate, then
the Judge's notes), uncommitted changes, and whether bootstrap is needed."""
import glob, os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import jlib

cfg = jlib.config(); st = cfg["paths"]["state"]
for key in ("campaign_state", "world_state", "rulings"):
    print(f"===== {st[key]}")
    print(open(jlib.path(st[key]), encoding="utf-8").read().strip())
logs = [p for p in glob.glob(jlib.path(cfg["logs"]["session_log"]["folder"]) + "/S*.md")]
print("===== latest session log")
if logs:
    latest = max(logs, key=os.path.getmtime)
    lines = open(latest, encoding="utf-8").read().splitlines()
    print(os.path.relpath(latest, jlib.ROOT)); print("\n".join(lines[-40:]))
else:
    print("(none yet)")
print("===== handoff (generated now from the state files; the Judge's notes below it)")
try:
    import handoff
    print(handoff.compose(cfg).strip())
except Exception as e:                           # a brief never fails for want of the handoff
    print(f"(handoff unavailable: {e})")
fm, _ = jlib.read_note(st["campaign_state"])
print("===== status")
print("bootstrap needed" if not (fm.get("public") or {}).get("party") else f"session {fm.get('session')}, party of {len(fm['public']['party'])}")
dirty = subprocess.run(["git", "-C", jlib.ROOT, "status", "--short"], capture_output=True, text=True).stdout.strip()
print("uncommitted changes:\n" + dirty if dirty else "working tree clean")
