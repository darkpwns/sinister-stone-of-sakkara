# Dungeon delves — with the rules engine

Load when the party is inside a dungeon, lair or ruin. The engine (`bash $S/acks.sh CMD …`, stage 2) keeps the
clock, light, timers, rest and the wandering checks in the exploration state (config `tools.exploration_state`), and
resolves listening, searching, secret doors, locks, stuck doors, traps, mapping and movement rates with their time
cost and source. Do not look those up. Look up (rules lookup skill) only what `tools.coverage` leaves to lookup:
climbing, swimming and other caving rules (their throws go through `acks.sh throw`), a trap's own effect, a spell's
effect and duration. If setup printed `engine: UNAVAILABLE`, run the delve by Judge's Screen §4 with `dice.py` and
`encounter.py dungeon LEVEL` (the old procedure is in the git history of this file).

Engine lines: `[H]` parts are Judge-only (wandering checks, encounter rolls, listening and searching results, trap
triggers): Judge block only. `| JUDGE:` lists what is left to you; `| NOTE:` actor differences and readings applied.

## Before the first turn
1. Read the hub note's `Running …` section and Contents. No keyed content: stop, `unprepped-sites.md`.
2. Exploration state, once per campaign (it persists): `acks.sh explore-init --day <day> --time <HH:MM>`. Party
   members, once per character: `acks.sh party add <id>` (the actor id; Endurance is read from the
   actor; henchmen too).
