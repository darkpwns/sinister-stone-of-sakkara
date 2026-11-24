# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 53 · **day 829**, 08:39 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Cotta | Explorer 7 | 67409 | 20/20 |  |
| Brennus | Fighter 8 | 185516 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 10 | 286205 | 34/34 |  |
| Lucilla | Venturer 9 | 215234 | 43/43 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Neris | Priestess 8 | 175709 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 77207 | 23/23 |  |
| Phaedra | Mage 6 | 77813 | 20/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |
| Ennia Ursa | Explorer 3 | 5618 | 9/9 |  |
| Vestus the Unlikely | Mage 8 | 165627 | 19/19 |  |

- **Adventure:** A159 A159 the road north (paid): Cotta (pc), Brennus (pc), Vettius (pc), Lucilla (pc), Neris (pc), Vestus the Unlikely (pc), Aelia (henchman), Phaedra (henchman), Ennia Ursa (henchman); lots 4; monsters 0 (0 XP); hoards unfound 165
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 880; aelia Aelia: 1600 gp/month; next due day 894; tiberius-maro Tiberius Maro: 400 gp/month; next due day 888; M42 Heavy Infantry: 72 gp/month; next due day 895; M43 Light Infantry: 96 gp/month; next due day 895; M44 Light Cavalry: 120 gp/month; next due day 895; M45 Bowman: 63 gp/month; next due day 895; M46 Crossbowman: 144 gp/month; next due day 895; M52 Heavy Infantry: 24 gp/month; next due day 901; M53 Light Infantry: 42 gp/month; next due day 901; M54 Bowman: 18 gp/month; next due day 901; M55 Crossbowman: 54 gp/month; next due day 901; M56 Light Cavalry: 30 gp/month; next due day 901; ennia-ursa Ennia Ursa: 100 gp/month; next due day 876; S
- **Schedule:** day 831: ram-moves-on-pony Night of day 831: the Gilded Ram's men, the usurper's street gangs and Sigvald's forty Jutlanders move on the Silk Pony (Bassus and his knives, crossbows; Thana inside); day 833: grey-sisters-vault The Grey Sisters' vault fee (10gp a month, paid ahead; last paid day 743 to day 832); day 834: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 834: weekly-watch Weekly: the Watch on the company; day 834: weekly-hesitant Weekly: one of the hesitant members turns; day 834: weekly-spies Weekly: Vettius' spies planted; day 834: weekly-secret Weekly: the Family's secret of the week; day 834: weekly-double-agents Weekly: the turned-hesitant double agents (none hesitant now: the S&B turncoat, the day-484 man, the day-526 man, Pullus and the day-554 turncoat (turned day 597) hold without rolling); day 834: weekly-canary Weekly: Vettius' canary trap f
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [wage-days] (3 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 54; read `R/memory.md`; a new session note `Session Log/S54 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad. The Judge plays the AI party by the profiles, heuristics and party notes (no party-agent calls). Priya plays Vestus.
- **In hand:** day 829, evening, the Silk Pony, Cyfaraun (settlement; the fifteen animals stabled there; the nine fatigued until a day's rest). S53: the ride north (A159 paid: three brilliants and a sword found on the road), Lucan Vesper of the Tower met on the road (the Regent wants the legion's gate), Vettius and Thana betrothed (user's direction), the spies' warning.
- **Next: the night of day 831** (schedule `ram-moves-on-pony`): the Gilded Ram's bravos, Lentulus Mordax's gangs and Sigvald's forty Jutlanders come at the Pony. Build the attackers before it (prep queue); play the company's plan (session log S53, Next time). Then Mordax's gangs choose; the wedding; selling through the Family; the Tower's library about the gate.
- **The user's directions (S53):** Vettius weds Thana (betrothed day 829; wedding at the Grey Sisters, Neris officiating); the party wants a way to join Cyfaraun and the fort: the Legion Waygate (Adventure/Legion Waygate.md, Rulings S53), learned through the Tower and the road; the tesserae lie in the Ruined Monastery's cache (prep it with them).
- **Bookkeeping on the road** (Rulings S53): feed for the non-grazing animals each evening (2sp a stone), water at wells; check `supplies show` daily (standard rations spoil in the wild); undo `supplies show --on ANIMAL` before stabling.
- Engine findings S53 (judge-notes): rest does not clear spells_used (S52); `--hex` override applies only to the named hex; `recover --lots` is 0-indexed; `supplies show --on` blocks `inv stable`.
