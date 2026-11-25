# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 9 · **day 66**, 17:35 · **Turos Tem** (settlement)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 2 | 3571 | 7/7 |  |
| Faustina | Priestess 2 | 3408 | 10/10 |  |
| Callista | Mage 2 | 3408 | 6/6 |  |
| Corvus | Explorer 2 | 3408 | 8/8 |  |
| Marius | None (0th level) 0 | 177 | 4/4 |  |
| Varro | Crusader 1 | 104 | 3/3 |  |
| Hrodric | Shaman 2 | 2999 | 7/7 |  |
| Severina | Venturer 1 | 567 | 7/7 |  |
| Petra | None (0th level) 0 | 0 | 3/3 |  |
| Titus | None (0th level) 0 | 0 | 3/3 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35)
- **Adventure:** A5 The hobgoblins' alliance (Buried Temple, level 1) (paid): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Marius (henchman), Varro (henchman); lots 5; monsters 1 (60 XP); hoards unfound 0
- **Wages:** marius Marius: 12 gp/month; next due day 121; petra Petra: 12 gp/month; next due day 98; titus Titus: 12 gp/month; next due day 105; varro Varro: 25 gp/month; next due day 112; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 2; galerius[party] active hp 7/7 init 4; faustina[party] active hp 10/10 init 4; callista[party] active hp 6/6 init 6; corvus[party] active hp 8/8 init 4; marius[party] active hp 4/4 init 2; varro[party] active hp 3/3 init 1; luminous-beetle1[foe] captured hp 8/8 init 2 slumbering; luminous-beetle2[foe] captured hp 7/7 init 6 slumbering; luminous-beetle3[foe] captured hp 6/6 init 1 slumbering; luminous-beetle4[foe] captured hp 4/4 init 6 slumbering; engaged
- **Schedule:** nothing due on day 66
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (2 slips): slipped on although enforced: the enforcement has a hole
  - ESCALATE [rest-due] (1 slip): slipped on after its reminder existed: move it into the engine or a script, make it a refusal, or tighten the trigger
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S10):** branch `claude/hopeful-ptolemy-1ea8tg` in this repo and the rules vault; tools on `tools.ref` (setup.sh). Set Campaign State `session:` to 10 **before any roll**; new log `Session Log/S10 — <summary>.md`; `party.agent.call_dir` to the new chat's scratchpad.
- **Standing instructions (user):** the Judge plays the six AI players by profiles, heuristics and party notes (no party-agent calls); Gideon calls. **New table rules (S09, user): combat is a failure state (steel only when the enemy cannot fight back or is plainly outmatched by the party and its allies; parley, tribute, trade, deception, alliance first; a failed edge means breaking off); dungeon and wilderness factions carry no lasting obligation and are used actively; settled factions only for the kingdom; the delve floors are minimums, not a measure of strength** (Campaign State Table rules, Party/heuristics.md, lesson `combat-failure-state`). Also: the kingdom goal; the pooled purse with Faustina; floors L1 6 HD, L2 12, L3 18; up to 4 henchmen; a downtime activity each between adventures; Hrodric's eagle by hand (4 hp, 1 HD).
- **In hand:** day 66, 17:35, Türos Tem; the whole company in town, rested. The purse with Faustina; 13,000gp with Karanos (free from day 82). Varro holds the 4 silver Ammonar symbols (L40), undivided: the players decide (sell, or keep for a temple of Ammonar). The pups' feed is paid to day 66: pay on (2.5gp a week) or Corvus hunts. Weather for each further town day: `weather --at 22.20 --day N` before the next march (lesson `town-days-weather`).
- **The temple now:** hobgoblins allied (Thethamun Friendly, half speed to about day 73); Abgal, Hepteth and four warriors fled toward the stair at 53 to the Lady (prep queue); orcs still take the party for recruits (a band held off raiding the hobgoblins); Red Eyes guard the stair under the ziggurat; Idimmu (never met in this timeline) takes 100gp a head. Options the players know: help Thethamun against Abgal's return; the Black Fangs below are out of favour (a possible ally); the hobgoblins' stair at 53 leads down (its lower door is sealed, Judge only).
- **Hiring:** month 3 searches open (days 61-90); the party holds 4 henchmen.
- **Engine gaps and slips (judge-notes):** S09's first run void (user); `rest-due` escalated (a sixth turn without rest on day 63: use `play.py walk` or `rest` each fifth turn); camp-past-encounter escalated (refusal widened); a module's own wandering encounter in 20.19 is the Judge's (the wagon).
