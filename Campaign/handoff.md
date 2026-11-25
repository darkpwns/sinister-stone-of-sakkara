# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 10 · **day 74**, 07:05 · **21.20** (wilderness)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 2 | 3571 | 6/7 |  |
| Faustina | Priestess 2 | 3408 | 10/10 |  |
| Callista | Mage 2 | 3408 | 6/6 |  |
| Corvus | Explorer 2 | 3408 | 8/8 |  |
| Marius | None (0th level) 0 | 177 | 4/4 |  |
| Varro | Crusader 1 | 104 | 3/3 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35); hrodric at Türos Tem (the pups) (since day 69); severina at Türos Tem (the pups) (since day 69); petra at Türos Tem (the pups) (since day 69); titus at Türos Tem (the pups) (since day 69)
- **Adventure:** A6 The tower's prisoners (Buried Temple, level 1) (open): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Marius (henchman), Varro (henchman); lots 0; monsters 1 (5 XP); hoards unfound 0
- **Wages:** marius Marius: 12 gp/month; next due day 121; petra Petra: 12 gp/month; next due day 128; titus Titus: 12 gp/month; next due day 135; varro Varro: 25 gp/month; next due day 112; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 2; galerius[party] left hp 6/7 init 6; faustina[party] left hp 10/10 init None; callista[party] left hp 6/6 init 5; corvus[party] left hp 8/8 init 2; marius[party] left hp 4/4 init None; varro[party] left hp 3/3 init -1; giant-rat1[foe] active hp 4/4 init 4; giant-rat2[foe] active hp 4/4 init 5; giant-rat3[foe] active hp 2/2 init 5; giant-rat4[foe] active hp 4/4 init 5; giant-rat5[foe] active hp 4/4 init 5; giant-rat6[foe] active hp 2/2 init 5; giant-rat7[foe] active hp 4/4 init 5; giant-r
- **Schedule:** nothing due on day 74
- **Standing reminders (lessons whose conditions hold now):**
  - [move-within-speed] a party member's move in a round is at most his running speed (combat speed if he also attacks or casts): `acks.sh move-rate ID` (loaded Lucilla, Brennus and Aelia run 30'); a charge is refused past running speed, a plain move is not (judge-notes S49 day 743 round 13 (Lucilla and Vettius moved 90'))
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (2 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [load-before-march] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
  - ESCALATE [rest-due] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S11):** branch `claude/hopeful-ptolemy-1ea8tg` (this repo and the rules vault); tools on `tools.ref`. Campaign State `session:` to 11 **before any roll**; new log `Session Log/S11 — <summary>.md`; `party.agent.call_dir` to the new chat's scratchpad.
- **Standing instructions (user):** as S09-S10: the Judge plays the six AI players; Gideon calls; **combat is a failure state; dungeon factions are used actively** (Table rules, heuristics); kingdom goal; pooled purse with Faustina; floors L1 6 / L2 12 / L3 18 HD; up to 4 henchmen; a downtime activity each; Hrodric's eagle by hand.
- **In hand:** dawn of day 74 at the well in 21.20 (half a day from Türos Tem) with Galerius, Faustina, Callista, Corvus, Varro, Marius, both donkeys and seven freed captives without actors (fed by hand: Rulings R2 S10). Hrodric, Severina, Petra and Titus in town with the pups (courses running). Adventure A6 open.
- **On arrival:** `location --settlement "Turos Tem"`; the merchants to Karanos: `recover --reward 500 --carrier faustina` (A6), Karanos **Friendly** (AX1 note: fees 3%, 1d4-1 shipping contracts); `adventure return`, payout A6; the inn (the Brethren's old bill 7gp 4sp 2cp: a Neutral reaction or Bargaining avoids paying; paying makes the innkeeper Friendly and yields a rumour). The rescued offer service (World State prep queue): the players decide within the cap of 4 henchmen. Callista may copy the Brethren's formulas.
- **Temple state:** hobgoblins allied (repulsed an orc raid); Idimmu Friendly (sold prisoners; the Lady's priests buy from him); Abgal below with the Lady; Red Eyes guard the ziggurat stair.
- **Slips (judge-notes / slips.jsonl):** load-before-march escalated (Varro overloaded day 69: check `move-rate` for every member after buying food); rest-due and camp-past-encounter escalated (S09).
