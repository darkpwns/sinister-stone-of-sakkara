#!/usr/bin/env python3
"""brief.py [--full] : what the resume step reads, in one print, and no more (C5; it printed a thousand lines):
Campaign State (whole: it is short), the handoff (its generated block made fresh from the state files: date, party,
who is left behind, adventure, wages, what the schedule holds due, the standing reminders and the lessons to
escalate, then the Judge's notes), the last rows of the Rulings table, the World State sections the resume names
(config `brief.world_sections`, default: Prep queue, NPC attitudes, and the latest entries of Scheduled events),
the tail of the latest session log and of the playtest's judge notes when the campaign has them (config
`brief.tails`), uncommitted changes, and whether bootstrap is needed. `--full` prints the three state notes whole,
as before.

Config (campaign.yaml, all optional):
  brief: {rulings_rows: 25, world_sections: ["Prep queue", "NPC attitudes", "Scheduled events:12"],
          tails: ["Playtest/judge-notes.txt:30"], session_lines: 40}
"""
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
import jlib  # noqa: E402

cfg = jlib.config()
st = cfg["paths"]["state"]
B = cfg.get("brief") or {}
full = "--full" in sys.argv[1:]


def section(text, name, n=None):
    """A '## name' section of a note (its first n bullet entries when n is given)."""
    m = re.search(r"^## " + re.escape(name) + r".*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return None
    body = m.group(1).strip("\n")
    if n:
        items, cur = [], []
        for ln in body.splitlines():
            if ln.startswith("- ") and cur:
                items.append("\n".join(cur))
                cur = []
            cur.append(ln)
        if cur:
            items.append("\n".join(cur))
        body = "\n".join(items[:n])
    return body


print(f"===== {st['campaign_state']}")
print(open(jlib.path(st["campaign_state"]), encoding="utf-8").read().strip())
print("===== handoff (generated now from the state files; the Judge's notes below it)")
try:
    import handoff
    print(handoff.compose(cfg).strip())
except Exception as e:                           # a brief never fails for want of the handoff
    print(f"(handoff unavailable: {e})")
if full:
    for key in ("world_state", "rulings"):
        print(f"===== {st[key]}")
        print(open(jlib.path(st[key]), encoding="utf-8").read().strip())
else:
    rows = [ln for ln in open(jlib.path(st["rulings"]), encoding="utf-8").read().splitlines() if ln.startswith("| ")]
    n = int(B.get("rulings_rows", 25))
    print(f"===== {st['rulings']} (the last {n} rows of {max(0, len(rows) - 2)}; --full for all)")
    print("\n".join(rows[:2] + rows[2:][-n:]))
    ws = open(jlib.path(st["world_state"]), encoding="utf-8").read()
    for spec in B.get("world_sections") or ["Prep queue", "NPC attitudes", "Scheduled events:12"]:
        name, _, k = str(spec).partition(":")
        body = section(ws, name, int(k) if k else None)
        if body is not None:
            print(f"===== {st['world_state']}: ## {name}" + (f" (the first {k} entries)" if k else ""))
            print(body)
logs = [p for p in glob.glob(jlib.path(cfg["logs"]["session_log"]["folder"]) + "/S*.md")]
print("===== latest session log")
if logs:
    latest = max(logs, key=os.path.getmtime)
    lines = open(latest, encoding="utf-8").read().splitlines()
    print(os.path.relpath(latest, jlib.ROOT))
    print("\n".join(lines[-int(B.get("session_lines", 40)):]))
else:
    print("(none yet)")
for spec in B.get("tails") or ["Playtest/judge-notes.txt:30"]:
    rel, _, k = str(spec).partition(":")
    p = jlib.path(rel)
    if os.path.exists(p):
        print(f"===== {rel} (the last {k or 30} lines)")
        print("\n".join(open(p, encoding="utf-8").read().splitlines()[-int(k or 30):]))
fm, _ = jlib.read_note(st["campaign_state"])
print("===== status")
print("bootstrap needed" if not (fm.get("public") or {}).get("party") else
      f"session {fm.get('session')}, party of {len(fm['public']['party'])}")
dirty = subprocess.run(["git", "-C", jlib.ROOT, "status", "--short"], capture_output=True, text=True).stdout.strip()
print("uncommitted changes:\n" + dirty if dirty else "working tree clean")
