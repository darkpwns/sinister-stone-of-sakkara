# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 40 · **day 588**, 06:11 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 213749 | 32/32 |  |
| Vestus the Unlikely | Mage 7 | 141312 | 18/18 |  |
| Lucilla | Venturer 8 | 188828 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 42128 | 19/19 |  |
| Brennus | Fighter 8 | 156954 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 146374 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 65726 | 23/23 |  |
| Tiberius Maro | Crusader 4 | 7582 | 18/18 |  |

- **Adventure:** A137 Descent 83 (the horns of Nargund's vault; the old ape) (paid): Lucilla (pc), Vettius (pc), Brennus (pc), Vestus the Unlikely (pc), Neris (pc), Cotta (pc), Aelia (henchman), Tiberius Maro (henchman); lots 7; monsters 1 (245 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 610; aelia Aelia: 1600 gp/month; next due day 594; tiberius-maro Tiberius Maro: 200 gp/month; next due day 618; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 1; vettius[party] active hp 30/32 init 2; vestus-the-unlikely[party] active hp 18/18 init 5; lucilla[party] active hp 42/42 init 2; cotta[party] active hp 19/19 init 5 surprised; brennus[party] active hp 35/35 init 8; neris[party] active hp 21/21 init 3; aelia[party] active hp 23/23 init 6; tiberius-maro[party] active hp 18/18 init 1 surprised; phaedra[party] left hp 2/20 init 4; gelatinous-mass1[foe] slain hp -26/13 init 4; engaged ; ward: the Underwatch shield (tiberius-maro) (Rulings S1
- **Schedule:** day 589: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 589: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 589: weekly-double-agents Weekly: the turned-hesitant double agents (none now: #5 ran day 568; #2 gone day 484, #3 and #4 ran day 561; the turncoat, the day-484 man, the day-526 man and Pullus hold without rolling); day 589: weekly-watch Weekly: the Watch on the company; day 589: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 589: weekly-hesitant Weekly: one of the hesitant members turns; day 589: weekly-spies Weekly: Vettius' spies planted; day 589: weekly-secret Weekly: the Family's secret of the week; day 589: weekly-hesitant-554 Weekly: the hesitant member who turned betrayer on day 554 sells word; day 590: weekly-teacher Weekly: the Great Teacher, awake and hidden in the Nethercity (fled day 555, 39/53
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 41; read `R/memory.md`; a new session note `Session Log/S41 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad.
- In hand: no adventure open. Day 588, 06:11, Cyfaraun (the Citadel). Nine: PCs Lucilla, Vettius, Brennus, Vestus (research to day 590), Neris, Cotta; henchmen Aelia, Phaedra (bed rest to day 592; on the roster as staying in Cyfaraun: `party add` her back when she rises), Tiberius Maro (Crusader 4, 200gp a month).
- Next: the weekly block day 589 (six week's-secret entries first); the Teacher 590; Vestus' scroll 591 (schedule item); the Order 592; Aelia's wage 594; the spear's identification 595; month 20 ends 600; Theron Askalaios' contract (Vestus) due by 600 (warded room, friends in the evenings, a rook: plan it).
- Below: the magic rock (L4) in the ant caves; M8's mummy warlords and M9; two ancient dragon horns in Nargund's vault. The Vanguard is abed.
- Engine notes (S39-S40): check `encounter show` after every `camp`; `level-up --apply` rolls the level loyalty itself; `damage --dice 1d4` rolls its own dice; the fight driver Playtest/tools/s38_trogs.py with S39_CLOSE=1; `state init` before each `encounter fight`; `play.py walk` does not relight a burned-out lantern; a member left in town: `party remove ID --stays Cyfaraun`.
