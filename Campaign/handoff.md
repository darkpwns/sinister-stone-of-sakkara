# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 14 · **day 132**, 05:40 · **Catacombs** (dungeon, level 2)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 3 | 6269 | 20/20 | gruesome scarring: nose flattened, cheek crushed, ear cauliflowered (day 87) |
| Faustina | Priestess 3 | 5984 | 15/15 |  |
| Callista | Mage 3 | 5984 | 8/8 |  |
| Corvus | Explorer 3 | 5984 | 16/16 |  |
| Varro | Crusader 1 | 1391 | 3/3 |  |
| Hrodric | Shaman 3 | 5469 | 17/17 |  |
| Quintus | Fighter 1 | 1235 | 7/7 |  |
| Zaira | Elven Spellsword 1 | 1177 | 5/5 |  |
| Severina | Venturer 2 | 2809 | 11/11 |  |
| Marius | Thief 2 | 1417 | 6/6 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35)
- **Adventure:** A11 A11 The Lady Below (Buried Temple, level 2) (open): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Hrodric (pc), Severina (pc), Varro (henchman), Quintus (henchman), Zaira (henchman), Marius (henchman); lots 0; monsters 2 (165 XP); hoards unfound 0
- **Wages:** marius Marius: 50 gp/month; next due day 181; varro Varro: 25 gp/month; next due day 172; quintus Quintus: 25 gp/month; next due day 194; zaira Zaira: 25 gp/month; next due day 194; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Schedule:** nothing due on day 132
- **Standing reminders (lessons whose conditions hold now):**
  - [location-after-return] a long wait under a dungeon location rolls wandering checks and gives no town night: if the company is back in the city, `location --settlement Cyfaraun` first (judge-notes days 317-318 (S17))
  - [torches-relit] no light is lit in the dungeon: `light on --kind torch --carrier ID` (or `light auto on --carriers A,B` once per delve; `play.py walk N --relight A,B` relights by itself) (judge-notes days 349, 352, 354, 406, 427, 430)
- **Lessons to escalate (slipped on again):**
  - ESCALATE [load-before-march] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [familiar-guide] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S15):** branch `ccr-d8a69e1e-0903mi` (this repo; pushed); tools on `tools.ref`, engine 7.24.0. Set Campaign State `session:` to 15 **before any roll**; new session log `S15 — ….md`. Run `acks.sh inv check` first: the S14 end save compacted the inventory again (if a light still in the exploration state now fails as lantern1 did, add its id to the inventory's `settings.lights_before`, as at the start of S14).
- **Standing instructions (user):** the Judge plays the six AI players (Gideon calls); combat is a failure state (steel only when the foe cannot fight back or is plainly outmatched by the party and its allies); dungeon factions used actively; travel only on the Türos Tem-temple corridor until the temple is done; kingdom goal; pooled purse with Faustina, coin above about 900gp banked with Karanos; up to 4 henchmen; a downtime record for everyone before each departure; party notes and rumours kept player-facing.
- **In hand:** dawn of day 132, A11 open, the company and all eight Black Fangs in the Black Fangs' cavern (L2 15; no wandering checks inside, Rulings R2 S14). The Lady is on guard in the Inner Fane (38) with every undead she gathered (the zombies of 23 and 35, the skeletons of 34; 23/34/35 stand empty) and two prisoners on the altar; she saw Marius and refused the ruse but let the company go. Seven company members and the eight Black Fangs bear copied symbols (Faustina and Varro bear none). Two holy water (Genelen); the Ancient Zaharan ward scroll is unreadable to the company.
- **First Judge decision of S15:** a hidden roll (write the terms first) for whether the Lady sends her gathered dead back to their posts on day 132 (and when), and whether she keeps potence up. Then let the AI party choose: bait the dead through the squeeze from 9 one at a time (a chokepoint the party plainly outmatches), wait for the posts to refill and slip in with the symbols, or go up for oil and return. Her tactics (AX1 38): charm person on the strongest fighter, arcane strikes, offers surrender at half hp, seizes the Stone and flees by the escape tunnel (27) when her minions are gone. The Stone: damaging it calls every abomination within 2,000' (all of level 2); destroying it: the striker saves vs Death or becomes an abomination. The party knows only the 'old stories' warning; Ingrid's plan is to carry it out, not smash it in place.
- **Rewards waiting:** the legate's 2,000gp when the raids stop (the Stone destroyed); the Tablet's three fragments to Genelen's order: 10,000 XP among the participants; the Lady's chest (L2 39, poison needle) half to the Black Fangs (deal to day 140).
- **Background:** weekly orc raid rolls on the hobgoblins (from day 120; next for the week of day 134); L1 replacement rolls while the Lady lives (prep queue); month 5 ends on day 150.
- **Slips to watch:** pass `--retrace` on the corridor; turn `light auto off` and put lights out at `location --clear` and before sleeping; give casters with a declared spell no standing order (round-auto passes a 'hold'); check a spell's level on the vault lists before naming it to the players; a wandering band's `reaction --faction` overwrites the faction's attitude (reset it with `faction set`).
