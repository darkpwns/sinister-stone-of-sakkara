"""S45: one member's melee with cleaves along a list of foes (engages each in turn; stops when no cleave is offered,
the list ends, or an attack is refused). usage: s45_cleave.py ATTACKER id1 id2 ... [-- extra attack args]"""
import sys, re
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
a = sys.argv[1]; rest = sys.argv[2:]
extra = rest[rest.index("--") + 1:] if "--" in rest else []
ids = rest[:rest.index("--")] if "--" in rest else rest
first = True
for t in ids:
    jacks.run(["state", "engage", a, t])
    code, o = jacks.run(["attack", a, t] + ([] if first else ["--cleave"]) + extra)
    last = re.sub(r" \(src: [^)]*\)", "", o.strip().splitlines()[-1] if o.strip() else "")
    m = re.search(r"-> (\d+) = (\d+) vs (\d+)\+ (HIT|miss)", last); hp = re.search(r"hp (-?\d+) -> (-?\d+)", last)
    print(f"  {a} -> {t}: {m.group(0) if m else last[:120]}{' hp ' + hp.group(2) if hp else ''}")
    if code != 0: break
    first = False
    if "may cleave" not in last: break
