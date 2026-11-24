"""S45: an area spell on many foes in the fight: one damage roll (open, the caster's), each target's save (hidden),
full or half by `damage --dice Nd1`. usage: s45_area.py CASTER "LABEL:DICE" TYPE SAVE id1 id2 ... (SAVE: blast|none)"""
import re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
caster, rolllab, typ, save, *ids = sys.argv[1:]
code, out = jacks.run(["roll", rolllab]); print(out.strip().splitlines()[-1][:120])
total = int(re.search(r"= (-?\d+)\s*$", out.strip().splitlines()[-1]).group(1))
dead = 0
for t in ids:
    half = False
    if save != "none":
        c, o = jacks.run(["save", t, save]); half = "SUCCESS" in o
    amt = total // 2 if half else total
    if amt <= 0: continue
    c, o = jacks.run(["damage", t, "--dice", f"{amt}d1", "--type", typ, "--extraordinary", "--attacker", caster] + (["--half"] if False else []))
    last = o.strip().splitlines()[-1]
    m = re.search(r"hp (-?\d+) -> (-?\d+)", last)
    if m and int(m.group(2)) <= 0: dead += 1
    print(f"  {t}: {'save, ' if half else ''}{amt} -> {m.group(2) if m else '?'}")
print(f"down: {dead} of {len(ids)}")
