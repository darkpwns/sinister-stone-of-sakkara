#!/usr/bin/env python3
"""leak.py : the leak check on player-facing writes (7.25.0 proposals, C8), run by save.sh once per save.

The player-facing files changed since the last commit (campaign.yaml secrecy.player_facing: the party notes and the
players' memory notes; Judge blocks and Judge-only callouts left out) are scanned for: Judge-only markers and
Judge-only note titles (as party.py's wall); the true name of any treasure lot the players have not identified (an
unrevealed property: 'sword +1' before its bonus is known); and, with --verbatim, any 8-word run shared with
Judge-only text and found in no other player-facing text (slow, and noisy where Judge notes repeat what the players
were told). Exit 0 clean, 3 with the hits listed (save.sh refuses; LEAK_OK=1 saves anyway, for a hit the Judge has
checked).

  leak.py [--all] [--verbatim] [FILE ...]
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jlib  # noqa: E402


def changed(cfg):
    """Player-facing .md files changed or new since HEAD (repo-relative)."""
    try:
        out = subprocess.run(["git", "-C", jlib.ROOT, "status", "--porcelain", "-z"], capture_output=True,
                             text=True).stdout
    except OSError:
        return []
    files = []
    for ent in out.split("\0"):
        if len(ent) > 3:
            files.append(ent[3:])
    return [f for f in files if f.endswith(".md") and facing(cfg, f)]


def facing(cfg, rel):
    sec = cfg.get("secrecy") or {}
    pf = list(sec.get("player_facing") or [])
    return any(rel == p or (p.endswith("/") and rel.startswith(p)) for p in pf)


def strip_judge(cfg, text):
    """The text without Judge blocks and Judge-only callouts (they may name anything)."""
    starts = [((cfg.get("logs") or {}).get("session_log") or {}).get("judge_block") or "> [!judge]",
              (cfg.get("secrecy") or {}).get("judge_only_callout") or "> [!danger]", "> [!judge]"]
    out, on = [], False
    for ln in text.splitlines():
        s = ln.strip()
        if any(s.startswith(x) for x in starts if x):
            on = True
            continue
        if on and s.startswith(">"):
            continue
        on = False
        out.append(ln)
    return "\n".join(out)


def lot_secrets(cfg):
    p = jlib.path(((cfg.get("tools") or {}).get("adventure_state")) or "Campaign/adventure-state.json")
    out = []
    if not os.path.exists(p):
        return out
    try:
        a = json.load(open(p, encoding="utf-8"))
    except ValueError:
        return out
    for lid, l in (a.get("lots") or {}).items():
        tn = str(((l.get("true") or {}).get("name")) or "").strip()
        pn = str(((l.get("player") or {}).get("desc")) or "").strip()
        if tn and not l.get("identified") and tn.lower() != pn.lower() and tn.lower() not in pn.lower() \
                and l.get("status") not in ("spent", "sold"):
            out.append((tn, lid))
    return out


def check(cfg, files, fast=True):
    import party as P
    hits = []
    lots = lot_secrets(cfg)
    sec = cfg.get("secrecy") or {}
    banned = []
    for folder in sec.get("judge_only_folders") or []:
        if folder.startswith("Campaign"):
            continue
        banned += [os.path.basename(p)[:-3] for p in glob.glob(jlib.path(folder) + "/*.md")]
    banned = [b for b in banned if b not in sec.get("revealed", []) and len(b) > 3]
    banned += [sec.get("judge_only_tag") or "", "[!danger]", "Judge only", "[H] "]
    jc = None
    for rel in files:
        p = jlib.path(rel)
        if not os.path.exists(p):
            continue
        text = strip_judge(cfg, jlib.FM.sub("", open(p, encoding="utf-8").read(), count=1))
        low = text.lower()
        for b in banned:
            if b and b.lower() in low:
                hits.append(f"{rel}: Judge-only marker or title {b!r}")
        for tn, lid in lots:
            if re.search(r"(?<![\w+])" + re.escape(tn.lower()) + r"(?![\w+])", low):
                hits.append(f"{rel}: names {tn!r} (lot {lid}, not identified by the players)")
        if not fast:
            if jc is None:
                jc = P.shingles(P.judge_corpus(cfg))
            others = []
            for f in sec.get("player_facing") or []:
                for g in ([jlib.path(f)] if f.endswith(".md") else glob.glob(jlib.path(f) + "**/*.md", recursive=True)):
                    if os.path.abspath(g) != os.path.abspath(p) and os.path.exists(g):
                        others.append(open(g, encoding="utf-8").read())
            common = (P.shingles(text) & jc) - P.shingles("\n".join(others))
            hits += [f"{rel}: verbatim Judge-only text \"{s}\"" for s in sorted(common)[:3]]
    return hits


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true", help="every player-facing file, not only the changed ones")
    ap.add_argument("--verbatim", action="store_true", help="also the 8-word verbatim scan against Judge-only text")
    a = ap.parse_args(argv)
    cfg = jlib.config()
    files = a.files
    if not files:
        if a.all:
            pf = list((cfg.get("secrecy") or {}).get("player_facing") or [])
            files = [os.path.relpath(g, jlib.ROOT) for f in pf
                     for g in ([jlib.path(f)] if f.endswith(".md") else glob.glob(jlib.path(f) + "**/*.md",
                                                                                     recursive=True))]
        else:
            files = changed(cfg)
    if not files:
        return 0
    hits = check(cfg, files, not a.verbatim)
    for h in hits:
        print("LEAK? " + h)
    return 3 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
