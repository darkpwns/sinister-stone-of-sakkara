# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 41 · **day 595**, 07:11 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 214106 | 32/32 |  |
| Vestus the Unlikely | Mage 7 | 141669 | 18/18 |  |
| Lucilla | Venturer 8 | 188828 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 42128 | 19/19 |  |
| Brennus | Fighter 8 | 156954 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 146714 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 65726 | 23/23 |  |
| Tiberius Maro | Crusader 4 | 7582 | 18/18 |  |
| Phaedra | Mage 6 | 61856 | 6/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |

- **Adventure:** A138 Order contract: Theron Askalaios (Vestus) (paid): Vettius (pc), Vestus the Unlikely (pc), Neris (pc); lots 1; monsters 1 (20 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 610; aelia Aelia: 1600 gp/month; next due day 624; tiberius-maro Tiberius Maro: 200 gp/month; next due day 618; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 0; vettius[party] active hp 32/32 init None; vestus-the-unlikely[party] active hp 18/18 init None; neris[party] active hp 21/21 init None; theron-askalaios[foe] dead hp -11/4 init None surprised,unconscious; engaged  | NOTE: Vestus the Unlikely: carried from day 533: lot L781 (TT Rod of Elemental Spheres; SOTN p. 135, L781): Rod of Elemental Spheres (L781, identified day 533): sphere of water (120', drowning), earth (boulder from his side), air (10' wind sphere around him), fire (10' spher
- **Schedule:** day 596: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 596: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 596: weekly-double-agents Weekly: the turned-hesitant double agents (none now: #5 ran day 568; #2 gone day 484, #3 and #4 ran day 561; the turncoat, the day-484 man, the day-526 man and Pullus hold without rolling); day 596: weekly-watch Weekly: the Watch on the company; day 596: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 596: weekly-hesitant Weekly: one of the hesitant members turns; day 596: weekly-spies Weekly: Vettius' spies planted; day 596: weekly-secret Weekly: the Family's secret of the week; day 596: weekly-hesitant-554 Weekly: the hesitant member who turned betrayer on day 554 sells word; day 597: weekly-teacher Weekly: the Great Teacher, awake and hidden in the Nethercity (fled day 555, 39/53
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 42; read `R/memory.md`; a new session note `Session Log/S42 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad.
- In hand: no adventure open. Day 595, 07:11, Cyfaraun (the Citadel). Nine, whole: PCs Lucilla, Vettius, Brennus, Vestus, Neris, Cotta; henchmen Aelia, Phaedra (up), Tiberius Maro (Crusader 4).
- Next: the weekly block day 596 (six week's-secret entries first); the Teacher day 597 (he knows the company's lodging and habits: a 1 is a move against them); the Order day 599; month 20 ends day 600 (the schedule's month-end steps; take less Calvus 4th and the day-540 turncoat 0th; research XP for Vestus' scroll; the Captain's monthly report: Tiberius has not made it this month); month 21's selling day: the Wolf-Spear L832 through the Family (its true value is in adventure-state).
- Below: the magic rock (L4) in the ant caves; the shaman is the Teacher's. M8's mummy warlords and M9; two ancient dragon horns in Nargund's vault. The Vanguard abed to about day 611.
- Engine notes: check `encounter show` after every `camp`; `level-up --apply` rolls the level loyalty itself; `damage --dice 1d4` rolls its own dice; the driver Playtest/tools/s38_trogs.py with S39_CLOSE=1; `state init` before each `encounter fight`; `play.py walk` does not relight a burned-out lantern; `identify` refuses goods lots (identify by hand).
