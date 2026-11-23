# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 34 · **day 523**, 05:45 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Brennus | Fighter 8 | 144865 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 9 | 186131 | 32/32 |  |
| Neris | Priestess 8 | 136577 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Vestus the Unlikely | Mage 7 | 130292 | 18/18 |  |
| Lucilla | Venturer 8 | 178119 | 39/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 32835 | 19/19 |  |
| Aelia | Bard 7 | 61144 | 22/23 |  |
| Hrodvar | Dwarven Vaultguard 6 | 42401 | 19/19 | notable scarring: his cheek marred by the scars of great claws and fangs (Mortal Wounds, day 423); intestines mangled and ruined (Mortal Wounds, day 499): must  |

- **Adventure:** A121 Descent 76 (O: the coffins) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Aelia (henchman), Cotta (pc); lots 6; monsters 1 (80 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 550; aelia Aelia: 1600 gp/month; next due day 534; hrodvar Hrodvar: 800 gp/month; next due day 553; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 4; brennus[party] active hp 34/35 init 6; vettius[party] active hp 31/32 init 6; neris[party] active hp 21/21 init 3; vestus-the-unlikely[party] active hp 18/18 init 5; lucilla[party] active hp 37/42 init 2; cotta[party] active hp 17/18 init 3; aelia[party] active hp 21/23 init 7; tunnel-prawn-sotn1[foe] dead hp -6/4 init 6 faltering,unconscious; tunnel-prawn-sotn2[foe] dead hp -2/1 init 5 unconscious; tunnel-prawn-sotn3[foe] dead hp -7/7 init 1 faltering,unconscious; tunnel-prawn-sotn4[fo
- **Schedule:** day 526: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 526: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 526: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 526: weekly-watch Weekly: the Watch on the company; day 526: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 526: weekly-hesitant Weekly: one of the hesitant members turns; day 526: weekly-spies Weekly: Vettius' spies planted; day 526: weekly-secret Weekly: the Family's secret of the week; day 529: order-roll The Order of the Eclipse's weekly assignment roll
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 35; read `R/memory.md`; `brief.py` prints this file. A new session note `Session Log/S35 — <summary>.md`, linked in the Campaign Log.
- In hand: no adventure open (A121 paid). Day 523, 05:45, the Solar Citadel. Nine: PCs Lucilla, Vettius, Brennus, Vestus, Neris and Cotta (Gideon's, since Iulia's death); henchmen Aelia (Lucilla's), Phaedra (Vettius'; abed to day 524, a peg foot) and Hrodvar (Vettius'; rejoined day 523 by the user's decision: apply his wound by hand, 2 turns of rest in 6, though the engine reads him as Endurance). Iulia is dead; the Rod of the Dawn and the Underwatch shield and spear are back with Arëtar, so the company has no moving ward but Neris' Holy Circle (Sustained); the lesson [underwatch-ward] is retired.
- The table's plan for the week (user's direction): (1) hire a replacement crusader at the highest level the market yields (only Vettius can take a 6th-level henchman; the engine's `retinue employer`, `recruit --class Crusader --level N`, `candidate`, `offer`, `hire`; give the hire the proficiencies his level allows); (2) Neris petitions Patriarch Arëtar to lend the Underwatch regalia (and if possible the Rod) to that crusader, pressing his concern for the Awakening and offering evidence (the hierophant's black scroll L794, the golden-skull shrine L786): a reaction/influence roll with named modifiers; rule it, record it in Rulings and World State. Arëtar is also to name a new Captain of the Underwatch (the knights quarrel over it: day-519 secret).
- Also due: Vestus' Order contract on Marius Corvo (built; NPC note) by day 540, by the Order's procedure, commission as its own adventure record; the Tower's identifications (ring, bracers, rod) on the schedule; the golden-skull shrine in the Grey Sisters' vault needs its 12th-level rune dispelled before anyone touches it.
- Below, by the company's own knowledge: N3's last 80 jars (easy; Vettius opens N's doors, the orbs are Vestus'), two coffin pieces in O3, F17's cases (the egg-bulbs wake the Great Teacher), J8's throne, L4's platform. Unknown to them: the white apes' caves (M), H14's crystals, the Great Teacher's sepulcher (T).
- Engine work-arounds in force (Rulings S34): a mummy's visage aura keeps cowering forever and ignores the immunity after a success: correct by hand; Righteous Rebuke's extra Hit Dice and Battle Magic's +1 initiative are not applied; a bash loop around a fight driver must break on the driver's exit code (lesson [driver-loop-stop]); `location --site` needs the hub column's settings (lesson [location-site-keeps-settings]); unsettling-event timers do not stop `play.py walk`: roll them at expiry.
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
