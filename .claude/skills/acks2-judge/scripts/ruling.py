#!/usr/bin/env python3
"""ruling.py : terms before the roll (7.25.0 proposals, C5).

  ruling.py search WORDS...
      The Rulings rows that share the most words with WORDS (precedents first, newest last).
  ruling.py make --question "Q" --terms "T" [--roll 1d6] [--label L] [--source S] [--new]
      Searches the Rulings first: when a row shares most of the question's words it is shown and nothing is written
      (rule by it, or --new for a new ruling). Otherwise the row is appended to Campaign/Rulings.md (today, the
      Campaign State session) and, with --roll, the dice are rolled hidden through the engine with a label citing the
      ruling ("Rulings <session> <question>: ..."), so the terms stand before the result.
"""
import argparse
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jlib  # noqa: E402

STOP = set("a an the of to in on at by for and or is are was were be it its his her their with as from that this "
           "what which who when does do can may".split())
RULINGS = "Campaign/Rulings.md"


def words(text):
    return {w for w in re.findall(r"[a-z0-9']+", str(text).lower()) if w not in STOP and len(w) > 2}


def rows(path=RULINGS):
    out = []
    p = jlib.path(path)
    if not os.path.exists(p):
        return out
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("| ") and not ln.startswith(("| Date", "| ---")):
            cells = [c.strip() for c in ln.strip().strip("|").split(" | ")]
            if len(cells) >= 4:
                out.append(cells)
    return out


def search(text, n=5):
    want = words(text)
    scored = []
    for i, r in enumerate(rows()):
        w = words(r[2] + " " + r[3])
        k = len(want & w)
        if k:
            scored.append((k / max(1, len(want)), i, r))
    scored.sort(key=lambda x: (-x[0], -x[1]))
    return scored[:n]


def session():
    """'R2 S16' in a campaign whose lessons file names a run beyond the first (the Rulings rows' form), else 'S16'."""
    cfg = jlib.config()
    fm, _ = jlib.read_note(cfg["paths"]["state"]["campaign_state"])
    s = str(fm.get("session"))
    run = fm.get("run")
    if run is None:
        lp = jlib.path((cfg.get("tools") or {}).get("lessons", "Campaign/lessons.yaml"))
        if os.path.exists(lp):
            m = re.search(r"^run:\s*(\d+)", open(lp, encoding="utf-8").read(), re.M)
            run = int(m.group(1)) if m else None
    if s.isdigit():
        return f"R{run} S{s}" if run and int(run) > 1 else f"S{s}"
    return s


def make(a):
    hits = search(a.question)
    strong = [h for h in hits if h[0] >= 0.5]
    if strong and not a.new:
        print("precedent(s) found: rule by them, or --new for a new ruling")
        for sc, _i, r in strong:
            print(f"  {r[1]} ({sc:.0%}): {r[2][:160]} -> {r[3][:200]}")
        return 3
    sess = a.session or session()
    row = (f"| {datetime.date.today().isoformat()} | {sess} | {a.question} | {a.terms} | "
           f"{a.source or 'Judge’s ruling (terms set before the roll)'} |\n")
    with open(jlib.path(RULINGS), "a", encoding="utf-8") as f:
        f.write(row)
    print(f"Rulings: {row.strip()}")
    if a.roll:
        import jacks
        label = f"Rulings {sess}: {a.label or a.question[:80]}"
        code, out = jacks.run(["roll", f"{label}:{a.roll}", "--hidden"])
        sys.stdout.write(out)
        return code
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search")
    p.add_argument("words", nargs="+")
    p = sub.add_parser("make")
    p.add_argument("--question", required=True)
    p.add_argument("--terms", required=True)
    p.add_argument("--roll")
    p.add_argument("--label")
    p.add_argument("--source")
    p.add_argument("--session")
    p.add_argument("--new", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "search":
        for sc, _i, r in search(" ".join(a.words)):
            print(f"{r[1]} ({sc:.0%}): {r[2][:160]} -> {r[3][:200]}")
        return 0
    return make(a)


if __name__ == "__main__":
    sys.exit(main())
