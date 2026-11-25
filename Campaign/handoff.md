# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 8 · **day 49**, 18:16 · **Turos Tem** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Octavia | Mage 1 | 277 | 6/6 | symptomatic: Spotted Pox (incapacitated) |
| Fulvia | Thief 1 | 264 | 5/5 |  |
| Eskil | Shaman 1 | 252 | 5/5 | intestines mangled and ruined (Mortal Wounds, day 16): must rest 2 turns of 6, CON reduced by 1/3, -4 to save vs. poison, -4 to reaction rolls; ghostly visions  |
| Gaius Rufo | None (0th level) 0 | 131 | 3/5 | one foot chewed off (Mortal Wounds, day 16): wooden peg (day 35), movement -30 feet, DEX reduced by 1/3 for AC; symptomatic: Bloody Flux (incapacitated) |
| Septimia | Priestess 1 | 9 | 3/4 |  |
| Aedo | Explorer 1 | 9 | 1/5 | grievously wounded (day 45, giant rats): 2 weeks of bed rest; intestines mangled and ruined (Mortal Wounds, day 45): must rest 2 turns of 6, CON reduced by 1/3, |
| Tullus Brocchus | None (0th level) 0 | 5 | 1/5 | in shock (day 45): magical healing and a night of bed rest (given), or a week of rest; two fingers of one hand bitten off (Mortal Wounds, day 45) |
| Decimus Ruga | None (0th level) 0 | 5 | 1/3 |  |
| Herennius Bow | None (0th level) 0 | 5 | 3/3 |  |
| Ione | None (0th level) 0 | 127 | 3/3 |  |

- **Adventure:** A3 A3 The Buried Temple: the hobgoblins and the prisoners (paid): Octavia (pc), Fulvia (pc), Eskil (pc), Gaius Rufo (pc), Septimia (pc), Aedo (pc), Ione (henchman), Tullus Brocchus (henchman), Decimus Ruga (henchman), Herennius Bow (henchman); lots 0; monsters 1 (75 XP); hoards unfound 0
- **Wages:** ione Ione: 12 gp/month; next due day 91; tullus-brocchus Tullus Brocchus: 12 gp/month; next due day 91; decimus-ruga Decimus Ruga: 12 gp/month; next due day 91; herennius-bow Herennius Bow: 12 gp/month; next due day 91; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Schedule:** nothing due on day 49
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S09):** the run-3 state is on branch `ccr-153d2d1f-1s9f7n` (fetch and merge it into the new chat's branch first). Set Campaign State `session:` to 9 before any roll; new log `Session Log/S09 — ….md`. The Judge plays the six AI players by profiles and heuristics (no party-agent calls); Gideon calls.
- **Reporting (user, 2026-11-25):** while a session is running, reply with no narration and no progress prose; at the end give only the outcomes (what happened, who was hurt or died, money and XP, where the party stands, Judge slips and engine findings, new rulings).
- **In hand:** evening of day 49, Türos Tem, no adventure open. Disease is the problem (`acks.sh disease show`): Eskil (Ague, symptomatic and incapacitated to day 76), onsets days 49-53 for Octavia, Aedo, Gaius, Decimus, Fulvia, Septimia. `disease diagnose ID --by septimia --ranks 1`; cures by hired casting (`spellcasting --payer ID --market "Turos Tem" --market-class V --type divine --level 3 --spell "Cure Disease"`; Genelen Indifferent), then `disease cure ID --how "cure disease"`.
- Aedo on bed rest 14 days from day 45; Eskil and Aedo lodge at the hospital (1sp a night; the courtyard heals 1d3 a day for those resting there, AX1). Wages paid to day 90. Purses: Octavia ~135, Fulvia ~104, Gaius ~80, Eskil ~66, Septimia ~19, Aedo ~7 (owes Octavia 10).
- **Routine slips to avoid:** `camp --hours 12` with watches (rest-day takes none); `light auto off` before waits in a dungeon; never `round-next` right before `round-auto`; a rat bite stops `round-auto` for `disease expose`; never cross 21.20 in fog or camp there (devil boar); rest a day before entering the temple (fatigue).
