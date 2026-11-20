#!/usr/bin/env python3
"""FALLBACK ONLY (rules engine unavailable). Wilderness encounters are the engine's (stage 4: `acks.sh travel`,
`search`, `hunt`, `camp`, `encounter start --wild`); this script keeps only the dungeon check.
   encounter.py dungeon LEVEL [--place]                    : one wandering-monster check (all rolls hidden);
                                                            --place skips the 1d6 check (stocking a "monster" room)
Procedure: Judge's Screen §4 and JJ "Running Dungeon Delves" (Wandering Monsters by Level), read from the rules
vault clone.
Prints what happened; the Judge still rolls lair %, surprise, evasion and reaction separately."""
import math, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import jlib

cfg = jlib.config()
VAULT = os.environ.get("RL_VAULT") or os.path.join(cfg["rules"]["clone_dir"], "vault")
DICE = os.path.join(os.path.dirname(__file__), "dice.py")


def roll(label, spec):
    out = subprocess.run([sys.executable, DICE, "--hidden", f"{label}:{spec}"], capture_output=True, text=True).stdout
    return int(out.strip().split("= ")[-1])


def rng(cell, v):
    for part in cell.replace("–", "-").split("/"):
        m = re.match(r"^\s*(\d+)\s*(?:-\s*(\d+))?\s*$", part)
        if m and int(m.group(1)) <= v <= int(m.group(2) or m.group(1)):
            return True
    return False


def vault_table(note, heading_hint=None):
    hits = [os.path.join(d, f) for d, _, fs in os.walk(VAULT) for f in fs if f == note + ".md"]
    if len(hits) != 1:
        jlib.die(f"rules vault note not found (once): {note}")
    text = open(hits[0], encoding="utf-8").read()
    if heading_hint:
        i = text.find(heading_hint)
        text = text[i:] if i >= 0 else ""
    block = []
    for ln in text.splitlines():
        if ln.startswith("|"):
            block.append(ln)
        elif block:
            break
    return jlib.table_rows(block)


def clean(cell):
    return re.sub(r"\[\[([^|\]]+)(?:\\?\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), cell)


ML = {1: [(1, 9, 1), (10, 11, 2), (12, 12, 3)], 2: [(1, 3, 1), (4, 9, 2), (10, 11, 3), (12, 12, 4)],
      3: [(1, 1, 1), (2, 3, 2), (4, 9, 3), (10, 11, 4), (12, 12, 5)], 4: [(1, 1, 2), (2, 3, 3), (4, 9, 4), (10, 11, 5), (12, 12, 6)],
      5: [(1, 1, 3), (2, 3, 4), (4, 9, 5), (10, 12, 6)], 6: [(1, 1, 4), (2, 3, 5), (4, 12, 6)]}


def pick(table, v):
    return next(r for lo, hi, r in table if lo <= v <= hi)


a = sys.argv[1:]
if len(a) < 2:
    print(__doc__); sys.exit(1)
if a[0] == "dungeon":
    lvl = int(a[1]); w = 6 if "--place" in a else roll("Wandering check", "1d6")
    print(f"wandering 1d6 = {w} -> {'ENCOUNTER' if w >= 6 else 'none'}")
    if w >= 6:
        minute = roll("Minute of turn", "1d10")
        m = pick(ML[min(lvl, 6)], roll("Monster level", "1d12"))
        e = roll(f"ML{m} table", "1d12")
        rows = vault_table("Running Dungeon Delves", f"Monster Level {m}**")
        cell = clean(next(x for x in rows if rng(x["1d12"], e))[f"Monster Level {m}"])
        factor = 1.5 ** max(0, lvl - m) * 0.5 ** max(0, m - lvl)
        dm = re.search(r"\(([\dd+]+)\)\s*$", cell)
        num = None
        if dm:
            num = roll("Number appearing", dm.group(1).replace(" ", ""))
            num = max(1, math.ceil(num * factor))
        dist = roll("Encounter distance", "2d6") * 10
        print(f"minute {minute}; monster level {m}; 1d12 = {e}: {cell}; number {num} (x{factor:g}); distance {dist}' (reduce to light/sight)")
        print(f"reaction modifier {m - lvl:+d} (Monster Level - Dungeon Level)")
else:
    print(__doc__); sys.exit(1)
