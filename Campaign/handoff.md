# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 31 · **day 503**, 05:50 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Iulia | Crusader 8 | 108447 | 40/40 | minor scarring (puncture wound) |
| Brennus | Fighter 7 | 110902 | 31/31 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 8 | 139421 | 22/22 |  |
| Neris | Priestess 7 | 104850 | 20/20 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Phaedra | Mage 6 | 45544 | 20/20 |  |
| Vestus the Unlikely | Mage 7 | 96980 | 18/18 |  |
| Cotta | Explorer 4 | 11966 | 13/13 |  |
| Lucilla | Venturer 8 | 143218 | 40/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Aelia | Bard 6 | 45281 | 20/20 |  |

- **Adventure:** A113 Descent 69 (K: the hero tomb) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Iulia (pc), Phaedra (henchman), Hrodvar (henchman), Aelia (henchman), Cotta (henchman); lots 4; monsters 2 (6,480 XP); hoards unfound 39
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 520; aelia Aelia: 800 gp/month; next due day 534; cotta Cotta: 200 gp/month; next due day 511; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 4; iulia[party] active hp 39/40 init 6; hrodvar[party] absent hp 13/19 init None; brennus[party] active hp 24/31 init 7; vettius[party] active hp 22/22 init 4; neris[party] active hp 20/20 init 7; phaedra[party] active hp 20/20 init 1; vestus-the-unlikely[party] active hp 18/18 init 7; cotta[party] active hp 13/13 init 5; lucilla[party] active hp 33/42 init 2; aelia[party] active hp 20/20 init 5; bombardier-beetle1[foe] dead hp -3/13 init 1 unconscious; bombardier-beetle2[foe] dead hp -2/1
- **Schedule:** day 504: vanguard-k The Imperial Vanguard goes down by the 12U cesspool to K by L9 (AX3 reactions if the company is at the grate or below); day 505: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 505: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 505: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 505: weekly-watch Weekly: the Watch on the company; day 505: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 505: weekly-hesitant Weekly: one of the hesitant members turns; day 505: weekly-spies Weekly: Vettius' spies planted; day 505: weekly-secret Weekly: the Family's secret of the week; day 507: l-miasma-returns L's miasma gathers again over the sludge (burned off by the Vanguard's blast on day 503); firedamp rules
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 32; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A112, A113 paid; goods sold). Nine in the company at the Solar Citadel, morning of day 503, whole. Hrodvar resigned after his grievous wound (abed in the city at his own charge; actor in Characters/former); the party keeps the henchmen it has and does not hire (strength above every floor).
- Below, the table's list: the alchemists' laboratory beyond the queen's panel (its bronze doors are sealed: approved personnel, a shadowcowl robe, an iron mask, the sword of command, or Dispel Magic at caster level 11+; Passageway through the wall), the shaman's platform (L4) beyond L3's slime, the sealed cases (F17: the egg-bulbs wake the Great Teacher in T2), J8, R (check its prep first). K is emptied but for K9's flailing spirit.
- The Vanguard: L on day 503 (the firedamp killed a man-at-arms and burned the miasma off until day 507: flame is safe over L's sludge until then; the schedule restores the rule). Next: K on day 504 (schedule `vanguard-k`), by Rulings S30.
- The Family: double agents #3 and #4 roll weekly; write the six week's-secret entries before the day-505 roll.
- Engine findings to watch: the stone slab door kind gave -6 (not Rulings S18's 0): check the doors ruling before the next slab; a monster with several weapon attacks takes no `--weapon`; drivers must resolve actors by perceived name (`count_index`); `timer remove` takes the label.
- Fight helpers: `Playtest/tools/s29_melee.py` (one round), `s30_queen.py` (one big foe), `s31_golems.py` (wards and Smite Undead against blocked undead). Rotate the front before anyone falls below half.
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