3. The site: `acks.sh location --site "<name>" --hub "<hub note path>"` reads the hub's `Running …` lines
   (`Dungeon level: N`, `Wandering monsters: none` or `Wandering monsters: 1d6 every 3 turns, 4+`, `Encounter table:
   FILE` in acks-table/1 with `source.campaign: true`). Without a hub line: `--level N` (JJ p. 36 default check
   1d6 every 2 turns, 6+). Prep writes these lines in the hub's `Running …` section.
   An area with its own rate (a module's "5-6 each turn in Area 1"): `acks.sh location --wandering "1d6 every 1 turns, 5+"` changes only the rate (site, level and table stay); go back with the hub's value. A module's level 2 table: `--table FILE`.
4. Light: `acks.sh light on --kind torch|lantern|candle --carrier <id>` (`--tallow` for tallow candles): the torch, candle or flask of oil comes out of the carrier's inventory, refused if he has none (`inventory.md`). Marching
   order in the tracker (`public.tracker.formation`). Speeds: `acks.sh move-rate <id>` (encumbrance from the
   actor's gear; `--coins N`/`--add-stone N` for loot carried; `--blinded`).

## Each turn (10 minutes)
1. Actions declared: methodical (a full turn) or hasty (1 round). Each action command below gives its throw and its
   time cost; it does **not** move the clock (several characters act in the same turn).
   - Listen (closest member only, once per turn while moving): `acks.sh explore listen <id> [--still]` — hidden.
     Whether the noise is in earshot: `acks.sh explore earshot --sound talking --env normal --distance 30 --doors 1`.
   - Search: `acks.sh explore search <id> --methodical|--hasty [--feature <name>] [--pole]`; secret doors:
     `acks.sh explore secret-door <id> [--hasty]` — hidden. Hasty: thieves only; a failed hasty search of a feature
     is remembered until a higher level.
   - Locks: `acks.sh explore lock <id> --hasty|--methodical --lock <name>` (or `--key`). Jammed locks remembered.
   - Stuck doors: `acks.sh explore force-door <id> [<helper id>] [--crowbar] [--spikes N] --door <name>`;
     batter with an axe: `acks.sh explore batter --door wooden|iron-banded` (then `turn 1` or `turn 3`); spikes:
     `acks.sh explore spike --spikes N --by <id>` (his iron spikes are used up; `--crowbar` and `--pole` need the tool in
     the actor's inventory).
   - Traps: risky movement past a trigger `acks.sh explore trap-trigger <who> [--pole] [--times N] --trap <name>`
     (hidden; in marching order); disabling `acks.sh explore trapbreak <id> --hasty|--methodical --trap <name>`;
     pits `acks.sh explore pit <who> --depth 20` (damage to Campaign State hp, or `damage` in a fight).
   - Mapping: `acks.sh explore map <id> [--error]` (needs an open lit source; mapper vulnerable).
2. Advance the clock: `acks.sh turn [N]` (or `--rounds N` for a hasty action outside a fight, a fight's rounds when
   it ends, or the time an influence attempt took). It runs the wandering checks the site's settings call for (at the
   start of every 2nd turn by default), burns light and timers, counts turns since rest, and reports everything that
   ran out, expired or became due. **If a check finds an encounter, the advance stops at its minute** and the line
   shows who, how many and the maximum distance (all `[H]`): go to `encounters.md`.
   `turn N` also stops in the turn the last light burns out. Many turns in one call: `python3 $S/play.py walk N
   --relight A,B` (rests after 5 turns, relights (a carrier's own lantern first: lit, or refuelled and lit), stops
   with the reason at an encounter, a character down, no light left, a timer that runs out (`--past-timers` to go on)
   or anything left to the Judge); or set the standing order `acks.sh light auto on --carriers A,B` once per
   delve and the engine lights the next torch itself.
3. Rest: `acks.sh rest` (1 turn) after 5 turns; the `turn` line says "rest due"; a 6th turn without rest makes the
   party winded (no running or charging) until it rests 1 turn (Endurance exempt).
4. Spells and effects with a duration: `acks.sh timer add "<spell> (<caster>)" --for 6t [--hidden]` with the duration
   from the spell's note; `turn` reports the expiry.
5. Room by room: `acks.sh location --room <key>` (for the log); World State per room below.

## Reading rooms
Read only the notes for rooms the party is in or can perceive. Lead with what matters (danger, exits, what draws the
eye), then answer what the player looks at. Never mention what a key holds that the characters cannot perceive
(hidden doors, contents of closed containers, monsters out of sight). A listen or search line marked `[H]` that
succeeds lets you narrate what is there; a failure says nothing either way.

## State
- `save.sh` runs `xsync.py` first: it copies the engine's player view (time of day, light sources with bearer and
  turns left, winded) into Campaign State `public.time` / `public.light`. Wandering checks, encounters and hidden
  timers never leave the exploration state. Rations: `public.rations` from the engine's travel block (stage 4).
- World State: one subsection per site, headed with its wiki link: each room entered and its state (opened, looted,
  monsters slain or fled, traps sprung, locks jammed). Campaign State `public`: party hp and conditions.
- Write after each room resolved and each fight; `save.sh`. Leaving the site for a settlement:
  `acks.sh location --settlement <Name>` (one command: no wandering checks, the rest count cleared; a town night then
  counts). Leaving it for the wilderness: `acks.sh location --clear`. `location` alone shows where the party is.
  Moving on inside a delve (`location --site … --level N`) keeps the wandering count. A door kind the module gives
  (a slab, a bronze door): `explore force-door A B --helpers C,D --door-kind "<kind>"`: the engine reads the campaign's
  doors table and rulings; never pass a door's penalty by hand.
- `acks.sh clock [--player]` shows the time, light, timers, rest and location (`--player`: open values only).
- A day passing (`turn` line "day N begins"): with a travel block (`travel-init` before the expedition), the engine's
  rollover runs rations (iron rations keep one week in a dungeon), water, sleep owed, fatigue (each hour of delving is
  strenuous) and healing; read its lines. Sleeping in the dungeon: `camp --watches … --hours 8` records the sleep and
  makes no wilderness night check; run the site's wandering checks for those hours (`wander-check`).

## Engine 7.23-7.24 (Sakkara run 2 requests)
- **Rest turns are enforced:** `turn N` refuses exploration that would pass the fifth turn without a rest turn
  (RR p. 271): `rest` first, or `turn N --auto-rest` (rests whenever one falls due, as `play.py walk`); a Judge who
  means it: `ACKS_ACK=rest-due`.
- **An encounter is played before anything else:** `encounter end` refuses a wandering encounter that arrived and was
  never played (no distance, surprise, reaction, evasion or fight) unless `--unplayed "why"`; `location` (a change),
  `wait` and the day commands refuse while an encounter is unresolved (`ACKS_ACK=encounter-open`); `acks.sh batch`
  stops after the command that brought an encounter and names it.
- **Waiting at a site is rest:** `wait` in a dungeon counts as rest for fatigue, not delving (reading
  `time.waiting_not_delving`); the line says what each day at the site counts as. A night slept there: `wait --hours N
  --sleep [--armored IDS]` (or `camp`, as before).
- **Room settings from the hub:** `Room R: <rate>[; table FILE] [(condition)]` lines in a hub's Running section;
  `location --room R` applies them and the site's return when the party leaves the room; a setting that waits for
  'once …' applies after `location --room R --cleared` (the ogre den, L2 7).
- **Module stat lines:** `encounter start --placed --key "Adventure/Level 2 - Catacombs.md#7" --in-lair yes`: the
  monster, number, hp list and a special weapon from the room key; `encounter fight` uses them (no `state set`).
- **Taint (AX1 level 2):** `taint drink ID` (a save vs Spells or a mutation), `taint touch ID`, `taint immerse ID
  --rounds N`, `taint show` from `Campaign/taint.yaml`; `reaction` sums the face's mutations. Water purified with
  `water --purified-by ID` carries no taint.
