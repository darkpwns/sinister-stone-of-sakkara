# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 52 · **day 817**, 06:00 · **Turos Aster** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Cotta | Explorer 7 | 65454 | 20/20 |  |
| Brennus | Fighter 8 | 183463 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 10 | 284152 | 34/34 |  |
| Lucilla | Venturer 9 | 213084 | 43/43 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Neris | Priestess 8 | 173754 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 76230 | 23/23 |  |
| Phaedra | Mage 6 | 76836 | 20/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |
| Ennia Ursa | Explorer 3 | 4641 | 9/9 |  |
| Vestus the Unlikely | Mage 8 | 163574 | 19/19 |  |
| Tiberius Maro | Crusader 5 | 17978 | 19/19 |  |

- **Adventure:** A158 A158 the stone sisters' cave (paid): Cotta (pc), Brennus (pc), Vettius (pc), Lucilla (pc), Neris (pc), Vestus the Unlikely (pc), Aelia (henchman), Phaedra (henchman), Ennia Ursa (henchman), Tiberius Maro (henchman); lots 11; monsters 2 (735 XP); hoards unfound 165
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 880; aelia Aelia: 1600 gp/month; next due day 894; tiberius-maro Tiberius Maro: 400 gp/month; next due day 888; M42 Heavy Infantry: 72 gp/month; next due day 895; M43 Light Infantry: 96 gp/month; next due day 895; M44 Light Cavalry: 120 gp/month; next due day 895; M45 Bowman: 63 gp/month; next due day 895; M46 Crossbowman: 144 gp/month; next due day 895; M52 Heavy Infantry: 24 gp/month; next due day 901; M53 Light Infantry: 42 gp/month; next due day 901; M54 Bowman: 18 gp/month; next due day 901; M55 Crossbowman: 54 gp/month; next due day 901; M56 Light Cavalry: 30 gp/month; next due day 901; ennia-ursa Ennia Ursa: 100 gp/month; next due day 876; S
- **Schedule:** day 820: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 820: weekly-watch Weekly: the Watch on the company; day 820: weekly-hesitant Weekly: one of the hesitant members turns; day 820: weekly-spies Weekly: Vettius' spies planted; day 820: weekly-secret Weekly: the Family's secret of the week; day 820: weekly-double-agents Weekly: the turned-hesitant double agents (none hesitant now: the S&B turncoat, the day-484 man, the day-526 man, Pullus and the day-554 turncoat (turned day 597) hold without rolling); day 820: weekly-canary Weekly: Vettius' canary trap for the untraced wharf betrayers (three on day 597) (Rulings S42); day 823: jutland-company-north Sigvald's Jutland company (40) reaches Cyfaraun and reports to the Gilded Ram's owner (refused at the ford day 817)
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [wage-days] (3 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 53; read `R/memory.md`; a new session note `Session Log/S53 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad. The Judge plays the AI party by the profiles, heuristics and party notes (no party-agent calls). Priya plays Vestus.
- **In hand:** day 817, evening, Türos Aster / the fort (settlement). S52: rations and wages; the stone sisters' cave cleared (A158 paid); the barony's first domain month (Rulings S52 rows: revenue, garrison, expenses, base morale +1, morale roll, population, no prestige while the stronghold is insufficient, administering); Thana's news (Pullus' old lieutenant made himself boss of the street; the take stopped); Sigvald's Jutland company refused at the ford (false oath under Discern Evil) and gone north to the Ram.
- **The council's decision (day 817): ride north to Cyfaraun at dawn of day 818** with nine (Tiberius holds the fort with the soldiers): retake the street, see Thana, sell the dragon's blood and the medusae's parts through the Family, collect Lucilla's caravan returns, hire more laborers. Wages are paid ahead to the autumn; grain for soldiers and workmen to day 878.
- **Before riding:** `party remove tiberius-maro --stays "the fort of the Ford"`; unstable the animals at the Legate's stables (fee owed per night since day 743); road food for nine (fort-stores standard rations, inns along the road); `travel-init`, the Imperial road (void navigation on road days by hand).
- **Prep before Cyfaraun (Judge only, prep queue):** the usurper's strength and the Ram's response once the Jutlanders arrive (schedule `jutland-company-north`, day 823); the weekly city block (six entries first).
- **Not yet prepped:** the Ruined Monastery (31.17, H218 TT K): prep by R/unprepped-sites.md before the party goes.
- Engine findings S52 (judge-notes): actors' spells_used not cleared by rest-day/wait; `encounter start --wild --hex` overrides only the named hex while the table comes from the travel hex; `recover --lots` is 0-indexed; the month-end item lacked Rulings S46's usurpation roll (added).
