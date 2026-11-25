# Handoff (current state)

One file, rewritten each session by `handoff.py`; never appended to. The first block is generated from the state files; the second is the Judge's.

<!-- generated:start -->
- **Session** 9 · **day 67**, 05:50 · **no location** (-)

| Party | Class | XP | hp | Conditions |
| --- | --- | --- | --- | --- |
| Galerius | Fighter 2 | 3353 | 1/7 |  |
| Faustina | Priestess 2 | 3200 | 2/6 | bed rest 1 week (critically wounded day 66, healed by Varro): incapacitated; shattered ribs (permanent, day 66): constant fatigue and pain; must rest 2 turns ev |
| Callista | Mage 2 | 3200 | 4/6 |  |
| Corvus | Explorer 2 | 3200 | 1/8 | in shock (day 66): magical healing and one night of bed rest, or 1 week of bed rest: incapacitated; three fingers smashed on one hand: the hand is useless (perm |
| Hrodric | Shaman 2 | 2999 | 1/7 | in shock (day 66): magical healing and one night of bed rest, or 1 week of bed rest: incapacitated; two fingers smashed on one hand (permanent, day 66) |
| Severina | Venturer 1 | 567 | 7/7 |  |
| Varro | Crusader 1 | 0 | 3/3 |  |

- **Left behind:** lupa at Türos Tem (former henchman, bed rest at the inn) (since day 35); petra at Türos Tem (keeping the pups) (since day 59); titus at Türos Tem (keeping the pups) (since day 59)
- **Adventure:** A5 The Catacombs (Buried Temple, level 2) (open): Galerius (pc), Faustina (pc), Callista (pc), Corvus (pc), Hrodric (pc), Severina (pc), Marius (henchman, dead), Varro (henchman); lots 0; monsters 0 (0 XP); hoards unfound 0
- **Wages:** petra Petra: 12 gp/month; next due day 98; titus Titus: 12 gp/month; next due day 105; varro Varro: 25 gp/month; next due day 112; owed now: 0 gp | NOTE: wage timing: reading wage.timing
- **Fight in the combat state:** round 9; galerius[party] active hp 1/7 init 4; faustina[party] active hp 2/10 init 2; callista[party] active hp 4/6 init 5; corvus[party] active hp 1/8 init 1; hrodric[party] active hp 1/7 init 7; severina[party] active hp 7/7 init 1; marius[party] dead hp -5/4 init 4 unconscious; varro[party] active hp 3/3 init 4; ogre1[foe] absent hp 10/20 init 1 dehydrated; ogre2[foe] absent hp 5/15 init 4; hrodric-eagle[party] unconscious hp -2/4 init 6 unconscious; engaged
- **Schedule:** nothing due on day 67
- **Standing reminders (lessons whose conditions hold now):**
  - no standing reminder applies to the current state
- **Lessons to escalate (slipped on again):**
  - ESCALATE [camp-past-encounter] (2 slips): slipped on although enforced: the enforcement has a hole
<!-- generated:end -->

## Judge's notes for the next session
- **Start (S10):** branch `claude/hopeful-ptolemy-1ea8tg` in this repo and the rules vault; the tools clone on `tools.ref` (setup.sh). Set Campaign State `session:` to 10 **before any roll**; new log `Session Log/S10 — <summary>.md`, linked in the Campaign Log; `party.agent.call_dir` to the new chat's scratchpad.
- **Standing instructions (user):** as S08: the Judge plays the six AI players by profiles, heuristics and party notes; Gideon calls; the kingdom goal; the pooled purse with Faustina; Buried Temple floors L1 6 HD, L2 12, L3 18; up to 4 henchmen; a downtime activity each between adventures; skilled old-school play; the fortress long-term; Hrodric's eagle by hand (dead day 66: a new one at his next level).
- **In hand:** dawn of day 67, camp at the spring in 19.19 beside the temple. Adventure A5 open (no treasure). Faustina (critically wounded, a week of bed rest from day 66), Hrodric and Corvus (in shock: magical healing and one night of bed rest, or a week) incapacitated (half speed). Galerius 1 hp. Varro has his one Cure Light Injury again: on Hrodric, then a night's bed rest (rest days, `rest-day`), then Hrodric's two cures for Corvus (and one for Galerius or Faustina). A night encounter is pending for hour 1 after dusk if they stay camped (the camp line said so). Galerius and Severina slept only 7 hours (watch split): sleep owed.
- **Money:** the purse is empty (Faustina 2sp); 13,000gp with Karanos (free from day 82; 15% before). Wages paid: Petra to 97, Titus to 104, Varro to 111. The pups (Petra and Titus) fed to day 66; more feed owed from day 67 (pay on return).
- **Marius:** dead (death processed; actor in `Characters/former/`), body hidden in L2 1 under the stair, his gear `body:marius`. Severina keeps Petra and Titus. A heroic funeral or reserve XP: none (henchman).
- **Next:** home to Türos Tem through the mud (4 days or more); `adventure return` and an empty payout for A5; Faustina's week; training resumes (`train resume C21`-`C25`); month 3 searches open (the party is at 3 henchmen now). The 47 goblins in L1 43 (Friendly, want the hobgoblins) and Idimmu (Friendly) stand.
- **Engine gaps / slips (judge-notes):** the town week had no weather (mud never dried): roll `weather --at HEX --day N` for days spent in a settlement before the next march; `round-auto` acts for the current combatant: never call `round-next` before it; standing order `hold` still attacks a foe in reach: after a parley, end the fight at once; `camp --hours` must leave every member 8 hours (12 with four watches).
