# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 29 · **day 480**, 21:56 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 8 | 134730 | 22/22 |  |
| Neris | Priestess 7 | 101512 | 20/20 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Iulia | Crusader 8 | 104646 | 40/40 | minor scarring (puncture wound) |
| Varro | Fighter 6 | 41156 | 25/25 |  |
| Hrodvar | Dwarven Vaultguard 6 | 40592 | 19/19 | notable scarring: his cheek marred by the scars of great claws and fangs (Mortal Wounds, day 423) |
| Brennus | Fighter 7 | 107101 | 29/31 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Phaedra | Mage 6 | 43566 | 20/20 |  |
| Marcellus | Fighter 6 | 42388 | 40/40 |  |
| Vestus the Unlikely | Mage 7 | 93475 | 18/18 |  |
| Cotta | Explorer 4 | 10298 | 13/13 |  |
| Lucilla | Venturer 8 | 138864 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Aelia | Bard 6 | 43613 | 20/20 |  |

- **Adventure:** A104 Descent 65 (G2b, G6) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Iulia (pc), Phaedra (henchman), Varro (henchman), Hrodvar (henchman), Aelia (henchman), Marcellus (henchman), Cotta (henchman); lots 9; monsters 9 (4,930 XP); hoards unfound 39
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 490; varro Varro: 800 gp/month; next due day 497; hrodvar Hrodvar: 800 gp/month; next due day 497; aelia Aelia: 800 gp/month; next due day 504; marcellus Marcellus: 800 gp/month; next due day 504; cotta Cotta: 200 gp/month; next due day 511; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 3; vettius[party] active hp 22/22 init 4; neris[party] active hp 20/20 init 3; iulia[party] active hp 40/40 init 7; varro[party] active hp 25/25 init 1; hrodvar[party] active hp 19/19 init 3; brennus[party] active hp 29/31 init 9; phaedra[party] active hp 20/20 init 5; marcellus[party] active hp 40/40 init 4; vestus-the-unlikely[party] active hp 18/18 init 3; cotta[party] active hp 13/13 init 3; lucilla[party] active hp 42/42 init 4; aelia[party] active hp 20/20 init 4; grey-goo1[foe] slai
- **Schedule:** day 481: vanguard The Imperial Vanguard goes down by the 12U cesspool (AX3 reactions at the grate if the company descends); day 481: circle-rite Nasga's circle gathers at the House of Green Silk (Iulia's month-16 task; until the circle is ended); day 482: circle-rite Nasga's circle gathers at the House of Green Silk (Iulia's month-16 task; until the circle is ended); day 483: circle-rite Nasga's circle gathers at the House of Green Silk (Iulia's month-16 task; until the circle is ended); day 484: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 484: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 484: weekly-double-agents Weekly: the turned-hesitant double agents (#2, #3) and the turncoat; day 484: weekly-watch Weekly: the Watch on the company; day 484: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 484: weekly-hesi
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 30; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A104 paid, its goods sold). The company is at the Solar Citadel, night of day 480. Nobody enervated or wounded beyond a scratch.
- Day 481: Oppius brings the Order's two fresh contracts (H for Lucilla, I for Vettius: reason, petitioner and level in World State, day 480); build each target (an NPC note and `npc.py`), then the PCs plan the deed within the month. The Imperial Vanguard goes down by the 12U cesspool that day: if the company descends, the meeting at the grate by AX3's reactions.
- Each night: the schedule's `circle-rite` (Nasga's circle at the House of Green Silk, Livilla Corax, Adventure/AX3/NPCs). On a rite night Iulia raids with Brennus, Marcellus, Hrodvar and the Watch's men; remove the schedule item when the circle is ended. Keep Iulia out of the Family's work.
- Delves the table chose next: L4 (the troglodyte shaman's guide to the platform), F17 (its glass eggs wake the Great Teacher in T2: the party fears it from Neris' vision; Telepathy or an anti-magic sphere avoids the alarm), the K galleries, J8, R (check prep first: `unprepped-sites.md`).
- Sealed nights below: `camp --watches "A,B;C,D;E,F" --hours 12` (the engine's watches are 4 hours; casters off watch); do not pre-roll the night's checks (camp rolls them). The unsettling-event throw every 12 turns below is by hand (`timer add … --hidden`, then `roll 1d6 --hidden` and the table at 6).
- Fight helpers this session: `Playtest/tools/s29_melee.py` (one round for a melee fight, foes by `count_index`), `s29_sealed.py` (sealed rest turn by turn, non-sealed wanderers ended), `s29_nightchecks.py` (do not use before `camp`).
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
