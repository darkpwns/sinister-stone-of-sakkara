# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 16 · **day 148**, 18:10 · **Türos Tem** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 4 | 9852 | 19/21 | gruesome scarring: nose flattened, cheek crushed, ear cauliflowered (day 87) |
| Faustina | Priestess 4 | 9414 | 20/20 |  |
| Callista | Mage 3 | 9214 | 8/8 |  |
| Corvus | Explorer 4 | 9214 | 18/18 |  |
| Varro | Crusader 3 | 3207 | 8/8 |  |
| Hrodric | Shaman 4 | 8699 | 17/18 |  |
| Quintus | Fighter 2 | 2851 | 8/8 |  |
| Severina | Venturer 4 | 6039 | 21/21 |  |
| Marius | Thief 3 | 3033 | 13/13 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35); zaira at left Callista's service (day 145); at the inn in Türos Tem, healing (since day 145)
- **Adventure:** A12 A12 The Stone Below (Buried Temple, level 2, and the troglodyte warren) (paid): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Hrodric (pc), Severina (pc), Varro (henchman), Quintus (henchman), Zaira (henchman), Marius (henchman); lots 13; monsters 9 (906 XP); hoards unfound 2; partly taken: H2 Troglodyte warren W6 (the chieftain's hall): [0] 22,000 22,000 copper pieces; [1] 8,000 8,000 silver pieces; [2] 1,000 1,000 electrum pieces; [3] taken: ornamental worth 25gp (Agate, lapis lazuli, tiger eye, turquoise) (25gp); [4] taken: ornamental worth 50gp (Bloodstone, crystal, citrine, jasper, moonstone, onyx) (50gp); [5] taken: ornamental worth 25gp (Agate, lapis lazuli, ti
- **Wages:** marius Marius: 100 gp/month; next due day 181; varro Varro: 100 gp/month; next due day 172; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 3; galerius[party] active hp 14/20 init 5; faustina[party] active hp 15/15 init 2; callista[party] active hp 8/8 init 6; corvus[party] active hp 13/16 init 6; varro[party] active hp 5/5 init 2; hrodric[party] active hp 14/18 init 3; hrodric-eagle[party] active hp 9/12 init 3; quintus[party] active hp 7/7 init 6; severina[party] active hp 17/17 init 1; marius[party] active hp 6/6 init 5; zaira[party] active hp 1/5 init 4; large-raptor1[foe] dead hp 0/4 init 5 unconscious; engaged
- **Schedule:** day 150: month-end Month's end; day 155: orc-raid-hobgoblins Apsa's orcs raid the hobgoblins (L1)
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [load-before-march] (4 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [familiar-guide] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S17):** branch `ccr-d8a69e1e-0903mi` (this repo; pushed); tools on `tools.ref`, engine 7.24.0. Set Campaign State `session:` to 17 **before any roll** (the S16 build rolls landed under session 15 because it was set late); new session log `S17 — ….md`. Run `acks.sh inv check` after setup (add any light id a compaction archived to the inventory's `settings.lights_before`).
- **Standing instructions (user):** the Judge plays the six AI players (Gideon calls); combat is a failure state (steel only when the foe cannot fight back or is plainly outmatched); dungeon factions used actively; kingdom goal; pooled purse with Faustina, coin banked with Karanos; up to 4 henchmen; a downtime record for everyone before each departure; party notes and rumours player-facing. The corridor rule is fulfilled (AX1 complete day 143).
- **In hand:** evening of day 148 in Türos Tem. **Between adventures:** Campaign State says so, so the resume loads `R/bootstrap.md` (its last section: a new adventure in a running campaign). Next per Table rules: AX2 *Secrets of the Nethercity* (`Adventure/SOTN/`; hub hook: a priestess henchman sought in Cyfaraun; the Lady's letter to a 'Lord of Secrets' is a second bridge). Decide with the AI table what they do first (they know nothing of SOTN): recruit henchmen (Callista lost Zaira; Galerius loses Quintus on day 150), the Shrine of the White Lady (23.16, unprepped), the arch at the full moon.
- **Month 5 ends on day 150:** `play.py month-end` (wages: Quintus' last month; Varro 50gp from day 172; training courses; the bank).
- **Slips to watch (S15-S16):** loads with carried supplies before `travel`; `water --source` at every well; the surprise note penalty before any `reaction` (lesson note-penalty-before-reaction); `capture` before `state end`; a zone's frontage does not block passage: keep foes out of a held tunnel by hand; casters with declared spells and members declaring withdrawal get order `none` so round-auto stops for them; pause training courses when the trainers leave town; never type an item's true name into an open roll label.
