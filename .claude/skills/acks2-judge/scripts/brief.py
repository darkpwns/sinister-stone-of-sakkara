#!/usr/bin/env python3
"""brief.py [--full] : what the resume step reads, in one print, and no more (C5; it printed a thousand lines):
Campaign State (without its generated `public.party` block, which the handoff's party table repeats; `--full` keeps
it), the handoff (its generated block made fresh from the state files: date, party,
who is left behind, adventure, wages, what the schedule holds due, the standing reminders and the lessons to
escalate, then the Judge's notes), the last rows of the Rulings table, the World State sections the resume names
(config `brief.world_sections`, default: Prep queue, NPC attitudes, and the latest entries of Scheduled events),
the tail of the latest session log and of the playtest's judge notes when the campaign has them (config
`brief.tails`), uncommitted changes, and whether bootstrap is needed. `--full` prints the three state notes whole,
as before.

Config (campaign.yaml, all optional):
  brief: {rulings_rows: 8, world_sections: ["Prep queue", "NPC attitudes", "Scheduled events:12"],
          tails: ["Playtest/judge-notes.txt:8"], session_lines: 40}
Older Rulings rows are found by keyword (`grep -i WORD` the Rulings note), as the skill's ruling order says.
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


def drop_party(text):
    """Campaign State without the generated `public.party` list (the handoff's party table has the same rows) and
    with the `public.trail` list on one line."""
    out, mode, trail = [], None, []
    for ln in text.splitlines():
        if mode and (re.match(r"^  [A-Za-z_]", ln) or re.match(r"^\S", ln)):
            if mode == "trail":
                out.append("  trail: " + ", ".join(trail))
            mode = None
        if mode == "party":
            continue
        if mode == "trail":
            trail.append(ln.strip().lstrip("- ").strip("'\""))
            continue
        if re.match(r"^  party:\s*$", ln):
            mode = "party"
            out.append("  party: (generated from the actors; see the handoff's party table)")
            continue
        if re.match(r"^  trail:\s*$", ln):
            mode, trail = "trail", []
            continue
        out.append(ln)
    return "\n".join(out)


cs = open(jlib.path(st["campaign_state"]), encoding="utf-8").read().strip()
print(f"===== {st['campaign_state']}" + ("" if full else " (public.party omitted: the handoff has it)"))
print(cs if full else drop_party(cs))
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
    n = int(B.get("rulings_rows", 8))
    print(f"===== {st['rulings']} (the last {n} rows of {max(0, len(rows) - 2)}; grep the note by keyword for the rest)")
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
for spec in B.get("tails") or ["Playtest/judge-notes.txt:8"]:
    rel, _, k = str(spec).partition(":")
    p = jlib.path(rel)
    if os.path.exists(p):
        print(f"===== {rel} (the last {k or 8} lines)")
        print("\n".join(open(p, encoding="utf-8").read().splitlines()[-int(k or 8):]))
fm, _ = jlib.read_note(st["campaign_state"])
print("===== status")
print("bootstrap needed" if not (fm.get("public") or {}).get("party") else
      f"session {fm.get('session')}, party of {len(fm['public']['party'])}")
dirty = subprocess.run(["git", "-C", jlib.ROOT, "status", "--short"], capture_output=True, text=True).stdout.strip()
print("uncommitted changes:\n" + dirty if dirty else "working tree clean")
