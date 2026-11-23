# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 35 · **day 540**, 06:14 · **Cyfaraun** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Vettius | Thief 9 | 197971 | 32/32 |  |
| Vestus the Unlikely | Mage 7 | 132761 | 18/18 |  |
| Lucilla | Venturer 8 | 180706 | 42/42 | minor scarring (fang mark on the hand); wears a Ring of Fire Protection (L63, identified day 195); third eye in the forehead (Tampering with Mortality, day 243) |
| Cotta | Explorer 6 | 35187 | 19/19 |  |
| Brennus | Fighter 8 | 148288 | 35/35 | nose flattened, cheek crushed, ear cauliflowered (gruesome scarring); made a woman by the gods (Tampering with Mortality, day 247): -2 to reaction rolls with th |
| Neris | Priestess 8 | 138801 | 21/21 | a vision of terrible import (Tampering with Mortality, day 246): the beetle-faced teacher asleep in the cold below the black river; a priestess of Calefa, the L |
| Aelia | Bard 7 | 62256 | 23/23 |  |
| Phaedra | Mage 6 | 58341 | 20/20 | critically wounded (Mortal Wounds, day 517): one foot lost to frostbite (peg required, movement reduced by 30', DEX reduced by 1/3 for AC purposes); 1 week of b |
| Hrodvar | Dwarven Vaultguard 6 | 43513 | 19/19 | notable scarring: his cheek marred by the scars of great claws and fangs (Mortal Wounds, day 423); intestines mangled and ruined (Mortal Wounds, day 499): must  |
| Tiberius Maro | Crusader 3 | 4112 | 12/12 |  |

- **Adventure:** A127 Order contract: Faustus Cerco (Vettius) (paid): Vettius (pc); lots 1; monsters 1 (10 XP); hoards unfound 114
- **Wages:** phaedra Phaedra: 800 gp/month; next due day 550; aelia Aelia: 1600 gp/month; next due day 564; hrodvar Hrodvar: 800 gp/month; next due day 553; tiberius-maro Tiberius Maro: 150 gp/month; next due day 558; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 0; vettius[party] active hp 32/32 init None; faustus-cerco[foe] dead hp -10/3 init None asleep,dead,unconscious; engaged
- **Schedule:** day 543: order-roll The Order of the Eclipse's weekly assignment roll; day 545: vettius-hideout-followers Vettius' Hideout followers arrive at the Silk Pony: 8 1st-level thieves (2d6 8; within 1d4 4 weeks of day 520: day 545); one is an infiltrator for the Brotherhood (1d6 6; no second: 4); day 547: weekly-brotherhood Weekly: someone seeks the Brotherhood; day 547: weekly-wharf-betrayer Weekly: an untraced wharf betrayer sells word; day 547: weekly-double-agents Weekly: the turned-hesitant double agents #3 and #4 (#2 gone day 484; the turncoat and the day-484 man hold without rolling); day 547: weekly-watch Weekly: the Watch on the company; day 547: weekly-city-link Weekly: the city links the Captain's deed and the new guild; day 547: weekly-hesitant Weekly: one of the hesitant members turns; day 547: weekly-spies Weekly: Vettius' spies planted; day 547: weekly-secret Weekly: the Family'
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [surprise-members] (1 slip): slipped on although enforced: the enforcement has a hole
  - ESCALATE [npc-rolls-hidden] (1 slip): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- Start: set Campaign State `session:` to 36; read `R/memory.md`; a new session note `Session Log/S36 — <summary>.md`, linked in the Campaign Log.
- In hand: no adventure open. Day 540 morning, the Solar Citadel (lodging by the Captain's privilege again: Rulings S35). Ten: PCs Lucilla, Vettius, Brennus, Vestus, Neris, Cotta; henchmen Aelia (Lucilla's), Phaedra (Vettius'; foot restored by Arëtar day 540, abed to day 554, a third eye), Hrodvar (Vettius'; gut healed by Arëtar day 540: no extra rest any more; 10% penalty on earned XP to his next level), Tiberius Maro (Vettius'; Crusader 3; Captain of the Underwatch).
- Tiberius bears the Underwatch shield and spear as stand-ins in the inventory (a mundane Shield and Spear: the engine refused to re-claim L232/L233, whose instances were removed at Iulia's death; S35 finding) with `actor mod` lines: ac.shield +1 and notes for the spear (+2 by hand, `--magic`) and the ward. In a fight: `state ward add tiberius-maro --name "the Underwatch shield" --radius 10 --within party --evil foes --fall creature --source "Rulings S14, S35"`. Attacking from inside drops the ward against that foe (it happened on day 535). The Rod of the Dawn (L203) is lent to him; its use is by hand as before.
- Next: month 19's selling day (L786, the golden-skull shrine, through the Family); the Order (day 543); Vettius' Hideout followers (day 545, one a Brotherhood infiltrator); barge fee (day 546); the Tower's identification of the soul gem L805 (day 547: reveal it as SOTN's large soul gem, Caogan inside); weekly block 547 (write the six secrets first; the day-540 turncoat's own roll; the officer's suspicion extra 1-in-6).
- Judge's watch: Gaius Sertorius Macro (wants the Captain dead; his name in the Codex): a contract on him may come at an Order roll; his brother the knight resents the appointment.
- Below, by the company's knowledge: N and O are empty. F17's cases (the egg-bulbs wake the Great Teacher), J8's throne (the incarnation of terror), L4's platform. The party's next delve target is the table's choice.
- Lesson [surprise-members] is now a refusal (S35 escalation): pass --members to every `encounter surprise`.
- The combat state and `throw`/`save` refuse a non-combatant when a combat state exists: `state init` and `state add` first (or run them inside a fight).
