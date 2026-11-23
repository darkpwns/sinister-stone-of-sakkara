# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 32 · **day 510**, 05:50 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Iulia | Crusader 8 | 111098 | 40/40 | minor scarring (puncture wound) |
| Brennus | Fighter 7 | 113553 | 31/31 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 8 | 154819 | 22/22 |  |
| Neris | Priestess 7 | 107375 | 20/20 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Phaedra | Mage 6 | 46806 | 20/20 |  |
| Vestus the Unlikely | Mage 7 | 99631 | 18/18 | studying Flight from the princess's book (L724), a week's dedicated study, days 507-513 (JJ Spell Repertoire) |
| Cotta | Explorer 4 | 13228 | 13/13 |  |
| Lucilla | Venturer 8 | 145996 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Aelia | Bard 6 | 46543 | 20/20 |  |

- **Adventure:** A114 Descent 70 (R: the prince and princess) (paid): Lucilla (pc), Vettius (pc), Vestus the Unlikely (pc), Neris (pc), Brennus (pc), Iulia (pc), Phaedra (henchman), Aelia (henchman), Cotta (henchman); lots 11; monsters 5 (6,961 XP); hoards unfound 77
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 520; aelia Aelia: 800 gp/month; next due day 534; cotta Cotta: 200 gp/month; next due day 511; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 3; iulia[party] active hp 35/40 init 5; brennus[party] active hp 31/31 init 9; vettius[party] active hp 22/22 init 7; neris[party] active hp 20/20 init 6; phaedra[party] active hp 20/20 init 2; vestus-the-unlikely[party] active hp 18/18 init 3; cotta[party] active hp 13/13 init 6; lucilla[party] active hp 27/42 init 5; aelia[party] active hp 20/20 init 4; giant-fly1[foe] dead hp -1/8 init 5 unconscious; giant-fly2[foe] dead hp -5/11 init 3 unconscious; giant-fly3[foe] dead hp -2/12 init 5 
- **Schedule:** day 512: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 512: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 512: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 512: weekly-watch Weekly: the Watch on the company; day 512: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 512: weekly-hesitant Weekly: one of the hesitant members turns; day 512: weekly-spies Weekly: Vettius' spies planted; day 512: weekly-secret Weekly: the Family's secret of the week; day 515: order-roll The Order of the Eclipse's weekly assignment roll
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
- **Lessons to escalate (slipped on again):**
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 33; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A114 paid). Nine at the Solar Citadel on day 510, whole. Vestus studies Flight (L724) to day 513 (then `actor item vestus-the-unlikely add spell "Flight" --level 3` and drop the condition). Phaedra could study Skinchange or Flight next.
- Against poison (S32): Delay Poison before the front walks into the unknown; Neris' and Iulia' scrolls (Neutralize Poison x3, Delay Poison x1) are inventory items; a Potion of Antivenom is worth buying when the month's stock has one.
- Brennus' Order contract: Cnaeus Lento (Fighter 3), due by day 540; build him (npc.py) before the deed.
- Below: R2 still holds the gilded coffins and the great tusks (heavy: about 63 stone); R3's bronze door (288 skeletons, 2d20 a round after 6 rounds) unopened; N's sealed doors; L4, F17, J8.
- The Vanguard: away on a bounty after Irial's funeral (back about day 535); their delves use the JJ abstract method (Rulings S31).
- Watch: the campaign doors table's slab row now reads Rulings S18 (0, 2 helpers); magic arrows are goods lots (finding); `mortal-wounds` has no --hidden (NPC rolls through it are open: re-read hidden ones by hand).
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
