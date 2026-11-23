#!/usr/bin/env python3
"""handoff.py [--notes TEXT | --notes-file FILE] [--print] : the one current-state handoff file.

The handoff is a single file (config `logs.handoff`, default Campaign/handoff.md), rewritten each session, never
appended to. Its first block is GENERATED from the state files through the engine (so no number is copied forward
by hand): session, date and place, the party with level, XP, hp and conditions, the open adventure, encounter and
fight, wages with the engine's due days, what the schedule holds due and next, the standing reminders of the lessons
index whose conditions hold now, and the lessons to escalate. Its second block is the Judge's: what was in hand and
what comes next, replaced with --notes / --notes-file (kept as it is otherwise).
`--print` prints the file's text without writing it (brief.py uses it). Judge only: the file is in Campaign/."""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jacks  # noqa: E402
import jlib  # noqa: E402

START, END = "<!-- generated:start -->", "<!-- generated:end -->"
SRC = re.compile(r" *\(src:[^)]*(?:\([^)]*\)[^)]*)*\)")


def line(ctx, *argv, n=1200):
    code, out = jacks.run(list(argv), ctx)
    out = SRC.sub("", (out.strip().splitlines() or [""])[-1])
    return code, out[:n]


def generated():
    ctx = jacks.context()
    cfg = ctx["cfg"]
    out = []
    xs = {}
    if os.path.exists(ctx["xstate"]):
        with open(ctx["xstate"], encoding="utf-8") as f:
            xs = json.load(f)
    ck, loc = xs.get("clock") or {}, xs.get("location") or {}
    r = ck.get("round_of_day", 0)
    out.append(f"- **Session** {ctx['session']} · **day {ck.get('day', '?')}**, {r // 60:02d}:{r % 60:02d} · "
               f"**{loc.get('site') or 'no location'}** ({loc.get('kind') or '-'}"
               + (f", level {loc['level']}" if loc.get("level") else "") + ")")
    ids = list(xs.get("party") or {})
    try:
        views = jlib.actor_views(ids, player=False,
                                 fields=["name", "class", "level", "xp", "hp_max"]) if ids else {}
    except Exception as e:                       # the handoff never fails for want of one view
        views, _ = {}, out.append(f"- party views unavailable: {e}")
    rows = []
    for i in ids:
        v = views.get(i) or {}
        try:
            a = jlib.load_actor(next(p for d in jlib.actor_dirs(cfg) for p in [os.path.join(d, i + ".json")] if os.path.exists(p)))
        except StopIteration:
            a = {}
        st = a.get("state") or {}
        conds = "; ".join(str(c if isinstance(c, str) else c.get("name")) for c in st.get("conditions") or [])
        rows.append(f"| {v.get('name', i)} | {v.get('class', '')} {v.get('level', '')} | {v.get('xp', '')} | "
                    f"{st.get('hp', '?')}/{v.get('hp_max', '?')} | {conds[:160]} |")
    if rows:
        out += ["", "| Party | Class | XP | hp | Conditions |", "| --- | --- | --- | --- | --- |", *rows, ""]
    for label, argv in (("Adventure", ["adventure", "show"]), ("Wages", ["wages", "show"])):
        code, t = line(ctx, *argv, n=700)
        out.append(f"- **{label}:** {t.replace('[H] ', '')}")
    enc = xs.get("encounter")
    if enc and not enc.get("closed"):
        out.append(f"- **Encounter open:** {enc.get('id')} ({enc.get('status')}): end or resolve it before a new one")
    if os.path.exists(ctx["state"]):
        code, t = line(ctx, "state", "show", n=500)
        out.append(f"- **Fight in the combat state:** {t}")
    if ctx["schedule"]:
        code, t = line(ctx, "schedule", "due", "--ahead", "8", n=900)
        out.append(f"- **Schedule:** {t}")
    if ctx["lessons"]:
        code, t = line(ctx, "lesson", "brief", n=3000)
        body, _, esc = t.partition(" | JUDGE: ")
        out.append("- **Standing reminders (lessons whose conditions hold now):**")
        out += [f"  - {x}" for x in body.split("; [") and re.split(r"; (?=\[)", body)]
        if esc:
            out.append("- **Lessons to escalate (slipped on again):**")
            out += [f"  - {x}" for x in esc.split(" / ")]
    return "\n".join(out)


def path(cfg):
    return jlib.path(((cfg.get("logs") or {}).get("handoff")) or "Campaign/handoff.md")


def compose(cfg, notes=None):
    p = path(cfg)
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    m = re.search(r"## Judge's notes for the next session\n(.*)\Z", old, re.S)
    judge = notes if notes is not None else (m.group(1).strip() if m else
                                             "(nothing yet: `handoff.py --notes-file FILE` at session end)")
    return ("# Handoff (current state)\n\nOne file, rewritten each session by `handoff.py`; never appended to. The "
            "first block is generated from the state files; the second is the Judge's.\n\n"
            f"{START}\n{generated()}\n{END}\n\n## Judge's notes for the next session\n{judge.strip()}\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--notes")
    ap.add_argument("--notes-file")
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    cfg = jlib.config()
    notes = a.notes
    if a.notes_file:
        notes = open(a.notes_file, encoding="utf-8").read()
    text = compose(cfg, notes)
    if a.print:
        print(text)
        return 0
    with open(path(cfg), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"handoff written: {os.path.relpath(path(cfg), jlib.ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
