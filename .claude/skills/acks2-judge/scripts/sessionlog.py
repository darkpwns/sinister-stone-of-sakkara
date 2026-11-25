#!/usr/bin/env python3
"""sessionlog.py : the session log composer and the state notes' front-matter check (7.25.0 proposals, C7).

  sessionlog.py fm [FILE ...]
      Every state note's front matter (Campaign/*.md, the session logs, Party notes; or the files given) must parse as
      YAML; exit 3 naming each that does not (S16: an unquoted colon in Campaign State broke dice.py). save.sh runs it.
  sessionlog.py draft [--session N] [--out FILE]
      A draft of "Where they went / Who they met / Treasure and XP" from the exploration state's events and location
      changes, the encounters (as the party perceived them), the session's payouts and levels; and the Judge block
      from the session's hidden rolls and the judge-notes lines of the session. Written to --out (default
      Campaign/session-draft.md, Judge only) for the Judge to edit into the session note: nothing is guessed.
"""
import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jlib  # noqa: E402

FM = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


def fm_files(cfg):
    log = ((cfg.get("logs") or {}).get("session_log") or {}).get("folder") or "Session Log/"
    out = glob.glob(jlib.path("Campaign") + "/*.md") + glob.glob(jlib.path(log) + "*.md") + \
        glob.glob(jlib.path("Party") + "/**/*.md", recursive=True)
    return sorted(out)


def fm_check(files):
    import yaml
    bad = []
    for p in files:
        try:
            text = open(p, encoding="utf-8").read()
        except OSError:
            continue
        m = FM.match(text)
        if not m:
            continue
        try:
            v = yaml.safe_load(m.group(1))
            if v is not None and not isinstance(v, dict):
                bad.append((p, "front matter is not a mapping"))
        except yaml.YAMLError as e:
            mark = getattr(e, "problem_mark", None)
            bad.append((p, f"{getattr(e, 'problem', e)}" + (f" (line {mark.line + 2})" if mark else "")))
    return bad


def draft(a):
    cfg = jlib.config()
    st = cfg["paths"]["state"]
    fm, _ = jlib.read_note(st["campaign_state"])
    sess = a.session or fm.get("session")
    t = cfg.get("tools") or {}
    xs = json.load(open(jlib.path(t.get("exploration_state", "Campaign/exploration-state.json")), encoding="utf-8"))
    rolls = []
    if os.path.exists(jlib.path(st["roll_log"])):
        for ln in open(jlib.path(st["roll_log"]), encoding="utf-8"):
            try:
                r = json.loads(ln)
            except ValueError:
                continue
            if str(r.get("session")) == str(sess):
                rolls.append(r)
    out = [f"# Draft: session {sess} (sessionlog.py; Judge only until edited)", ""]
    dl = xs.get("day_log") or {}
    first = int(a.from_day) if a.from_day else (min(int(k) for k in dl) if dl else 0)
    out += ["## Where they went"]
    tdays = ((xs.get("travel") or {}).get("days") or {})
    for k in sorted(set(dl) | set(tdays), key=int):
        if int(k) < first:
            continue
        rec = dl.get(k) or {}
        mem = list((tdays.get(k) or {}).values())
        trav = max((float(m.get("travel_hours") or 0) for m in mem), default=0)
        town = any(m.get("in_settlement") for m in mem)
        bits = []
        if trav:
            bits.append(f"{trav:g} h on the road")
        if rec.get("delve_rounds"):
            bits.append(f"{int(rec['delve_rounds']) // 10} turns delving")
        if town and not trav and not rec.get("delve_rounds"):
            bits.append("in town")
        out.append(f"- Day {k}: " + (", ".join(bits) or "rest"))
    trail = ((xs.get("travel") or {}).get("trail") or [])[-12:]
    if trail:
        out.append(f"- Hexes (last of the trail): {' '.join(trail)}")
    out += ["", "## Who they met"]
    enc = [e for e in (xs.get("past_encounters") or []) + ([xs["encounter"]] if xs.get("encounter") else [])]
    dayof = lambda e: int((re.search(r"day (\d+)", str(e.get("at"))) or [0, 0])[1])
    for e in [e for e in enc if dayof(e) >= first][-40:]:
        who = e.get("perceived") or e.get("monster_name") or e.get("entry")
        out.append(f"- {e.get('at')}: {who} x{e.get('number')}" + (f" ({e.get('reaction')})" if e.get("reaction") else "")
                   + (f"; {e.get('status')}" if e.get("status") else "") + "  <- name as the party knows it")
    out += ["", "## Treasure and XP"]
    ap = jlib.path(t.get("adventure_state", "Campaign/adventure-state.json"))
    if os.path.exists(ap):
        ad = json.load(open(ap, encoding="utf-8"))
        for x in [ad.get("adventure")] + list(ad.get("closed") or []):
            if x and str(x.get("session") or "") in (str(sess), f"S{sess}") or (x and x.get("status") == "paid"
                                                                               and x is ad.get("adventure")):
                out.append(f"- {x.get('id')} {x.get('name')}: {x.get('status')}"
                           + (f", XP {x.get('xp_total')}" if x.get("xp_total") else ""))
    lv = [r for r in rolls if re.search(r"level|hit points|hp roll", str(r.get("label")), re.I)]
    out += [f"- level roll: {r.get('label')} {r.get('total')}" for r in lv[:20]]
    out += ["", f"{(cfg.get('logs') or {}).get('session_log', {}).get('judge_block') or '> [!judge]- Judge rolls'}"]
    for r in [r for r in rolls if r.get("vis") == "hidden"]:
        out.append(f"> - {r.get('label')}: {r.get('spec')} -> {r.get('rolls')} = {r.get('total')}")
    jn = jlib.path("Playtest/judge-notes.txt")
    if os.path.exists(jn):
        pat = re.compile(rf"\bS{sess}\b")
        notes = [ln.strip() for ln in open(jn, encoding="utf-8") if pat.search(ln[:40])]
        if notes:
            out += [">", "> Judge notes:"] + [f"> - {n[:400]}" for n in notes]
    dst = jlib.path(a.out or "Campaign/session-draft.md")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"draft written: {os.path.relpath(dst, jlib.ROOT)} ({len(rolls)} roll(s) of session {sess})")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fm")
    p.add_argument("files", nargs="*")
    p = sub.add_parser("draft")
    p.add_argument("--session")
    p.add_argument("--from-day", help="the session's first game day (default: the first day the exploration state "
                                      "still keeps)")
    p.add_argument("--out")
    a = ap.parse_args(argv)
    if a.cmd == "fm":
        bad = fm_check([jlib.path(f) for f in a.files] if a.files else fm_files(jlib.config()))
        for p_, why in bad:
            print(f"FRONT MATTER: {os.path.relpath(p_, jlib.ROOT)}: {why}")
        return 3 if bad else 0
    return draft(a)


if __name__ == "__main__":
    sys.exit(main())
