#!/usr/bin/env python3
"""S29 melee driver: runs ONE combat round from the current point of the combat state (round already started).
Party: melee fighters attack an engaged foe, else close on the nearest foe within 40' and attack it (cleaves taken on
foes in reach); Cotta shoots the nearest unengaged foe; casters named in FAN cast Fan of Flames at their initiative on
every foe within 40' (one 1d8, Blast save each; declared at round-start by the caller); everyone else holds.
Foes: close on a random fighter (charge when the distance allows: running speed), engage, attack with every attack of
their routine. Stops (exit 3) when a party member falls; the caller runs round-end and the next round-start.
Usage: s29_melee.py "fan:phaedra,vestus-the-unlikely" (empty for none)"""
import json, os, random, re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
ST = "Campaign/combat-state.json"
FIGHT = ["brennus", "varro", "hrodvar", "marcellus", "iulia", "lucilla", "vettius", "aelia"]
SHOOT = ["cotta"]
FAN = [x for x in (sys.argv[1].split(":", 1)[1].split(",") if len(sys.argv) > 1 and ":" in sys.argv[1] else []) if x]


def run(*a):
    code, out = jacks.run(list(a))
    line = out.strip().splitlines()[-1] if out.strip() else ""
    print("  $", " ".join(a), "->", re.sub(r" \(src: .*", "", line)[:260])
    return code, out


def cs():
    c = json.load(open(ST))
    cb = c["combatants"]
    return c, (cb if isinstance(cb, dict) else {x["id"]: x for x in cb})


def active(x):
    return x.get("status", "active") == "active" and x["hp"] > 0


def dist(c, a, b):
    for k in (f"{a}|{b}", f"{b}|{a}"):
        if k in (c.get("distances") or {}):
            return c["distances"][k]
    return None


def engaged(c, a):
    out = []
    for e in c.get("engaged") or []:
        if a in e:
            out += [x for x in e if x != a]
    return out


def foes(cb):
    return [k for k, v in cb.items() if v["side"] != "party" and active(v)]


while True:
    c, cb = cs()
    rn = jacks.run(["round-next"])[1].strip()
    m = re.search(r"count -?\d+: (.*?) (acts|is surprised)", rn)
    if "end of round" in rn or "no one left" in rn or not m:
        print("  round-next:", rn[:200]); break
    c, cb = cs()
    nm = m.group(1); ci = c.get("count_index") or 0; od = c.get("order") or []
    pick = [od[i] for i in (ci, ci - 1) if 0 <= i < len(od) and nm in (cb[od[i]].get("perceived"), cb[od[i]].get("name"))]
    who = pick[0] if pick else None
    if who is None or "surprised" in rn or "cannot act" in rn:
        continue
    me = cb[who]
    if not active(me):
        continue
    if me["side"] == "party":
        live = foes(cb)
        if not live:
            continue
        if who in FAN:
            tg = [f for f in live if (dist(c, who, f) or 99) <= 40]
            if tg:
                code, out = jacks.run(["roll", "1d8"]); dmg = int(out.strip().rsplit("=", 1)[1].split()[0])
                print(f"  {who} Fan of Flames 1d8 = {dmg} on {len(tg)}")
                for f in tg:
                    s = jacks.run(["save", f, "blast"])[1]
                    d = dmg // 2 if "SUCCESS" in s else dmg
                    if d > 0:
                        run("damage", f, "--dice", f"{d}d1", "--type", "fire", "--extraordinary")
                FAN.remove(who)
            continue
        if who in SHOOT:
            free = [f for f in live if not engaged(c, f)]
            if free:
                t = min(free, key=lambda f: dist(c, who, f) or 0)
                run("attack", who, t, "--range", "short")
            continue
        if who in FIGHT:
            en = [f for f in engaged(c, who) if f in live]
            if not en:
                near = sorted([f for f in live if (dist(c, who, f) or 99) <= 40], key=lambda f: dist(c, who, f))
                if not near:
                    continue
                run("state", "engage", who, near[0]); en = [near[0]]
            code, out = run("attack", who, en[0])
            while "may cleave" in out:
                c, cb = cs(); live = foes(cb)
                nxt = [f for f in engaged(c, who) if f in live] or [f for f in live if (dist(c, who, f) or 99) <= 5]
                if not nxt:
                    break
                code, out = run("attack", who, nxt[0], "--cleave")
        continue
    # a foe
    tgt = [f for f in engaged(c, who) if active(cb[f])]
    if not tgt:
        cands = [p for p in FIGHT if p in cb and active(cb[p])]
        p = random.choice(cands)
        run("state", "engage", who, p); tgt = [p]
    nat = len(me["stats"]["monster"]["attacks"]) if isinstance(me["stats"]["monster"].get("attacks"), list) else 1
    raw = me["stats"]["monster"]["attacks"][0].get("raw", "1") if nat else "1"
    n = int(re.match(r"(\d+)", raw).group(1)) if re.match(r"(\d+)", raw) else 1
    for i in range(n):
        run("attack", who, tgt[0], "--attack", str(i))
    c, cb = cs()
    down = [k for k, v in cb.items() if v["side"] == "party" and v["hp"] <= 0]
    if down:
        print("PARTY DOWN:", down); sys.exit(3)
c, cb = cs()
print("foes:", [(k, v["hp"]) for k, v in cb.items() if v["side"] != "party" and active(v)])
print("party hurt:", [(k, v["hp"]) for k, v in cb.items() if v["side"] == "party" and v["hp"] < (v.get("hp_max") or v["hp"])])
