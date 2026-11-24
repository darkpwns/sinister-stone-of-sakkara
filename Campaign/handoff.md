# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 38 · **day 574**, 09:34 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 209954 | 30/32 |  |
| Vestus the Unlikely | Mage 7 | 137517 | 11/18 |  |
| Lucilla | Venturer 8 | 185039 | 40/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 38683 | 16/19 |  |
| Brennus | Fighter 8 | 153337 | 32/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 142759 | 15/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 64003 | 18/23 |  |
| Tiberius Maro | Crusader 3 | 5859 | 5/5 |  |
| Phaedra | Mage 6 | 60744 | 12/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |

- **Adventure:** A133 Descent 80 (the doom throne, J8) (paid): Lucilla (pc), Vettius (pc), Brennus (pc), Vestus the Unlikely (pc), Neris (pc), Cotta (pc), Aelia (henchman), Phaedra (henchman), Tiberius Maro (henchman); lots 2; monsters 3 (4,100 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 580; aelia Aelia: 1600 gp/month; next due day 594; tiberius-maro Tiberius Maro: 150 gp/month; next due day 588; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 0; engaged
- **Schedule:** day 575: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 575: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 575: weekly-double-agents Weekly: the turned-hesitant double agents (none now: #5 ran day 568; #2 gone day 484, #3 and #4 ran day 561; the turncoat, the day-484 man, the day-526 man and Pullus hold without rolling); day 575: weekly-watch Weekly: the Watch on the company; day 575: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 575: weekly-hesitant Weekly: one of the hesitant members turns; day 575: weekly-spies Weekly: Vettius' spies planted; day 575: weekly-secret Weekly: the Family's secret of the week; day 575: weekly-hesitant-540 Weekly: the hesitant member who turned betrayer on day 540 sells word; day 575: weekly-hesitant-554 Weekly: the hesitant member who turned betrayer on day 554 sells word; day 57
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 39; read `R/memory.md`; a new session note `Session Log/S39 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad.
- In hand: no adventure open. Day 574, ~09:40, Cyfaraun (the company lodges at the Citadel with the Captain). Nine: PCs Lucilla, Vettius, Brennus, Vestus, Neris, Cotta; henchmen Aelia (Lucilla's), Phaedra (Vettius'), Tiberius Maro (Vettius'; Captain of the Underwatch; enervation ended day 570, but his maximum hp stays reduced until ritual magic or a level gained: Rulings S20; loyalty -2). Wounded members heal in town; spells used on day 574 return at the next rest.
- Next in the city: the weekly block on day 575 (write the six week's-secret entries before the roll); the Teacher's roll on day 576; the Order on day 578; wages before any delve that crosses them (Phaedra's falls first). Nuvicus' accusation failed (Rulings S38): the Prefect's man, Sextus Aufidius Lenas (no note yet), holds the apothecary's record of Nuvicus' poisons (Judge's watch).
- Below: J is spent. Open: L4's platform (the shaman may be the Teacher's now), M (white apes), R (the stair at the Y), the K galleries; the Teacher's servants (the I7 band is dead; 4 skeletons fled in G). The standing instruction wants multi-day expeditions with nights below in sealed rooms: plan the next descent so.
- Engine notes from S38: (1) `state end` leaves party combatants active, and `encounter fight` then refuses until `state init` (judge-notes S38); (2) `encounter surprise` with no --party/--monsters reads both sides blind: pass them; (3) a statline's own damage dice (SOTN breeders 1d2) cannot be set: the S38 driver corrects by hand; (4) the ward's +1 to saves against an evil source is printed as a note, not applied: add it as a named --mod; (5) new lesson [hands-before-delve] fires on `adventure start`.
