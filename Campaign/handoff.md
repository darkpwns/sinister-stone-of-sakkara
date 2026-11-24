# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 35 · **day 555**, 05:14 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 197971 | 32/32 |  |
| Vestus the Unlikely | Mage 7 | 132761 | 18/18 |  |
| Lucilla | Venturer 8 | 180706 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 35187 | 19/19 |  |
| Brennus | Fighter 8 | 148288 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 138801 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 62256 | 23/23 |  |
| Hrodvar | Dwarven Vaultguard 6 | 43513 | 19/19 | notable scarring: his cheek marred by the scars of great claws and fangs (Mortal Wounds, day 423); Your brush with death has shattered your former confidence: 1 |
| Tiberius Maro | Crusader 3 | 4112 | 12/12 |  |
| Phaedra | Mage 6 | 58341 | 20/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |

- **Adventure:** A127 Order contract: Faustus Cerco (Vettius) (paid): Vettius (pc); lots 1; monsters 1 (10 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 580; aelia Aelia: 1600 gp/month; next due day 594; hrodvar Hrodvar: 800 gp/month; next due day 583; tiberius-maro Tiberius Maro: 150 gp/month; next due day 588; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 0; vestus-the-unlikely[party] active hp 18/18 init None; engaged  | NOTE: Vestus the Unlikely: carried from day 533: lot L781 (TT Rod of Elemental Spheres; SOTN p. 135, L781): Rod of Elemental Spheres (L781, identified day 533): sphere of water (120', drowning), earth (boulder from his side), air (10' wind sphere around him), fire (10' sphere within 30', moved 20'/round); each once a day by its command word (none inside silence, Rulings S34); concentration
- **Schedule:** day 557: order-roll The Order of the Eclipse's weekly assignment roll; day 560: barge-mooring Tertulla's mooring fee for the black barge (2gp a week, paid a fortnight ahead; paid to day 559); day 561: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 561: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 561: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 561: weekly-watch Weekly: the Watch on the company; day 561: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 561: weekly-hesitant Weekly: one of the hesitant members turns; day 561: weekly-spies Weekly: Vettius' spies planted; day 561: weekly-secret Weekly: the Family's secret of the week; day 561: weekly-hesitant-540 Weekly: the hesitant member who turned betrayer o
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 36; read `R/memory.md`; a new session note `Session Log/S36 — <summary>.md`, linked in the Campaign Log.
- In hand: no adventure open. Day 555, 05:14, the Solar Citadel (the Captain's lodging, Rulings S35). Ten at full strength and provisioned (a week's iron rations each): PCs Lucilla, Vettius, Brennus, Vestus, Neris, Cotta; henchmen Aelia (Lucilla's), Phaedra (Vettius'; foot restored day 540, third eye), Hrodvar (Vettius'; healed day 540; 10% XP penalty to his next level; carries the tomb-jacks), Tiberius Maro (Vettius'; Crusader 3; Captain of the Underwatch). Wages for the delve are paid ahead.
- The table's next choice is the delve target; the company's knowledge after Caogan's answers is in the party notes (F17's lever, the cases and the Teacher; J8's throne; L4's platform).
- Tiberius bears the Underwatch shield and spear as stand-ins (inventory refused to re-claim L232/L233): `actor mod` lines carry ac.shield +1 and notes; the spear's +2 is applied by hand with `--magic`. In a fight: `state ward add tiberius-maro --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14, S35"`. Attacking from inside drops it against that foe.
- Hrodvar's tomb-jacks (Rulings S35): a turn to set, +2 to a heave on slabs, lids and lifting stone doors (lesson [tomb-jacks] reminds on `explore force-door --door-kind`).
- The soul gem L805 (Neris; 3,000 divine power left): pays research components or casts repertoire spells without slots (50/100/150/225 by level); Calefa's stricture: break it to free Caogan when spent or when the work below is done, else disfavor from a month's end (Rulings S35). Its power level is kept in the lot's player record and World State, not the engine.
- Magic research is by lookup (RR Magic Research; the engine does not run it): material at the start, components at the end, research rate per day, the throw at the end; the Tower's workshop is shared (crowding 1d3 per project), the Grey Sisters' scriptorium +1 for 4th-level divine scrolls. Month 19's end (day 570): Vestus 600 research XP.
- Next scheduled: the Order day 557; barge 560; weekly 561 (the day-554 turncoat's first roll); vault fee 563; month's end 570.
- Lessons now in force from S35: [surprise-members] is a refusal; [lasting-wounds-in-town] reminds on `wait` in Cyfaraun when a disabling wound is carried; [tomb-jacks].
