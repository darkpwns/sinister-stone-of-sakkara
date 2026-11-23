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
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 520; aelia Aelia: 800 gp/month; next due day 534; cotta Cotta: 200 gp/month; next due day 541; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 0; engaged
- **Schedule:** day 512: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 512: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 512: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 512: weekly-watch Weekly: the Watch on the company; day 512: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 512: weekly-hesitant Weekly: one of the hesitant members turns; day 512: weekly-spies Weekly: Vettius' spies planted; day 512: weekly-secret Weekly: the Family's secret of the week; day 515: order-roll The Order of the Eclipse's weekly assignment roll
- **Standing reminders (lessons whose conditions hold now):**
  - [underwatch-ward] Iulia bears the Underwatch shield (a Holy Circle that moves with her): once the fight is set up, `state ward add iulia --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14"` (`state ward out iulia ID` for anyone beyond 10'); the engine then bars enchanted creatures and drops the barrier per creature; `state ward close iulia` at the next turn (Rulings S14 (row 103), S15, S16, S19; RR p. 225)
- **Lessons to escalate (slipped on again):**
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 33; read `R/memory.md`; `brief.py` prints this file.
- In hand: no adventure open (A114 paid). Nine at the Solar Citadel, day 510, whole; the combat state is empty (`state init` again before each fight). Vestus studies Flight (L724) to day 513: then `actor item vestus-the-unlikely add spell "Flight" --level 3 --cause "…"` and drop the condition. Phaedra may study Skinchange or Flight from the rolls next. Cotta's wage paid ahead (day 510); Phaedra's falls due before the next delve after day 519.
- Against poison (S32): Delay Poison on the front before the unknown (RR p. 213; it also holds back one slain by poison within the turn); the scrolls are inventory items (Neris: Neutralize Poison, Delay Poison; Iulia: Neutralize Poison x2, Cure Light Injury); look for a Potion of Antivenom in each month's stock (Class II for Lucilla, Rulings S11; scrolls written to order, Rulings S32).
- Brennus' Order contract: Cnaeus Lento (Fighter 3, a sellsword), due by day 540, commission 1,500gp; build him with npc.py before the deed.
- Below, the table's choices: R2's heavy goods (two gilded coffins, two great tusks, the small tusks: about 63 stone); R3's bronze door (288 skeletons rising 2d20 a round after 6 rounds; undead are barred by the circles); N's sealed doors (no way in yet); L4's platform beyond L3's slime; F17 (the egg-bulbs wake the Great Teacher in T2); J8 (the incarnation of terror, 12 HD, beyond Smite Undead).
- The Imperial Vanguard: away on a bounty after Irial's funeral, back about day 535; their delves by the JJ abstract method (Rulings S31).
- Escalated lesson [npc-rolls-hidden]: `mortal-wounds` has no --hidden, so an NPC's Mortal Wounds roll through it is open; roll an NPC's d20 and d6 with `roll --hidden` and read the Savage table by hand (JJ: only CON, HD and equipment adjust it).
- Engine notes: the campaign doors table's slab row now matches Rulings S18 (0, two helpers); identification by use assumes deadly combat (use it only in a fight); magic arrows are goods lots; a henchman's morale score is set with `state set ID morale=N` in the fight (Rulings S31).
- Standing instructions from the user are unchanged (party notes; the S10-S28 handoffs in `Playtest/HANDOFF.md`).
