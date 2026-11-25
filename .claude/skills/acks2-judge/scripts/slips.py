#!/usr/bin/env python3
"""slips.py : the slip catcher (engine 7.25.0 proposals, C11). jacks.run calls `catch` after every command: a known slip
pattern seen in the command's result or the states is recorded in Campaign/slips.jsonl (`lesson slip`), so lessons
escalate without the Judge remembering to record them. Read-only otherwise; never fails a command.

Patterns (lesson id, category when no lesson exists yet):
  nonlethal-capture             `state end` with a foe knocked out by nonlethal damage and not yet captured
  water-at-known-source         `camp` or `travel` that found the skins under a day beside a known source
  training-pause                `travel` with a training course running whose trainer is in the party
  note-penalty-before-reaction  `reaction` rolled while a surprise note penalty was still on offer

`slips.py test` lists the patterns.
"""
import json
import os

PATTERNS = {
    "nonlethal-capture": "combat-procedure",
    "water-at-known-source": "overland-routine",
    "training-pause": "town-routine",
    "note-penalty-before-reaction": "encounter-procedure",
}


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def found(ctx, cmd, args, code, out):
    """[(lesson id, note)] the command shows."""
    hits = []
    xs = None

    def X():
        nonlocal xs
        if xs is None:
            xs = _load(ctx["xstate"])
        return xs
    if cmd == "state" and args[:1] == ["end"] and "knocked out by nonlethal damage alone" in out:
        hits.append(("nonlethal-capture", "state end with a foe knocked out by nonlethal damage, not captured "
                                          "(the engine refused)"))
    if cmd in ("camp", "travel", "forced-march") and "carried less than a day's water beside" in out:
        hits.append(("water-at-known-source", f"{cmd} beside a known source with skins under a day (the engine "
                                              "filled them)"))
    if cmd in ("travel", "forced-march") and code == 0 and os.path.exists(ctx.get("tstate") or ""):
        ts = _load(ctx["tstate"])
        party = set((X().get("party") or {}))
        running = [co for co in (ts.get("courses") or {}).values() if co.get("status") == "active"
                   and co.get("trainer") in party and not any(p.get("to") is None for p in co.get("paused") or [])]
        if running:
            hits.append(("training-pause", "travel with training running: " + ", ".join(
                f"{co.get('id')} ({co.get('trainer')})" for co in running) + " (`train pause`)"))
    if cmd == "reaction" and code == 0:
        sv = ((X().get("encounter") or {}).get("surprise") or {})
        if sv.get("note_penalty"):
            hits.append(("note-penalty-before-reaction", "reaction rolled with the note's surprise penalty still on "
                                                         "offer (`encounter surprise --apply-note-penalty`)"))
    return hits


def catch(ctx, argv, code, out, run):
    """Record each slip once per lesson, session and day (run: jacks.run, for `lesson slip`)."""
    if not argv or argv[0] in ("lesson", "batch") or not ctx.get("lessons"):
        return []
    try:
        hits = found(ctx, argv[0], list(argv[1:]), code, out)
    except Exception:          # noqa: BLE001 - the catcher never fails a command
        return []
    if not hits:
        return []
    day = (_load(ctx["xstate"]).get("clock") or {}).get("day")
    sp = os.path.join(os.path.dirname(ctx["lessons"]), "slips.jsonl")
    have = set()
    if os.path.exists(sp):
        with open(sp, encoding="utf-8") as f:
            for ln in f:
                try:
                    r = json.loads(ln)
                except ValueError:
                    continue
                have.add((r.get("lesson"), str(r.get("session")), r.get("day")))
    said = []
    for lid, note in hits:
        if (lid, str(ctx.get("session")), day) in have:
            continue
        a = ["lesson", "slip", lid, "--note", f"(caught) {note}"] + (["--day", str(day)] if day is not None else [])
        c, o = run(a + ["--category", PATTERNS[lid]], ctx) if lid not in _known(ctx) else run(a, ctx)
        if c == 0:
            said.append(f"SLIP recorded [{lid}]: {note}")
    return said


def _known(ctx):
    try:
        import yaml
        with open(ctx["lessons"], encoding="utf-8") as f:
            return {x.get("id") for x in (yaml.safe_load(f) or {}).get("lessons") or []}
    except Exception:          # noqa: BLE001
        return set()


if __name__ == "__main__":
    print(__doc__)
