#!/usr/bin/env python3
"""S13 helper: a fight against a slow fire-only foe by thrown burning oil (RR p. 298), the party giving ground.

Usage: s13_pudding.py ROUNDS  (state already initialised with the party and the foe id 'pudding').
Positions: pos[id] = feet between that member and the foe. A member, at his count: if engaged (pos 0) he
withdraws 10' and does not throw; otherwise he steps back up to 20' (while room is left) and throws a flask if he
has one. The foe, at its count: moves 20' toward the nearest member and attacks him if it reaches him.
Every die is the engine's (`acks.sh roll|save|damage|attack`). Writes the positions to a JSON file between calls.
"""
import json, re, subprocess, sys, os

A = ["bash", ".claude/skills/acks2-judge/scripts/acks.sh"]
POS = "/tmp/claude-0/-home-user/699c6776-71fd-51e7-843b-9b8acce23a3f/scratchpad/pudding_pos.json"
FOE = "pudding"; FOE_LABEL = "the glistening black mass"
# attack throw, DEX mod (missiles), oil holder
THROWERS = {"lucilla": (8, 1), "neris": (9, 1), "vestus-the-unlikely": (9, 1), "brennus": (7, 3),
            "marcellus": (8, 0), "aelia": (8, 0), "phaedra": (9, -1), "varro": (8, 0), "iulia": (8, 1), "vettius": (8, 1)}
ROOM = 85
BLESSED = os.environ.get("BLESSED") == "1"  # Neris' Holy Blessing: +1 to attack throws  # feet of passage and tunnel behind the line before the cave mouth (Judge's call)


def run(*args):
    out = subprocess.run(A + list(args), capture_output=True, text=True).stdout.strip().splitlines()
    return re.sub(r" *\(src[^)]*\)", "", out[-1]) if out else ""


def total(line):
    m = re.search(r"= (-?\d+)\s*$", line) or re.search(r"-> \[(\d+)\]", line)
    return int(m.group(1)) if m else 0


def oil(i):
    o = run("inv", "show", i)
    m = re.search(r"Oil, Military \(1 pint\)(?: ×(\d+))?", o)
    return 0 if not m else int(m.group(1) or 1)


def torches(i):
    o = run("inv", "show", i)
    m = re.search(r"torch(?: ×(\d+))?[,;]?", o)
    return 0 if not m else int(m.group(1) or 1)


def foe_hp():
    o = run("state", "show")
    m = re.search(r"pudding\[foe\] (\w+) hp (-?\d+)/", o)
    return (m.group(1), int(m.group(2))) if m else ("?", 0)


