# Prompt for the next session (paste into a new cloud session)

Attach the repositories `darkpwns/sinister-stone-of-sakkara`, `darkpwns/acks2-tools`, `darkpwns/acks2-rules-vault`
and `darkpwns/kardakia-campaign`, then paste everything between the lines.

---

resume Sakkara

Continue the Secrets of the Nethercity (AX2) playtest as the Judge, using the `acks2-judge` skill in `darkpwns/sinister-stone-of-sakkara`. Before anything else:

1. All four repositories: check out the branch `ccr-6e7c0096-7nmfvu` (the work is there, not on the default branches). `mkdir -p /home/claude` and symlink each clone from /home/user into it (`ln -s /home/user/<repo> /home/claude/<repo>`). Run `bash .claude/skills/acks2-judge/scripts/setup.sh && python3 .claude/skills/acks2-judge/scripts/brief.py`: setup must print `engine: ready: acks 7.17.7` (or later) and end with `ready`.
2. Read the handoff the brief prints (`Campaign/handoff.md`: generated state, then the Judge's notes), `.claude/skills/acks2-judge/references/memory.md` and `references/judge-screen.md`, `Campaign/Rulings.md` (the S29 rows above all), `Party/party-notes.md`, the S29 lines at the end of `Playtest/judge-notes.txt`, and the tail of `Session Log/S29 — The High Priest's Shade.md`. Do not read `Playtest/HANDOFF.md`: it is the archive of S01-S28.
3. Start session S30: set Campaign State `session: 30`, create `Session Log/S30 — <summary>.md` and link it in the Campaign Log. Set `party.agent.call_dir` in `Campaign/campaign.yaml` to this chat's scratchpad. The Judge plays the AI party by `Party/profiles/`, `Party/heuristics.md` and `Party/party-notes.md` (no party-agent calls), as in S06-S29.
4. First, the gap owed from S29: the Imperial Vanguard's descent by the 12U cesspool on day 481 was never resolved. Settle it by hidden rolls before play goes on (route, rooms reached, losses, what they took, when they came back up), record it in World State and judge-notes, and save.

Play from day 487, 21:18, at the Solar Citadel in Cyfaraun. Ten in the company; Iulia is on bed rest to day 492 (her hand restored), Brennus mending; Marcellus and Varro resigned day 484.
- Downtime, days 488-492: the party prepares for the next delve while Iulia rests (restock, Phaedra's wage on day 490, masks, research or spell copying, the Family's spies on the Vanguard; no hiring while above the floor), by each activity's procedure. Day 491 is the weekly block.
- Then play the following week: the delve the table plans once Iulia is up (next on its list: L's inner caves, the ant queen, her four soldiers and eggs; then L4, F17, K, J8, R). The Order's roll falls on day 494.

How play runs (engine 7.17.7; the references have the detail):
- A `REMINDER: [id] …` at the end of an engine line is a recorded lesson that applies now: act on it. `NOT RUN (lesson): …` is a refusal: fix the command, or put `ACKS_ACK=id` before it when you mean it. Record a slip with `acks.sh lesson slip ID --day N --note "…"` and the judge-notes line.
- The schedule (`Campaign/schedule.yaml`) holds the Order's roll, the weekly block, month's end and dated events; `acks.sh schedule run --due` rolls them hidden and prints the steps. Where a step says a consequence was never defined, rule it, record the ruling and write it into the schedule.
- Use `python3 $S/play.py walk N`, `play.py supplies`, `play.py bank --to guildhouse-bank`, `play.py payout`, `play.py cond add|remove ID "…"`, and `acks.sh batch` for a moment's independent commands. Never let a scripted loop run past an encounter, a fallen character or a JUDGE line. The S29 fight helpers are in `Playtest/tools/` (s29_melee.py, s29_antwall.py, s29_sealed.py).
- Town: `acks.sh location --settlement Cyfaraun` on every return, then `wait`; meals and the night are the engine's; the Captain's company lodges free at the Citadel.
- Fights: `state init` before each new fight and `encounter end` after it; set `state distance` for every foe first and step with `round-next` (never act outside it). The surprised cannot act in round 1. `state end` records the killed and writes hp to the actors: copy only the lasting conditions it names. Backstab is automatic. The Underwatch shield is `state ward add iulia …`; faewyrd whispers `state aura add …`. Rotate the front line before anyone is below half.
- In L: no torches or fire over the sludge (firedamp, Rulings S29): Iulia's spear and shut lanterns; filter masks (hourly save at +6).
- Sealed nights below: `camp --watches "A,B;C,D;E,F" --hours 12` (4-hour watches, casters off watch); camp makes the night's checks itself.
- Session end: `python3 $S/handoff.py --notes-file <file>` (what was in hand and what comes next, no numbers), then `save.sh "S30 end: <summary>"`.

Standing instructions from the user (unchanged from S08-S29):
- Every character uses all of his class powers and proficiencies where they apply; every henchman hired gets the proficiencies his level allows.
- New PCs start at 1st level with reserve and funeral XP; higher-level help is hired as henchmen.
- Party strength floor per depth band (Upper 18, Lower 24, Deep 30, Abyssal 39, Sub-Abyssal 48). A death that drops the party below the floor of its band turns it back. The party keeps the henchmen it has and hires again only below the floor.
- The party delves as adventurers: multi-day expeditions toward the deepest, richest areas its strength allows, sleeping below in sealed, spiked rooms.
- Taxes: one selling day a month, early in the month, for coin and gems; elven relics go to Liber Faunus at 80% (Liber is dead: the company's goods go through the Family at full value, Rulings S19).
- The test continues until a TPK.

Give the recap (at most 5 lines) and continue play. Commit and push after every state write (`save.sh`), on branch `ccr-6e7c0096-7nmfvu`.

---
