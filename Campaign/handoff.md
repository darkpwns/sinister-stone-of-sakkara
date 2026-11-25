# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 11 · **day 80**, 18:05 · **Turos Tem** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 2 | 3682 | 7/7 |  |
| Faustina | Priestess 2 | 3514 | 10/10 |  |
| Callista | Mage 2 | 3514 | 6/6 |  |
| Corvus | Explorer 2 | 3514 | 8/8 |  |
| Marius | None (0th level) 0 | 227 | 4/4 |  |
| Varro | Crusader 1 | 156 | 3/3 |  |
| Petra | None (0th level) 0 | 0 | 3/3 |  |
| Titus | None (0th level) 0 | 0 | 3/3 |  |
| Hrodric | Shaman 2 | 2999 | 7/7 |  |
| Severina | Venturer 1 | 567 | 7/7 |  |
| Quintus | Fighter 1 | 0 | 7/7 |  |
| Zaira | Elven Spellsword 1 | 0 | 5/5 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35)
- **Adventure:** A6 The tower's prisoners (Buried Temple, level 1) (paid): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Marius (henchman), Varro (henchman); lots 1; monsters 1 (5 XP); hoards unfound 0
- **Wages:** marius Marius: 12 gp/month; next due day 121; varro Varro: 25 gp/month; next due day 112; quintus Quintus: 25 gp/month; next due day 134; zaira Zaira: 25 gp/month; next due day 134; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 2; galerius[party] left hp 6/7 init 6; faustina[party] left hp 10/10 init None; callista[party] left hp 6/6 init 5; corvus[party] left hp 8/8 init 2; marius[party] left hp 4/4 init None; varro[party] left hp 3/3 init -1; giant-rat1[foe] active hp 4/4 init 4; giant-rat2[foe] active hp 4/4 init 5; giant-rat3[foe] active hp 2/2 init 5; giant-rat4[foe] active hp 4/4 init 5; giant-rat5[foe] active hp 4/4 init 5; giant-rat6[foe] active hp 2/2 init 5; giant-rat7[foe] active hp 4/4 init 5; giant-r
- **Schedule:** nothing due on day 80
- **Standing reminders (lessons whose conditions hold now):**
  - [move-within-speed] a party member's move in a round is at most his running speed (combat speed if he also attacks or casts): `acks.sh move-rate ID` (loaded Lucilla, Brennus and Aelia run 30'); a charge is refused past running speed, a plain move is not (judge-notes S49 day 743 round 13 (Lucilla and Vettius moved 90'))
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (2 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [load-before-march] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
  - ESCALATE [rest-due] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S12):** branch `claude/hopeful-ptolemy-1ea8tg` (this repo and the rules vault); tools on `tools.ref`. Campaign State `session:` to 12 **before any roll**; new log; `party.agent.call_dir` to the new chat's scratchpad.
- **Standing instructions (user):** the Judge plays the six AI players; Gideon calls; combat is a failure state and dungeon factions are used actively (Table rules, heuristics); kingdom goal; pooled purse with Faustina; floors L1 6 / L2 12 / L3 18 HD; up to 4 henchmen (now Varro, Marius, Quintus, Zaira); a downtime activity each; Hrodric's eagle by hand.
- **In hand:** day 80, 18:05, Türos Tem, everyone in town, rested. Weather rolled through day 80 (wet; mud stands): roll each further day (`weather --at 22.20 --day N`). The inn and the pups' feed paid through day 80 and 82. Quintus and Zaira hold only 0 days of food: provision before any march. Armor was short this month (Quintus in hide; a better suit when month 4 opens on day 91).
- **Next:** the pilgrimage to the Shrine of the White Lady (23.16), Faustina leading, when the ground dries: **build the site first** (`unprepped-sites.md`; prep queue). The arch in 22.20 (Rulings R2 S11). The temple: hobgoblins allied, Idimmu Friendly, Abgal below.
- **Training:** Severina's first tricks day 79 (check `train show`: record what was learned), Hrodric's day 82.
- **Slips (escalated):** load-before-march, rest-due, camp-past-encounter (judge-notes, slips.jsonl).
