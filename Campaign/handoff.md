# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 29 · **day 487**, 21:18 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Iulia | Crusader 8 | 105195 | 5/40 | minor scarring (puncture wound) |
| Hrodvar | Dwarven Vaultguard 6 | 40853 | 19/19 | notable scarring: his cheek marred by the scars of great claws and fangs (Mortal Wounds, day 423) |
| Brennus | Fighter 7 | 107650 | 13/31 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 8 | 136169 | 22/22 |  |
| Neris | Priestess 7 | 101753 | 20/20 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Phaedra | Mage 6 | 43996 | 20/20 |  |
| Vestus the Unlikely | Mage 7 | 93728 | 18/18 |  |
| Cotta | Explorer 4 | 10418 | 13/13 |  |
| Lucilla | Venturer 8 | 139811 | 36/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Aelia | Bard 6 | 43733 | 20/20 |  |

- **Adventure:** A110 Descent 66 (L: the ant nest, the magic rock) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Iulia (pc), Phaedra (henchman), Varro (henchman), Hrodvar (henchman), Aelia (henchman), Marcellus (henchman), Cotta (henchman); lots 0; monsters 2 (2,165 XP); hoards unfound 39
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 490; hrodvar Hrodvar: 800 gp/month; next due day 497; aelia Aelia: 800 gp/month; next due day 504; cotta Cotta: 200 gp/month; next due day 511; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 1; lucilla[party] active hp 33/42 init 5; vettius[party] active hp 22/22 init 7; vestus-the-unlikely[party] active hp 18/18 init 5; neris[party] active hp 20/20 init 4; brennus[party] active hp 10/31 init 4; phaedra[party] active hp 20/20 init 0; hrodvar[party] active hp 19/19 init 1; aelia[party] active hp 20/20 init 7; cotta[party] active hp 13/13 init 2; gelatinous-mass1[foe] slain hp -1/27 init 6; engaged
- **Schedule:** day 491: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 491: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 491: weekly-double-agents Weekly: the turned-hesitant double agents (#2, #3) and the turncoat; day 491: weekly-watch Weekly: the Watch on the company; day 491: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 491: weekly-hesitant Weekly: one of the hesitant members turns; day 491: weekly-spies Weekly: Vettius' spies planted; day 491: weekly-secret Weekly: the Family's secret of the week; day 491: talk-fades The talk of the purge fades (members' morale -1 ends; the hesitant regain their +1 loyalty); day 494: order-roll The Order of the Eclipse's weekly assignment roll
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 30; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A105-A110 all paid). The company is ten (Varro and Marcellus resigned day 484; actors in Characters/former) at the Solar Citadel, night of day 487. Iulia is abed under the Citadel's care (bed rest to day 492; her hand restored day 485); Brennus mending. No goods unsold.
- Owed first (judge-notes, gap S29): the Imperial Vanguard's descent by 12U on day 481 was never resolved. Before anything else, settle by hidden rolls and record in World State: their route, which rooms they reached (rival play, Adventure/AX3/City/Imperial Vanguard.md: they get somewhere first, sweep it and post a sign: likely ground the company left unfinished, such as L's inner caves, L4, F17 or the K galleries), losses, what they took, and whether and when they came back up. The day-484 week's-secret entry 1 is not established.
- Downtime while Iulia is abed (days 488-492), the party's preparation for the next delve, each by its procedure: Phaedra's wage (day 490, pay before the delve); restock (military oil, torches, holy water, arrows for Cotta and Aelia, iron rations); Phaedra's filter masks; Vestus' and Phaedra's research or spell copying where a procedure applies; the Family's spies on the Vanguard (what the city knows of their descent); no hiring (strength 67 with Iulia, above every floor: the standing instruction). The weekly block day 491 (write the six week's-secret entries before rolling; the turncoat no longer rolls; spies 11 + the week's 1d3). Rulings or rolls the engine does not cover: rule once, record.
- Then the following week (from day 492/493): the delve the table plans with Iulia back (the ward): L's inner caves are next on the party's list (4 soldier ants in L12, the queen and 18 eggs in L13; every surviving ant comes to her; the workers are all dead), L4's platform beyond L3's slime. No torches or fire over L's sludge (firedamp, Rulings S29); the masks' hourly save. The Order's roll day 494 (PCs in the city only).
- The Watch: Tullus Varga's body was found (day 483); its inquiry came up empty on day 484. The week's secret (day 484): the House of Green Silk's patrons want the Prefect to rein in the Captain: Judge's watch on Arëtar.
- Fight helpers: `Playtest/tools/s29_melee.py` (one round; options fan:/fight:/shoot:/front:; foes by count_index), `s29_antwall.py` (a webbed tunnel mouth fed from a pool), `s29_sealed.py` (sealed rest turn by turn). `state init` before each new fight; `encounter end` after each; step initiative with `round-next`, never act outside it; rotate the front before anyone falls below half. Sealed nights: `camp --watches "A,B;C,D;E,F" --hours 12` (4-hour watches, casters off watch); camp rolls the night's checks itself.
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
