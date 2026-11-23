"""S34 O3 driver: ONE round from round-end of the last, while Orthanach stands silenced in Neris' Noiselessness.
Brennus, Vettius (and Lucilla once she shakes off the visage: her paralysis save at her count, the Mummy rule: cower to
the next round) attack him; Neris concentrates; Vestus tends Phaedra. Orthanach cannot cast (silence) and the rod needs
its word (Judge's ruling S34): each round a hidden 1d6: 1-3 touch Brennus, 4-5 bewitch Brennus (spell-like, Spells save
+5 threatened), 6 summon insect plague (spell-like, once): the driver stops on 4-6 for the Judge.
Stops (exit 3) when a party member falls or Orthanach reaches 0 hp. Corrects the engine's visage saves for those already
immune this turn (saved earlier: Brennus, Vettius, Neris, Vestus)."""
import json, re, sys
sys.path.insert(0, ".claude/skills/acks2-judge/scripts")
import jacks
IMMUNE = {"brennus", "vettius", "neris", "vestus-the-unlikely"}
def run(*a):
    code, out = jacks.run(list(a)); line = out.strip().splitlines()[-1] if out.strip() else ""
    print("  $", " ".join(a)[:50], "->", re.sub(r" \(src: .*", "", line)[:200]); return code, out
def cs():
    c = json.load(open("Campaign/combat-state.json")); cb = c["combatants"]
    return c, (cb if isinstance(cb, dict) else {x["id"]: x for x in cb})
def conds(x): return [k["name"] for k in x.get("conditions", [])]
run("round-end"); run("round-start")
while True:
    code, out = run("round-next")
    if "round-end" in out or code: break
    m = re.search(r"count -?\d+: (.+?) (acts|is )", out)
    if not m: continue
    who = m.group(1); c, cb = cs()
    pid = {"Brennus": "brennus", "Vettius": "vettius", "Lucilla": "lucilla", "Neris": "neris",
           "Vestus the Unlikely": "vestus-the-unlikely", "Phaedra": "phaedra"}.get(who, "orthanach" if "mummy" in who or "Orthanach" in who else None)
    if pid in IMMUNE and "cowering" in conds(cb[pid]): run("state", "uncond", pid, "cowering")
    if pid in ("brennus", "vettius"):
        run("attack", pid, "orthanach")
    elif pid == "lucilla":
        if "cowering" in conds(cb["lucilla"]):
            run("state", "uncond", "lucilla", "cowering")
            code, o = run("save", "lucilla", "paralysis", "--by", "orthanach")
            if "SUCCESS" in o: IMMUNE.add("lucilla"); print("  Lucilla shakes off the stare (immune this turn); she acts next round")
            else: run("state", "cond", "lucilla", "cowering")
        else:
            run("attack", "lucilla", "orthanach")
    elif pid == "orthanach":
        code, o = run("roll", "--hidden", "Orthanach's action in the silence (1-3 touch Brennus, 4-5 bewitch Brennus, 6 insect plague):1d6")
        k = int(re.search(r"= (\d+)", o).group(1))
        if k <= 3: run("attack", "orthanach", "brennus", "--attack", "0")
        else: print(f"STOP: Orthanach's choice {k}: the Judge resolves it"); sys.exit(4)
    c, cb = cs()
    if cb["orthanach"]["hp"] <= 0: print("STOP: Orthanach at 0 hp"); sys.exit(3)
    if any(v["side"] == "party" and v["hp"] <= 0 and k not in ("iulia", "phaedra") for k, v in cb.items()):
        print("STOP: a party member is down"); sys.exit(3)
    if "concentrating" not in conds(cb["neris"]): print("STOP: Neris' concentration broke"); sys.exit(3)
