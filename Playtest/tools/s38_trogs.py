"""S38 I7 troglodyte driver: steps round-next; a troglodyte makes its 3 attacks (claw, claw, bite) on an engaged party
member (or the nearest standing one it is engaged with); a breeder's damage is 1d2 (SOTN I/J note), the engine's 1d4
re-read as ceil(d4/2) and the hp set back by hand. Stops (exit 3) at a party member's count, a fallen party member,
the last foe down, or a JUDGE line; exit 0 at round-end."""
import json, os, re, sys, math
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
def run(*a):
    code, out = jacks.run(list(a))
    print("  $", " ".join(a)[:70], "->", re.sub(r" \(src: .*", "", out.strip().splitlines()[-1] if out.strip() else "")[:260])
    return code, out
def cs():
    c = json.load(open("Campaign/combat-state.json")); return c, c["combatants"]
def up(x): return x.get("status", "active") == "active" and x["hp"] > 0
def foes(cb): return [k for k in cb if cb[k]["side"] == "foe" and up(cb[k])]
def engaged_with(c, k): return [b if a == k else a for a, b in (tuple(p) for p in c["engaged"]) if k in (a, b)]
PENDING = sys.argv[1:]
def act(pid):
    c, cb = cs()
    if not up(cb[pid]): return
    for n in range(3):
        c, cb = cs()
        tg = [t for t in engaged_with(c, pid) if up(cb[t]) and cb[t]["side"] == "party"]
        if not tg: print("no engaged target for", pid); return
        t = tg[0]; hp0 = cb[t]["hp"]
        code, o = run("attack", pid, t, "--attack", str(n))
        if "JUDGE" in o: print("JUDGE in attack line"); sys.exit(3)
        if pid.startswith("trogb"):
            mm = re.search(r"damage 1d4[^>]*-> \[?(\d+)\]?", o)
            if mm:
                r = int(mm.group(1)); d2 = math.ceil(r / 2)
                c, cb = cs(); new = hp0 - d2
                if cb[t]["hp"] != new:
                    run("state", "set", t, f"hp={new}"); print(f"  correction: breeder 1d2 (d4 {r} -> {d2}): {t} hp {new}")
        c, cb = cs()
        if not up(cb[t]): print("FALLEN:", t); sys.exit(3)
    c, cb = cs()
    if not foes(cb): print("ALL FOES DOWN"); sys.exit(3)
MELEE = {"brennus", "cotta", "lucilla", "vettius", "aelia", "neris"}
def melee(pid, cleave=False):
    c, cb = cs()
    tg = sorted([t for t in engaged_with(c, pid) if up(cb[t]) and cb[t]["side"] == "foe"], key=lambda k: cb[k]["hp"])
    if not tg: print("PARTY COUNT (no engaged foe):", pid); sys.exit(3)
    code, o = run("attack", pid, tg[0], *(["--cleave"] if cleave else []))
    if code != 0 or "JUDGE" in o: print("STOP: attack refused or JUDGE"); sys.exit(3)
    c, cb = cs()
    if not foes(cb): print("ALL FOES DOWN"); sys.exit(3)
    if "may cleave" in o: melee(pid, True)
for p in PENDING: act(p)
while True:
    code, out = jacks.run(["round-next"]); last = out.strip().splitlines()[-1] if out.strip() else ""
    print("NEXT:", re.sub(r" \(src: [^)]*\)", "", last)[:400])
    if code != 0 or "round-end" in last and "count" not in last: sys.exit(0)
    m = re.search(r"count (-?\d+): (.+?) (acts|is |may|in range)", last)
    if not m: sys.exit(0 if "round-end" in last else 3)
    who = m.group(2); c, cb = cs()
    ids = [k for k in cb if cb[k].get("name") == who or cb[k].get("perceived") == who]
    if "cannot act" in last: continue
    cur = c["order"][c["count_index"]] if c.get("count_index") is not None else None
    pid = cur if cur in cb else (ids[0] if ids else None)
    if pid is None:
        print("PARTY COUNT: ?"); sys.exit(3)
    if cb[pid]["side"] != "foe":
        if pid in MELEE and up(cb[pid]):
            melee(pid); continue
        print("PARTY COUNT:", pid); sys.exit(3)
    act(pid)
