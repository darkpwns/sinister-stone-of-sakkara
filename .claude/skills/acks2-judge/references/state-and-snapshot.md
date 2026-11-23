# State, snapshot, prep queue, session end

Load before the first state write of a chat, for the prep queue, and at session end. The config schema is in `config-schema.md`.

## Files and what goes where
- **Campaign State** front matter: `session`, `mode`, `location` (wiki link), `adventure`, and `public:` — `date {year, season, day}`, `time`, `weather`, `place` (the name the party uses), `hex`, `party` (list: `name, sheet, role, hp, hp_max, conditions, spells_used, encumbrance_st`; generated from the actors in `Characters/` by `xsync.py` at every save, never edited by hand), `light`, `rations`, `tracker` (combat-totm.md), `threads` (open threads as the party knows them). Body: Table rules, Resources (mounts and hirelings in brief; possessions, ammunition and torches are the inventory's, `inventory.md`), short Judge notes.
- **World State** (keep it short): `## Explored hexes` (Hex | Terrain | First visited | Notes), `## Dungeons and lairs`, `## Events triggered`, `## NPC attitudes`, `## Faction standing`, `## Scheduled events` (campaign clocks are linked, not copied), `## Prep queue (Judge only)`.
- **Rulings:** one table row per precedent: date, session, question, ruling, source or "Judge's ruling" / "Judge's call".
- **Ledger:** treasure, monster XP, shares and XP, wages, purchases and sales.
- **Actors** (`Characters/<id>.json`; NPCs `Actors/npc/`, named monsters `Actors/monsters/`): characters.md. Current hp, conditions and spells used are each actor's `state` (`acks.sh actor set`).
- **Wiki logs** (config `logs`), never duplicated in Campaign/: the session log; rumours given (the rumours note's "heard" section); story strands discovered (tick the box); clock status (the clock note's column, Judge only).

## Session log
`S## — <summary>.md` from the template, in config `logs.session_log.folder`, linked under the index section. The template's sections are the player-facing part, written in player terms (no Judge-only names or numbers). At the end, the collapsed Judge block (config `judge_block`) holds: hidden rolls (`dice.py --dump hidden`), monster hp and morale, the Judge half of each fight's tracker, site builds, NPC voices invented, and anything else Judge-only.

## Snapshot (`snapshot.py`, run by `save.sh`)
Player-facing fields only: date and time, weather, place and hex, explored hexes (hex and terrain), character and henchman actors as the player would see them (the engine's prepared player view, `acks actor show --player`, cut to the sheet keys the VTT page reads; a monster actor: its name), current hp, conditions, light and rations, this session's open rolls, the combat tracker's player half, rumours heard, open threads. It refuses (writes nothing) if `public:` has a key outside its whitelist or an actor file's id is not its name, if an unidentified item's true name or vault note name appears or a treasure true-record field (`rarity`, `base_gp`, `subtable`, `true`) does (engine stage 5), or if the output contains a Judge-only note title (from `secrecy.judge_only_folders`, unless listed in `secrecy.revealed`), the secret tag, a Judge-only callout or a hidden-roll marker. Fix the input, never the whitelist, unless the field is truly player-facing. Open rolls carry at most the latest 50 of the session; `public.trail` (the party's last hexes, oldest first, at most 20) feeds the map's movement trail.

## Display page (VTT) db write
The VTT page (config `display`: artifact slug, url, db document) shows the snapshot to the player; it never writes. After every `save.sh` that wrote a new snapshot:
1. `python3 $S/snapshot.py --payload` prints the document: `{"schema": 1, "written_at": …, "snapshot": {…}}`.
2. `db_write` (artifact tools; slug = config `display.artifact_slug`) with one op `set`, path = config `display.db_doc`, data = that document, `ifVersion` = the version from your last `db_write` result in this chat, or from `db_get` on that path if you have none (omit only if the document does not exist).
3. Failure (a conflict, a refusal, an outage): re-read the version with `db_get` and retry once. If that fails too, tell the user in one line ("display page not updated; the repo is"), carry on playing, and write again at the next state write. Each write is the whole snapshot, so the next one repairs a missed one. `Campaign/snapshot.json` in the repo stays authoritative.
4. Never write anything to the db except that document, and never a snapshot that `snapshot.py` refused.

## Prep queue (end of every session)
Rewrite `## Prep queue (Judge only)` in World State:
1. **Sites within about 3 days' travel:** `hex.py --sites <party hex> <N>` with N = 3 × the party's hexes per day (round up); list each UNPREPPED site with hex and distance.
2. **Threads the party is chasing:** from `public.threads` and the session log.
3. **Clock dates in the next 6 months:** from each config `logs.clocks` note (Judge only) and World State Scheduled events.
4. **NPCs named in play but not written up:** with the traits and voice given, the place met, and the session.
The prep skill (a later step) works through this list.

## Session end checklist
Session log (player part + Judge block) → Campaign State `public` → World State (incl. prep queue) → Ledger → Rulings → actors' state (hp, conditions, spells used) → wiki logs → calendar note's campaign date → the Judge's notes for the next session (`python3 $S/handoff.py --notes-file <file>`: what was in hand, what comes next; no numbers, the generated block has them) → `save.sh "S## end: <summary>"` (it also archives the actors' change logs, compacts the exploration state into `Campaign/archive/` and rewrites `Campaign/handoff.md`) (a message starting `S## end` also moves every actor's change log to `Campaign/actor-changes/<id>.jsonl`, tagged with the session) → confirm the push in one line.
