# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 39 · **day 581**, 08:31 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 213304 | 27/32 |  |
| Vestus the Unlikely | Mage 7 | 140867 | 18/18 |  |
| Lucilla | Venturer 8 | 188362 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 41704 | 19/19 |  |
| Brennus | Fighter 8 | 156509 | 29/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 145950 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 65514 | 23/23 |  |
| Tiberius Maro | Crusader 4 | 7370 | 18/18 |  |
| Phaedra | Mage 6 | 61856 | 2/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |

- **Adventure:** A136 Order contract: Gnaeus Sabucius (Vestus) (paid): Vettius (pc), Vestus the Unlikely (pc), Neris (pc); lots 1; monsters 1 (10 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 610; aelia Aelia: 1600 gp/month; next due day 594; tiberius-maro Tiberius Maro: 150 gp/month; next due day 588; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 1; vettius[party] active hp 26/32 init 7 disordered; vestus-the-unlikely[party] active hp 15/18 init 3; neris[party] active hp 21/21 init 6; gnaeus-sabucius[foe] slain hp -7/7 init 1 unconscious; engaged  | NOTE: Vestus the Unlikely: carried from day 533: lot L781 (TT Rod of Elemental Spheres; SOTN p. 135, L781): Rod of Elemental Spheres (L781, identified day 533): sphere of water (120', drowning), earth (boulder from his side), air (10' wind sphere around him), fire (10' sphere within 30'
- **Schedule:** day 582: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 582: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 582: weekly-double-agents Weekly: the turned-hesitant double agents (none now: #5 ran day 568; #2 gone day 484, #3 and #4 ran day 561; the turncoat, the day-484 man, the day-526 man and Pullus hold without rolling); day 582: weekly-watch Weekly: the Watch on the company; day 582: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 582: weekly-hesitant Weekly: one of the hesitant members turns; day 582: weekly-spies Weekly: Vettius' spies planted; day 582: weekly-secret Weekly: the Family's secret of the week; day 582: weekly-hesitant-554 Weekly: the hesitant member who turned betrayer on day 554 sells word; day 583: weekly-teacher Weekly: the Great Teacher, awake and hidden in the Nethercity (fled day 555, 39/53
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 40; read `R/memory.md`; a new session note `Session Log/S40 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad.
- In hand: no adventure open. Day 581, 08:31, Cyfaraun (the Citadel). Nine: PCs Lucilla, Vettius, Brennus, Vestus, Neris, Cotta; henchmen Aelia, Phaedra (bed rest to day 592: count her out of delves), Tiberius Maro (Crusader 4 since day 578; whole; loyalty -1).
- Next: the weekly block on day 582 (write the six week's-secret entries before the roll); the Teacher on 583; the Order on 585; wages before any delve that crosses them.
- The Imperial Vanguard went down for the white apes on day 580: roll their abstract delve (JJ 10; Rulings S31) before the company goes back to M. Nargund's vault holds only horns now (World State, Judge only).
- The Wolf-Spear (L832, Vettius) is unidentified: the Tower can identify it (as L822/L824).
- Engine and driver notes from S39: (1) `camp` does not stop at an encounter it rolls: check `encounter show` after every camp; (2) `level-up --apply` rolls the level loyalty itself: never add `loyalty --trigger level`; (3) `damage --dice 1d4` rolls the dice: do not `roll` first; (4) the fight driver Playtest/tools/s38_trogs.py needs S39_CLOSE=1 so idle melee members close on foes; S39_NATT, S39_FOEARGS, S39_PARTYARGS, S39_MELEE set per fight; (5) `state end` still leaves party combatants active: `state init` before the next `encounter fight`.
