# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 30 · **day 496**, 18:04 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Iulia | Crusader 8 | 105634 | 20/40 | minor scarring (puncture wound) |
| Hrodvar | Dwarven Vaultguard 6 | 41062 | 17/19 | notable scarring: his cheek marred by the scars of great claws and fangs (Mortal Wounds, day 423) |
| Brennus | Fighter 7 | 108089 | 31/31 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 8 | 136608 | 22/22 |  |
| Neris | Priestess 7 | 102171 | 20/20 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Phaedra | Mage 6 | 44205 | 20/20 |  |
| Vestus the Unlikely | Mage 7 | 94167 | 18/18 |  |
| Cotta | Explorer 4 | 10627 | 13/13 |  |
| Lucilla | Venturer 8 | 140271 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Aelia | Bard 6 | 43942 | 20/20 |  |

- **Adventure:** A111 Descent 67 (L: the queen's caves) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Iulia (pc), Phaedra (henchman), Hrodvar (henchman), Aelia (henchman), Cotta (henchman); lots 7; monsters 4 (1,178 XP); hoards unfound 39
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 520; hrodvar Hrodvar: 800 gp/month; next due day 527; aelia Aelia: 800 gp/month; next due day 504; cotta Cotta: 200 gp/month; next due day 511; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 1; iulia[party] active hp 20/40 init 2; hrodvar[party] active hp 17/19 init 5; brennus[party] active hp 31/31 init 8; vettius[party] active hp 22/22 init 4; neris[party] active hp 20/20 init 2 surprised; phaedra[party] active hp 20/20 init 1; vestus-the-unlikely[party] active hp 18/18 init 2; cotta[party] active hp 13/13 init 2; lucilla[party] active hp 42/42 init 4 surprised; aelia[party] active hp 20/20 init 6 surprised; giant-fly1[foe] dead hp -4/8 init 1 unconscious; giant-fly2[foe] de
- **Schedule:** day 498: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 498: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 498: weekly-double-agents Weekly: the turned-hesitant double agent #3 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 498: weekly-watch Weekly: the Watch on the company; day 498: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 498: weekly-hesitant Weekly: one of the hesitant members turns; day 498: weekly-spies Weekly: Vettius' spies planted; day 498: weekly-secret Weekly: the Family's secret of the week; day 501: order-roll The Order of the Eclipse's weekly assignment roll; day 503: vanguard-l The Imperial Vanguard goes down by the 12U cesspool to L by C2b (the ant caves; AX3 reactions at the grate or below if they meet the company); day 503: grey-sisters-vault The Grey Sisters
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 31; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A111 paid, goods sold). The company of ten at the Solar Citadel, evening of day 496, back from the ant caves: the colony is destroyed (soldiers, queen, eggs). Iulia and Hrodvar hurt (Neris' cures next morning). Vestus and Phaedra have their new spells (Bewitch Monster, Thunderbolt).
- The Vanguard: settled S30 by Rulings S30 (C on day 481, G7 on day 490). They go to L by 12U on day 503 (schedule `vanguard-l`): if the company is below in L or at the grate that day, play the meeting by AX3's reactions; otherwise settle their delve by hidden rolls. The Family has not learned the day-503 plan yet: it is entry 1 of the day-498 week's secrets (write all six before rolling).
- Next below, the table's list: the hidden panel in the queen's cave (to N8c: N is Sub-Abyssal, floor 48; read the N note and its prep status before the party opens it), L4's platform beyond L3's slime (the shaman's guide), F17's sealed cases (the egg-bulbs wake the Great Teacher in T2), the K galleries (L9's lion door), J8, R. No torches or fire over L's sludge or within its air (Rulings S29, S30); masks hourly at +6.
- Timed spells as actor mods (Holy Blessing HB###) do not expire by themselves: `actor unmod ID --item HB###` when the timer ends (slip S30).
- Fight helpers: `Playtest/tools/s29_melee.py`, `s29_antwall.py`, `s29_sealed.py`, `s30_queen.py` (one round against a single big foe). `encounter fight --set hp=` does not set keyed hp: `state set ID hp=N hp_max=N`.
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
