# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 33 · **day 516**, 10:16 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Iulia | Crusader 8 | 128178 | 40/40 | minor scarring (puncture wound) |
| Brennus | Fighter 8 | 131284 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 8 | 172550 | 22/22 |  |
| Neris | Priestess 7 | 123642 | 20/20 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Phaedra | Mage 6 | 55249 | 20/20 |  |
| Vestus the Unlikely | Mage 7 | 116711 | 18/18 |  |
| Cotta | Explorer 5 | 21361 | 18/18 |  |
| Lucilla | Venturer 8 | 163890 | 31/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Aelia | Bard 6 | 54676 | 20/20 |  |

- **Adventure:** A118 Descent 73 (N: the library) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Iulia (pc), Phaedra (henchman), Aelia (henchman), Cotta (henchman); lots 9; monsters 1 (50 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 550; aelia Aelia: 800 gp/month; next due day 534; cotta Cotta: 400 gp/month; next due day 541; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Schedule:** day 519: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 519: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 519: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 519: weekly-watch Weekly: the Watch on the company; day 519: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 519: weekly-hesitant Weekly: one of the hesitant members turns; day 519: weekly-spies Weekly: Vettius' spies planted; day 519: weekly-secret Weekly: the Family's secret of the week; day 522: order-roll The Order of the Eclipse's weekly assignment roll
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
- **Lessons to escalate (slipped on again):**
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 34; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A118 paid). Nine at the Solar Citadel, day 516 noon; Lucilla below full hp (cures or rest first). The combat state file is gone (`state init` or `encounter fight` before each fight).
- The table's next steps: the last library jars in N3 (one half-load trip); the south-west passage behind N11 (the hepatizon orb in the SW hollow opens it and must stay there while anyone is beyond; N12's sconces hold yellow mold spores; in N13 the orbs swap roles: the electrum opens O1, the hepatizon blasts). Beyond is O, the deadliest tomb of the module (a 12-HD mummy lord and two 9-level mummies, beyond Smite Undead; four bronze statues); its door password (Orthanach) is in J14's records. Prep queue in World State has the detail.
- Phaedra put off her Skinchange study (L723) for the delves: a week's study when she takes it up. Vestus has Flight.
- Unsettling-event throws: keep the 12-turn timer while in the Nethercity and roll at its expiry (`play.py walk` does not stop for it).
- Every sealed N door opens for Vettius (the sword of command): he walks up first.
- Light: Vettius' lantern over the sludge shut (`light close`), Iulia's spear; masks; torches only in clean air; Aelia and Brennus carry the torches.
- Escalated lesson [npc-rolls-hidden] stands (roll an NPC's Mortal Wounds with `roll --hidden`). New lesson [location-site-keeps-settings]: pass the hub column's settings with every `location --site`.
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
