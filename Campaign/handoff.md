# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 48 · **day 743**, 05:46 · **Ruined Imperial Fortress** (wilderness)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Cotta | Explorer 6 | 55955 | 19/19 |  |
| Brennus | Fighter 8 | 173489 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Vettius | Thief 9 | 262012 | 32/32 |  |
| Lucilla | Venturer 9 | 202635 | 41/43 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Neris | Priestess 8 | 164255 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 71481 | 23/23 |  |
| Phaedra | Mage 6 | 72087 | 20/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |
| Vestus the Unlikely | Mage 7 | 153754 | 18/18 |  |
| Ennia Ursa | Explorer 1 | 1158 | 4/4 |  |
| Tiberius Maro | Crusader 5 | 13302 | 19/19 |  |

- **Adventure:** A155 A155 the march to the bugbears' fort (open): Lucilla (pc), Vettius (pc), Brennus (pc), Tiberius Maro (henchman), Cotta (pc), Neris (pc), Aelia (henchman), Phaedra (henchman), Vestus the Unlikely (pc), Ennia Ursa (henchman); lots 23; monsters 3 (8,000 XP); hoards unfound 166
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 790; aelia Aelia: 1600 gp/month; next due day 774; tiberius-maro Tiberius Maro: 400 gp/month; next due day 798; M42 Heavy Infantry: 72 gp/month; next due day 775; M43 Light Infantry: 108 gp/month; next due day 775; M44 Light Cavalry: 120 gp/month; next due day 775; M45 Bowman: 63 gp/month; next due day 775; M46 Crossbowman: 144 gp/month; next due day 775; M52 Heavy Infantry: 24 gp/month; next due day 781; M53 Light Infantry: 42 gp/month; next due day 781; M54 Bowman: 18 gp/month; next due day 781; M55 Crossbowman: 54 gp/month; next due day 781; M56 Light Cavalry: 30 gp/month; next due day 781; ennia-ursa Ennia Ursa: 25 gp/month; next due day 786; o
- **Fight in the combat state:** round 8; lucilla[party] active hp 40/43 init 6 blessed; vettius[party] active hp 32/32 init 6 blessed; brennus[party] active hp 33/35 init 8 blessed,disordered; cotta[party] active hp 19/19 init 8 blessed,disordered; neris[party] active hp 21/21 init 3; aelia[party] active hp 23/23 init 2 blessed; phaedra[party] active hp 20/20 init 2; vestus-the-unlikely[party] active hp 18/18 init 3; ennia-ursa[party] active hp 4/4 init 1; s2[foe] fled hp 13/29 init 1 faltering; c2[foe] slain hp -25/25 init 4 
- **Schedule:** DUE weekly-wharf-betrayer: Weekly: an untraced wharf betrayer sells word (day 743); DUE weekly-watch: Weekly: the Watch on the company (day 743); DUE weekly-hesitant: Weekly: one of the hesitant members turns (day 743); DUE weekly-spies: Weekly: Vettius' spies planted (day 743); DUE weekly-secret: Weekly: the Family's secret of the week (day 743); DUE grey-sisters-vault: The Grey Sisters' vault fee (10gp a month, paid ahead; last paid day 652 to day 742) (day 743); DUE weekly-double-agents: Weekly: the turned-hesitant double agents (none hesitant now: the S&B turncoat, the day-484 man, the day-526 man, Pullus and the day-554 turncoat (turned day 597) hold without rolling) (day 743); DUE weekly-canary: Weekly: Vettius' canary trap for the untraced wharf betrayers (three on day 597) (Rulings S42) (day 743); day 745: fortress-raids Weekly: the bugbears' raids from the fort (K5) and the Impe
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [wage-days] (3 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 49; read `R/memory.md`; a new session note `Session Log/S49 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad. The Judge plays the AI party by the profiles, heuristics and party notes (no party-agent calls). Priya plays Vestus again.
- **In hand: a fight is open.** `Campaign/combat-state.json` is the fight at the Ruined Imperial Fortress (day 743, sunrise, about seven rounds in); read the prep queue's first entry (who is where, hp, morale) before `round-start`. The company is inside the east breach; the tribe's remainder holds the west wall against Tiberius' soldiers at the ford; the central hall holds the drudges, whelps and hoard. Positions are the Judge's (state distance/engage); clear stale engagements (`state disengage`) before charges.
- **First:** the day-743 weekly city block is due and not run: write the six week's-secret entries in World State, then `ACKS_ACK=secret-entries-first acks.sh schedule run --due`.
- Engine findings to watch (judge-notes S47-S48): navigation thrown on road days (void by hand); round-end morale counts sleepers as felled (void); `encounter surprise` omits a monster's own surprise bonus (`--monster-bonus`); leaders' weapon bonuses not modelled; fight helpers must stop on 'not paid' and 'DUE day'.
- Wages: all paid to day 773 or later; `wages show` before any multi-day march (lesson wages-before-split: pay through the expected return plus a month).
- After the fort: Neris' rites in the strongroom (Calefa's boon, Rulings S48); the Legate's patent (Rulings S48); A155's payout at Türos Aster (the farm's hoard and the fort's); the barony (JJ domains); retire `fortress-raids`.
