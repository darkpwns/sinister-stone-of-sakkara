# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 12 · **day 87**, 06:07 · **Buried Temple** (dungeon, level 1)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 2 | 3682 | 7/7 |  |
| Faustina | Priestess 2 | 3514 | 10/10 |  |
| Callista | Mage 2 | 3514 | 6/6 |  |
| Corvus | Explorer 2 | 3514 | 8/8 |  |
| Marius | None (0th level) 0 | 227 | 4/4 |  |
| Varro | Crusader 1 | 156 | 3/3 |  |
| Hrodric | Shaman 2 | 2999 | 7/7 |  |
| Quintus | Fighter 1 | 0 | 7/7 |  |
| Zaira | Elven Spellsword 1 | 0 | 5/5 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35); severina at Türos Tem (training her pups) (since day 82)
- **Adventure:** A7 Below the stepped tower (Buried Temple, level 2) (open): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Hrodric (pc), Varro (henchman), Quintus (henchman), Zaira (henchman), Marius (henchman); lots 0; monsters 0 (0 XP); hoards unfound 0
- **Wages:** marius Marius: 12 gp/month; next due day 121; varro Varro: 25 gp/month; next due day 142; quintus Quintus: 25 gp/month; next due day 134; zaira Zaira: 25 gp/month; next due day 134; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 2; galerius[party] left hp 6/7 init 6; faustina[party] left hp 10/10 init None; callista[party] left hp 6/6 init 5; corvus[party] left hp 8/8 init 2; marius[party] left hp 4/4 init None; varro[party] left hp 3/3 init -1; giant-rat1[foe] active hp 4/4 init 4; giant-rat2[foe] active hp 4/4 init 5; giant-rat3[foe] active hp 2/2 init 5; giant-rat4[foe] active hp 4/4 init 5; giant-rat5[foe] active hp 4/4 init 5; giant-rat6[foe] active hp 2/2 init 5; giant-rat7[foe] active hp 4/4 init 5; giant-r
- **Schedule:** day 90: month-end Month's end
- **Standing reminders (lessons whose conditions hold now):**
  - [location-after-return] a long wait under a dungeon location rolls wandering checks and gives no town night: if the company is back in the city, `location --settlement Cyfaraun` first (judge-notes days 317-318 (S17))
  - [move-within-speed] a party member's move in a round is at most his running speed (combat speed if he also attacks or casts): `acks.sh move-rate ID` (loaded Lucilla, Brennus and Aelia run 30'); a charge is refused past running speed, a plain move is not (judge-notes S49 day 743 round 13 (Lucilla and Vettius moved 90'))
  - [rest-due] a rest turn after every five turns in a dungeon (`rest`); the line says 'rest due': the party left the temple winded on day 4 (R2 S02 day 4)
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (2 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [load-before-march] (2 slips): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
  - ESCALATE [rest-due] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S13):** branch `claude/hopeful-ptolemy-1ea8tg` (this repo and the rules vault); tools on `tools.ref`. Campaign State `session:` to 13 **before any roll**; new log; `party.agent.call_dir` to the new chat's scratchpad.
- **Standing instructions (user):** the Judge plays the six AI players; Gideon calls; combat is a failure state and dungeon factions are used actively; **travel only between Türos Tem and the Buried Temple until it is complete** (Table rules, lesson temple-corridor); kingdom goal; pooled purse with Faustina; floors L1 6 / L2 12 / L3 18 HD; up to 4 henchmen (Varro, Marius, Quintus, Zaira); a downtime activity each between adventures; Hrodric's eagle by hand.
- **In hand:** day 87, 06:07, in the Buried Temple, L1 27 (the orcs' toll room, Apsa's truce just made); adventure A7 open with Galerius, Faustina, Callista, Corvus, Hrodric (PCs) and Varro, Quintus, Zaira, Marius; 14 HD (floor L2 12). Purse 1,134gp with Faustina; 13,000gp with Karanos (Friendly: 3% early). Torch 8 nearly out (Marius has 4 more; Corvus' torches next). Severina in Türos Tem with her pups (Come learned day 79; next trick, Heel, day 94); Hrodric's pups learned Come day 82, his courses paused from day 82 (resume on return; Heel due day 97 plus the days paused). Guard duty is seven tricks in the order Come, Heel, Stay, Guard, Attack, Defend, Down (Rulings R2 S12).
- **Next:** Idimmu (Friendly since S10) for the stair (100gp a head); below: the Red Eyes' guard room at the stair foot, then west to the Black Fangs (AX1 L2 8-9: +2 peaceful; Ur-Shet partners against the ogres or the Red Eyes). The ogres of L2 7: only with the Black Fangs as the main force (combat is a failure state).
- **Slips (escalated):** load-before-march, rest-due, camp-past-encounter.
