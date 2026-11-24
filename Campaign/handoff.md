# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 43 · **day 609**, 06:51 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 226202 | 32/32 |  |
| Vestus the Unlikely | Mage 7 | 145918 | 18/18 |  |
| Lucilla | Venturer 8 | 193279 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 46175 | 19/19 |  |
| Brennus | Fighter 8 | 161668 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 152036 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 67749 | 23/23 |  |
| Tiberius Maro | Crusader 4 | 9605 | 18/18 |  |
| Phaedra | Mage 6 | 64516 | 20/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |

- **Adventure:** A141 Order contract: Lucius Caper (Vettius) (paid): Vettius (pc), Phaedra (henchman), Neris (pc); lots 1; monsters 1 (80 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 610; aelia Aelia: 1600 gp/month; next due day 624; tiberius-maro Tiberius Maro: 200 gp/month; next due day 618; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Schedule:** day 610: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 610: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 610: weekly-watch Weekly: the Watch on the company; day 610: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 610: weekly-hesitant Weekly: one of the hesitant members turns; day 610: weekly-spies Weekly: Vettius' spies planted; day 610: weekly-secret Weekly: the Family's secret of the week; day 610: weekly-double-agents Weekly: the turned-hesitant double agents (none hesitant now: the S&B turncoat, the day-484 man, the day-526 man, Pullus and the day-554 turncoat (turned day 597) hold without rolling); day 610: weekly-canary Weekly: Vettius' canary trap for the untraced wharf betrayers (three on day 597) (Rulings S42); day 611: weekly-teacher Weekly: the Great Teacher, awake and hidden in the Nethercity (fled
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 44; read `R/memory.md`; a new session note `Session Log/S44 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad.
- In hand: no adventure open. Day 609, 06:51, Cyfaraun (the Citadel). Nine, whole.
- Next: the weekly block day 610 (six week's-secret entries first; an extra 1-in-6 Watch roll for Galeo's disappearance; the weekly-canary trap); Phaedra's wage 610 (Vettius); the Teacher 611 (whole again; watching the Citadel); the Order 613.
- The user's direction (S42, clarified): Vettius turns the betrayers he can and kills those he cannot (Rulings S42).
- Below: L4 (the cave of the shining floor beyond L3's 40' of slime and sludge): the company believes it the magic rock; stepping in teleports everyone in the cave to the Istrith Forest platform (SOTN L4; fix the hex at first use). M8's mummy warlords and M9; two ancient dragon horns in Nargund's vault.
- Engine notes: remove Campaign/combat-state.json outside fights (throws refuse otherwise); check `encounter show` after every `camp`; `level-up --apply` rolls the level loyalty itself; `damage --dice` rolls its own dice; the driver Playtest/tools/s38_trogs.py with S39_CLOSE=1; `state init` before each `encounter fight`; `play.py walk` does not relight a burned-out lantern; recover magic items as `--item`; close an Order contract's adventure (commission paid) before starting a descent.
