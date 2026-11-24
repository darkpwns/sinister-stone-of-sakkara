# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 44 · **day 614**, 05:15 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 229171 | 32/32 |  |
| Vestus the Unlikely | Mage 7 | 148887 | 18/18 |  |
| Lucilla | Venturer 8 | 196390 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 49003 | 19/19 |  |
| Brennus | Fighter 8 | 164637 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 154864 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 69163 | 23/23 |  |
| Tiberius Maro | Crusader 4 | 11019 | 18/18 |  |
| Phaedra | Mage 6 | 65930 | 20/20 | You grow an alien eye on the center of your forehead. The eye stays lidded most of the time. Three times per day you may unlid the eye and use the telepathy spe |

- **Adventure:** A143 A143 the drowned cellar under the Citadel: the Teacher (paid): Vettius (pc), Vestus the Unlikely (pc), Lucilla (pc), Cotta (pc), Brennus (pc), Neris (pc), Aelia (henchman), Tiberius Maro (henchman), Phaedra (henchman); lots 5; monsters 1 (5,000 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 640; aelia Aelia: 1600 gp/month; next due day 624; tiberius-maro Tiberius Maro: 200 gp/month; next due day 618; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Schedule:** day 616: barge-mooring Tertulla's mooring fee for the black barge (2gp a week, paid a fortnight ahead; paid to day 615); day 617: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 617: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 617: weekly-watch Weekly: the Watch on the company; day 617: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 617: weekly-hesitant Weekly: one of the hesitant members turns; day 617: weekly-spies Weekly: Vettius' spies planted; day 617: weekly-secret Weekly: the Family's secret of the week; day 617: weekly-double-agents Weekly: the turned-hesitant double agents (none hesitant now: the S&B turncoat, the day-484 man, the day-526 man, Pullus and the day-554 turncoat (turned day 597) hold without rolling); day 617: weekly-canary Weekly: Vettius' canary trap for the untraced wharf betrayers (thr
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [driver-loop-stop] (1 slip): prose only and slipped on: give it a trigger (remind or refuse)
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 45; read `R/memory.md`; a new session note `Session Log/S45 — <summary>.md`, linked in the Campaign Log; set `party.agent.call_dir` to the new chat's scratchpad.
- In hand: no adventure open. Day 614 before dawn, Cyfaraun (the Citadel), just up from the drowned cellar. **The Great Teacher is destroyed** (A143 paid; Rulings S36 satisfied; weekly-teacher retired). His goods: L861 the scrambler (empty), L862 his arcane sword (identified), L863 the silkweave suit, L864 two anagathics, L865 a healing syringe (L863-L865 unidentified: the Tower can name them), L866 robe and jewelled belt (15,000gp). Selling through the Family on month 22's selling day (Rulings S19) gives sale XP to A143's holders for identified, unused items; the company may keep some (the suit for Vettius, the anagathics).
- Oppius brings four Order contracts on day 614 (World State day 614; notes in Adventure/AX3/NPCs): roll each target's habits when the company first watches.
- The troglodyte shaman (I13) is free and will guide the company to L4 when it brings gifts for her tribe; fix the Istrith hex at first use of L4. Energy crystals: 28 in H14's ceiling stars (SOTN) could charge L861 and the hilts.
- The Regent Aurëus holds the canister (L825) and is cold to Vestus (-1 next reaction). Tiberius owes Arëtar the month-21 report: the herald of the Awakening is dead under the Citadel's own catacombs (Judge's call on Arëtar's reaction and on the drowned cellar's door).
- Calendar: barge 616; the weekly block 617 (six week's-secret entries first; canary: three untraced wharf men, two of whom sold days 612-613); Tiberius 618; Order 620; vault and Aelia 623; month 21 ends 630.
- Engine notes: do not declare a monster's spell-like power as a spell in `round-start` (it gets marked disrupted); `rest N` for waiting, not `turn N`; Playtest/tools/s44_trogs.py drives mass melee with front-line engagement (S44_FRONT, S44_CAP, BREEDER_PREFIX); remove Campaign/combat-state.json outside fights.
