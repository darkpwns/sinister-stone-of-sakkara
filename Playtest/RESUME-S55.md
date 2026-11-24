resume Sakkara

Continue the Sakkara playtest (AX1-AX3) as the Judge, using the `acks2-judge` skill in `darkpwns/sinister-stone-of-sakkara`. Before anything else:

1. All four repositories: check out the branch `ccr-6e7c0096-7nmfvu`. `mkdir -p /home/claude` and symlink each clone from /home/user into it (`ln -s /home/user/<repo> /home/claude/<repo>`). Run `bash .claude/skills/acks2-judge/scripts/setup.sh && python3 .claude/skills/acks2-judge/scripts/brief.py`: setup must print `engine: ready: acks 7.17.7` (or later) and end with `ready`. Read the brief's parts (Campaign State, the handoff) with head/sed, not whole.
2. Read the handoff (`Campaign/handoff.md`), `.claude/skills/acks2-judge/references/memory.md`, `references/judge-screen.md` and `references/combat-totm.md`, `Campaign/Rulings.md` (the S52-S54 rows above all), `Party/party-notes.md` (lessons 100-110 and the S52-S54 entries), the S52-S54 lines at the end of `Playtest/judge-notes.txt`, the prep queue and NPC attitudes in `Campaign/World State.md`, `Adventure/Legion Waygate.md`, and the tail of `Session Log/S54 — The Night at the Silk Pony.md`. Do not read `Playtest/HANDOFF.md`.
3. Start session S55: set Campaign State `session: 55`, create `Session Log/S55 — <summary>.md` and link it in the Campaign Log. Set `party.agent.call_dir` in `Campaign/campaign.yaml` to this chat's scratchpad. The Judge plays the AI party by `Party/profiles/`, `Party/heuristics.md` and `Party/party-notes.md` (no party-agent calls). Priya plays Vestus.
4. First, before play: the day-862 weekly city block (six week's-secret entries in World State first, then `ACKS_ACK=secret-entries-first acks.sh schedule run --due`); fort meals from `fort-stores` for days 852-859 are not yet drawn (the company was on the march 852-859: draw from the 859 return on).

Play from day 859, late morning, at the fort of the Ford (26.19; the location is set as the settlement 'Turos Aster' by convention; the animals are at the Legate's stables). No adventure is open. Hit points: Vettius 18/34, Cotta 18/20, Neris 19/21, Vestus 18/19, Phaedra 19/20, the rest full.
- The Legion Waygate (Rulings S53, S54; Adventure/Legion Waygate.md): the fort's arch is open; the company holds the three tesserae (L999-L1001) and the watchword; the city's arch is in the buried legion camp under Cyfaraun's Old District's old baths (the stolen survey) and is UNPREPPED: prep it by `references/unprepped-sites.md` before the party goes. The gate does nothing until both arches are open.
- Vettius is away from Cyfaraun again: month 29 ends day 870: the take at half and the 1-in-6 usurpation roll (the month-end item lists the Ford's rolls and the Family's terms). Thana is with child (before the winter festival).
- Near the fort: the unicorn spring (27.18, 600 st of components: carts), the ruined wizard's tower (27.18, unoccupied JJ ruin: prep if visited), the vista and spring in 26.19, the draugr of 30.17 (avoid).
- Wages: the earliest due are Ennia day 875 and Phaedra 880: before any march pay through the expected return plus a month (lesson wages-before-split).

How play runs (engine 7.17.7; the references have the detail):
- A `REMINDER: [id] …` at the end of an engine line is a recorded lesson that applies now: act on it. `NOT RUN (lesson): …` is a refusal: fix the command, or put `ACKS_ACK=id` before it when you mean it.
- Known engine gaps (judge-notes S47-S54): navigation is thrown on road days and beside the road (`navigate --found` when the party sees the road); the hexes CSV's 'wilderness' classification breaks `travel`, `camp` and wilderness encounters (pass `--hex CC.RR:classification=unsettled` for every such hex on the route; the barony 26.19 as outlands); `encounter start --wild --hex` overrides only the named hex (the table comes from the travel hex); `recover --lots` is 0-indexed; actors' spells_used is not cleared by `rest-day --settlement`; `state set hd=N` does not re-roll hp (roll and set hp yourself); `offer --count` above the pool rolls then fails; water is not shared at the rollover (check every member's waterskins and water before a march); mounts need feed (Rulings S53: 2sp a stone, carried); `supplies show ID --on ANIMAL` must be undone (`--on none`) before `inv stable`; foes' spells are not modelled; dice labels must not contain a colon.
- Big fights: step them with `round-start` / `round-next` and act for the combatant named; the S54 drivers in `Playtest/tools/s54_*.py` show the pattern (stop at a fallen party member).
- Session end: `python3 $S/handoff.py --notes-file <file>`, then `save.sh "S55 end: <summary>"`.

Standing instructions from the user (unchanged from S08-S54):
- Every character uses all of his class powers and proficiencies where they apply; every henchman hired gets the proficiencies his level allows.
- New PCs start at 1st level with reserve and funeral XP; higher-level help is hired as henchmen. A PC's death: the player takes over the dead PC's henchman, else another henchman in the party (Table rules).
- Party strength floor per depth band (Upper 18, Lower 24, Deep 30, Abyssal 39, Sub-Abyssal 48). A death that drops the party below the floor of its band turns it back. The party keeps the henchmen it has and hires again only below the floor.
- The party delves as adventurers: multi-day expeditions toward the deepest, richest areas its strength allows, sleeping below in sealed, spiked rooms.
- Taxes: one selling day a month, early in the month, for coin and gems; the company's goods go through the Family at full value (Rulings S19).
- Rival NPC parties' delves off stage use the rulebook's abstract dungeon method (JJ 10; Rulings S31); their wilderness fights the abstract wilderness method (JJ 11).
- A missed wage that comes from the Judge's bookkeeping and not from the players' choice is void (Rulings S47): the players pay ahead before any departure.
- Vettius is married to Thana (S54); the party pursues the legion gate to join Cyfaraun and the fort (user's direction, S53).
- The test continues until a TPK.

Give the recap (at most 5 lines) and continue play. Commit and push after every state write (`save.sh`), on branch `ccr-6e7c0096-7nmfvu`.
