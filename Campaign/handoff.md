# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 15 · **day 139**, 05:54 · **21.20** (wilderness)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 3 | 7771 | 20/20 | gruesome scarring: nose flattened, cheek crushed, ear cauliflowered (day 87) |
| Faustina | Priestess 3 | 7418 | 15/15 |  |
| Callista | Mage 3 | 7418 | 8/8 |  |
| Corvus | Explorer 3 | 7418 | 16/16 |  |
| Varro | Crusader 2 | 2109 | 5/5 |  |
| Hrodric | Shaman 4 | 6903 | 18/18 |  |
| Quintus | Fighter 1 | 1953 | 7/7 |  |
| Zaira | Elven Spellsword 1 | 1860 | 5/5 |  |
| Severina | Venturer 3 | 4243 | 17/17 |  |
| Marius | Thief 2 | 2135 | 6/6 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35)
- **Adventure:** A11 A11 The Lady Below (Buried Temple, level 2) (paid): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Hrodric (pc), Severina (pc), Varro (henchman), Quintus (henchman), Zaira (henchman), Marius (henchman); lots 11; monsters 5 (943 XP); hoards unfound 0
- **Wages:** marius Marius: 50 gp/month; next due day 181; varro Varro: 50 gp/month; next due day 172; quintus Quintus: 25 gp/month; next due day 194; zaira Zaira: 25 gp/month; next due day 194; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 5; galerius[party] active hp 20/20 init 4 fatigued; faustina[party] active hp 15/15 init 1; callista[party] active hp 8/8 init 6; corvus[party] active hp 16/16 init 6; varro[party] active hp 3/3 init -1 fatigued; hrodric[party] active hp 17/17 init 4; hrodric-eagle[party] active hp 5/8 init 3; quintus[party] active hp 7/7 init 6; zaira[party] active hp 5/5 init 4; severina[party] active hp 11/11 init 0; marius[party] active hp 2/6 init 3; zombie1[foe] destroyed hp -2/7 init 3; zombie2[foe]
- **Schedule:** nothing due on day 139
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [load-before-march] (4 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [familiar-guide] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S16):** branch `ccr-d8a69e1e-0903mi` (this repo; pushed); tools on `tools.ref`, engine 7.24.0. Set Campaign State `session:` to 16 **before any roll**; new session log `S16 — ….md`. Run `acks.sh inv check` after setup (add any light id a compaction archived to the inventory's `settings.lights_before`).
- **Standing instructions (user):** the Judge plays the six AI players (Gideon calls); combat is a failure state; dungeon factions used actively; travel only on the Türos Tem-temple corridor until the temple is done (the Stone is not destroyed: the rule stands); kingdom goal; pooled purse with Faustina, coin banked with Karanos; up to 4 henchmen; a downtime record for everyone before each departure; party notes and rumours player-facing.
- **In hand:** dawn of day 139, camp at the freeholder's well in 21.20, heavy rain and strong wind; the company bound for the temple (20.19) to go after the Stone. No adventure open: `adventure start` (A12) and `join` everyone before going below. Donkeys with Apsa's orcs at L1 27 (stabling owed from day 131). Water filled at the well; fill again at the spring in 20.19.
- **The Lady is dead (day 132)**; the Stone was carried below by five troglodytes by a crack beyond the cave-in past L2 31 (Rulings R2 S15). **Before the company follows, build the troglodytes' warren** (unprepped-sites.md; the prep queue gives the choices) and decide the route the company can take (36-25-26-28-30-31, or the spiral stair from L1 18 to 29's bars and 28's ghouls). The Lady's dead keep their posts at 23, 34, 35; Faustina and Varro carry no sign.
- **Rewards waiting:** the legate's remaining 1,500gp when the raids stop (decide by a recorded roll whether raids continue, the first time the company is in town); the Tablet's three fragments to Genelen's order: 10,000 XP among the participants; the fane's cleansing (200 XP each Lawful) once the Stone is destroyed.
- **Slips to watch (S15):** check every member's march load **with carried food and water** before `travel` (move-rate leaves supplies out; the engine refuses only when a pack animal has room); `water --source` at every well and river the party camps at or passes (lesson water-at-known-source); a room's `wandering: none` set as the site rate stays after leaving the room: reset the level's rate; roll a monster's surprise note penalty before any reaction.