def main(rounds):
    st = json.load(open(POS)) if os.path.exists(POS) else {}
    pos = st.get("pos", {}); room = st.get("room", ROOM); burn = st.get("burn", [])
    for r in range(rounds):
        decl = [x for d in os.environ.get("DECL", "").split(",") if d for x in ("--declare", d + ":spell")]
        print(run("round-start", *decl)[:400])
        moved = set(); newburn = []
        while True:
            o = run("round-next")
            if "all combatants" in o or not o:
                break
            m = re.search(r"count (-?\d+): (.+?) acts", o)
            if not m:
                print("??", o); break
            who = m.group(2)
            if "cannot act" in o:
                print("  ", o); continue
            if "Black" in who or "pudding" in who.lower() or "mass" in who:
                pref = os.environ.get("PREF", "")
                near = min((k for k in pos if pos[k] is not None), key=lambda k: (pos[k], 0 if k == pref else 1))
                gap = pos[near]
                step = min(20, gap)
                for k in pos:
                    if pos[k] is not None:
                        pos[k] = max(0, pos[k] - step)
                if gap <= 20:
                    run("state", "engage", FOE, near)
                    print("  foe flows %d' onto %s:" % (step, near), run("attack", FOE, near))
                else:
                    print("  foe flows 20' after the line")
                continue
            i = {"Vestus the Unlikely": "vestus-the-unlikely"}.get(who, who.split()[0].lower())
            # last round's direct hits burn again at the thrower's count
            for b in [b for b in burn if b == i]:
                print("   still burning (%s's flask):" % i, run("damage", FOE, "--dice", "1d8", "--type", "fire", "--mundane"))
                burn.remove(b)
            if i not in pos or pos[i] is None:
                continue
            fans = os.environ.get("FANS", "").split(",")
            cure = dict(x.split(":") for x in os.environ.get("CURE", "").split(",") if ":" in x)
            if i == os.environ.get("PREF") and pos[i] == 0:
                print("  %s holds and defends:" % i, run("state", "defend", i)); continue
            if i in cure:
                print("  %s cures %s:" % (i, cure[i]), run("roll", "%s Cure Light Injury on %s:1d6+1" % (i, cure[i]))); continue
            if i in os.environ.get("SPARKS", "").split(",") and pos[i] <= 45:
                sv = run("save", FOE, "blast")
                dm = run("damage", FOE, "--dice", "1d6", "--type", "fire", "--extraordinary", *(["--half"] if "SUCCESS" in sv else []))
                print("  %s casts Burning Sparks on the burning oil:" % i, sv, dm); continue
            if i in fans and pos[i] <= 40:
                sv = run("save", FOE, "blast")
                dm = run("damage", FOE, "--dice", "1d8", "--type", "fire", "--extraordinary", *(["--half"] if "SUCCESS" in sv else []))
                print("  %s casts Fan of Flames:" % i, sv, dm); fans.remove(i); continue
            if pos[i] == 0:
                pos[i] = 10; run("state", "disengage", i, FOE); print("  %s withdraws 10'" % i); continue
            back = min(20, room) if (i not in moved and os.environ.get('HOLD') != '1') else 0
            if back and len(moved) == 0:
                room -= back
            if back:
                for k in pos:
                    if pos[k] not in (None, 0) and k not in moved:
                        pos[k] += back
                moved |= set(k for k in pos if pos[k] is not None)
            if i not in THROWERS or (oil(i) == 0 and torches(i) == 0):
                print("  %s gives ground (no flask)" % i); continue
            if oil(i) == 0:
                at, dex = THROWERS[i]; d = pos[i]; pen = 0 if d <= 15 else (2 if d <= 45 else 5)
                if d > 60:
                    print("  %s: out of range" % i); continue
                bl = 1 if BLESSED else 0; hit = at + 5 + pen - dex - bl; spl = at + pen - dex - bl
                ro = run("roll", "%s throws a lit torch at %s (%d', hit %d+, splash %d+):1d20" % (i.capitalize(), FOE_LABEL, d, hit, spl))
                run("inv", "remove", i, "torch", "1", "--why", "used", "--cause", "lit and thrown at the black mass, day 288")
                n = total(ro)
                if n >= hit:
                    print("  ", ro, "| HIT:", run("damage", FOE, "--dice", "1d4", "--type", "fire", "--mundane"))
                elif n >= spl:
                    print("  ", ro, "| splash:", run("damage", FOE, "--dice", "1d1", "--type", "fire", "--mundane"))
                else:
                    print("  ", ro, "| miss")
                s_, hp_ = foe_hp()
                if s_ == "destroyed" or hp_ <= 0:
                    print("FOE DOWN"); break
                continue
            at, dex = THROWERS[i]
            d = pos[i]; pen = 0 if d <= 15 else (2 if d <= 45 else 5)
            if d > 60:
                print("  %s: out of range" % i); continue
            bl = 1 if BLESSED else 0
            hit = at + 5 + pen - dex - bl; spl = at + pen - dex - bl
            ro = run("roll", "%s throws burning oil at %s (%d', hit %d+, splash %d+):1d20" % (i.capitalize(), FOE_LABEL, d, hit, spl))
            run("inv", "remove", i, "oil, military (1 pint)", "1", "--why", "used", "--cause", "thrown burning at the black mass, day 288")
            n = total(ro); nat = int(re.search(r"\[(\d+)\]", ro).group(1)) if re.search(r"\[(\d+)\]", ro) else n
            if nat == 1:
                print("  ", ro, "| FUMBLE:", run("damage", i, "--dice", "1d8", "--type", "fire", "--mundane")); continue
            if n >= hit:
                print("  ", ro, "| HIT:", run("damage", FOE, "--dice", "1d8", "--type", "fire", "--mundane")); newburn.append(i)
            elif n >= spl:
                sv = run("save", FOE, "blast")
                print("  ", ro, "| splash:", sv if "SUCCESS" in sv else sv + " " + run("damage", FOE, "--dice", "1d3", "--type", "fire", "--mundane"))
            else:
                sc = run("roll", "scatter of %s's flask (1d12 clock, 6 = back at the line; %s):1d12" % (i, "1d10'" if pen == 0 else "2d10'"))
                print("  ", ro, "| miss, scatter", total(sc))
            s, hp = foe_hp()
            if s == "destroyed" or hp <= 0:
                print("FOE DOWN", s, hp); burn = []; break
        burn = newburn + burn
        print(run("round-end"))
        s, hp = foe_hp()
        json.dump({"pos": pos, "room": room, "burn": burn}, open(POS, "w"))
        print("== positions", pos, "room left", room, "| oil", {k: oil(k) for k in THROWERS if k in pos})
        if s == "destroyed" or hp <= 0:
            break
        if any("unconscious" in run("state", "show") for _ in [0]):
            print("SOMEONE DOWN"); break


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
