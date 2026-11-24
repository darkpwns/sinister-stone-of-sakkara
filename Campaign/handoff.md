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
- **The table's direction (user, end of S43): the company hunts the Great Teacher.** Before the first hunt, fix by hidden rolls (Judge only) where he lairs now, how he comes and goes, who holds his canister (L825), and what each lead yields; the World State prep queue lists the leads and candidates (the troglodyte caves and the shaman of I13; the old lizard-men's wharf and tunnel; his old sepulchre T; the Undercity under the Citadel). The party's plan is in Party/party-notes.md (S43 plan): spies on the wharf and the roofs, a night trap on the Citadel's roof, Neris' divinations, the third eyes' telepathy, Cotta's tracking below. Statblock: Adventure/SOTN/Bestiary/Great Teacher (SOTN).md (53 hp, whole; scrambler 3 charges; flees by Arcane Shift rather than die). No XP until he is destroyed, captured or outsmarted for good (Rulings S36).
- Next on the calendar: the weekly block day 610 (six week's-secret entries first: put the Teacher leads among them; an extra 1-in-6 Watch roll for Galeo's disappearance; the weekly-canary trap for three wharf betrayers); Phaedra's wage 610 (Vettius); the Teacher's weekly roll 611 (a 1 is a move against the company); the Order 613; barge 616; Tiberius' wage 617; vault and Aelia 623; month 21 ends day 630.
- The user's direction (S42, clarified): Vettius turns the betrayers he can and kills those he cannot (Rulings S42).
- Below, besides the Teacher: L4 (the cave of the shining floor beyond L3's slime and sludge, the magic rock: everyone who steps in goes to the Istrith Forest platform; fix the hex at first use); M8's mummy warlords and M9; two ancient dragon horns in Nargund's vault. Four Watch officers have vanished since day 557.
- Engine notes: remove Campaign/combat-state.json outside fights (throws refuse otherwise); check `encounter show` after every `camp`; `level-up --apply` rolls the level loyalty itself; `damage --dice` rolls its own dice; the driver Playtest/tools/s38_trogs.py with S39_CLOSE=1; `state init` before each `encounter fight`; `play.py walk` does not relight a burned-out lantern; recover magic items as `--item`; close an Order contract's adventure (commission paid) before starting a descent.
