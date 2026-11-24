# Engine and tool requests from the Sakkara playtest (S47-S54)

Work in `darkpwns/acks2-tools` (the engine, `acks`) and in the Judge skill's scripts in `darkpwns/sinister-stone-of-sakkara`
(`.claude/skills/acks2-judge/scripts/`; keep `darkpwns/kardakia-campaign`'s copy of the skill in step). Branch:
`ccr-6e7c0096-7nmfvu` in every repo. Evidence for each item: `Playtest/judge-notes.txt` (the Slip/Finding/Void lines of
S47-S54) and `Campaign/roll-log.jsonl` in the Sakkara repo. Rules come from `darkpwns/acks2-rules-vault` (read-only):
every number the engine applies must name its source as the engine already does; where the rules are silent, add a
named reading or a campaign-ruling hook (`Campaign/engine-rulings.yaml`), never a silent default.

For every change: a test in the engine's test suite; `engine/COVERAGE.md` and `HISTORY.md` updated; the version bumped
(7.18.x); `acks check` passes; the skill's references (`references/*.md`) and `scripts/tests/test_scripts.py` updated
where a command changes. Run the full test suites before each commit. Do not change campaign state files.

## A. Bugs and refusals that cost time in play (fix first)
1. **Hex classification 'wilderness'.** The hexes CSV uses `wilderness`; `travel`, `camp`, `search` and
   `encounter start --wild` fail with "'wilderness' is not in list". Map it in the hex adapter (to `unsettled` by the
   JJ territory table, or make the mapping a campaign setting in `campaign.yaml hexes`), and let a domain's hexes be
   read as the domain's classification (`outlands` for the Barony of the Ford, 26.19) from campaign data.
2. **Navigation on and beside roads.** A route that follows a road throws no Navigation; but a route that leaves the
   road for one hex, and the first day out from a settlement, keep throwing and putting the party 'lost' onto the road
   it knows. When a lost party enters a road hex, or any hex it has visited and named, it becomes aware and found by
   itself (RR Navigation: a recognised landmark). `--familiar ID` (Pathfinding) must work with classification overrides.
3. **`encounter start --wild --hex CC.RR:…`** applies the override to that hex but rolls on the travel hex's table.
   Add `--at CC.RR` (roll on that hex's tables) and refuse an override for a hex that is neither the travel hex nor `--at`.
4. **`recover --lots`** is 0-indexed and silent about it. Show each lot's index in `treasure`/`adventure show` output,
   accept lot ids, and add `recover --undo L#` (returns the lot to its hoard, voiding the recover event).
5. **`state set ID hd=N`** keeps the 1-HD hp rolled at `state add`; `perceived=` set later is not used in attack lines.
   Add `state add … --hd N` (rolls hp for those Hit Dice) and make `state set hd=` offer `--reroll-hp`; attack lines
   must use the current `perceived`.
6. **`offer --count N`** above the candidates' count rolls the reaction, then fails without recording. Refuse before
   any roll.
7. **Spells used.** `rest-day --settlement` (and `wait` in a settlement over 8 night hours) does not clear actors'
   `state.spells_used`; `camp` does. Clear it wherever restful sleep is recorded.
8. **Water at the rollover.** Food is shared at the rollover, water is not: a member with no waterskins dehydrates while
   others carry days of water (Neris, S53). Share water as food is shared (the same `--mode`), and refuse `travel` when
   any member has less than a day of water and the route has no river or well that day (`ACKS_ACK` to override).
9. **`supplies show ID --on ANIMAL`** blocks `inv stable` until undone with `--on none`; `inv stable` should unpack the
   members' supplies onto the members (and dismount riders) by itself, saying so.
10. **`schedule due --ahead`** lists items run early with `schedule run --day N` as still due on the current day.
11. **`state end`** demands a damage type for every felled foe that took `state set hp` damage. Record the type when
    damage comes from `damage --type` or the new area command (B1), and default to the weapon's type for attacks.
12. **`retinue set`** takes no `--cause`; add it and write the change to the retinue history. A hireling group's count
    lost to monsters (S54: three laborers) needs `retinue lose ID N --cause "…"`.
13. **Dead animals.** `inv holder remove` refuses while the animal holds its tack; add `inv animal dies ID --cause …`
    (load dropped at the site, riders dismounted, holder closed).
14. **`roll`**: accept exploding dice (`1d10!`) for the population rolls, and colons in labels (quote-safe parsing).
15. **`treasure --terrain`** accepts only the table's exact words (`grass`, not `grassland`): map the hex adapter's
    terrains and aliases.
16. **`wait` in a settlement** while fatigued counts as "still active" and worsens fatigue; a day of `wait` in town with
    no strenuous activity should count as rest (or refuse `wait` past 12 hours and point to `rest-day`).
17. Known from S47-S51, still open: round-end morale counts slumbering party members as felled; `encounter surprise`
    omits a monster's own surprise bonus; leaders' weapon bonuses and Hit-Dice saves (MM leader tables) not modelled;
    stale engagements from killed foes block charges; `level-up --member` rolls the henchman's level loyalty itself
    (document it); `search` names a known site first; `encounter start --placed` rolls a lair check for a found lair.

## B. New engine capability
1. **Area spells: `acks area --spell "Fireball" --caster ID --targets A,B,… [--dice 8d6]`.** Rolls the damage once
   (open), each target's save (hidden), skips the save where half the damage would still fell the target, applies
   damage with its type and tier, and records the type for `state end`. Reads the spell's area, save and damage from
   the vault note; `--count N` for "about N creatures in the area" with the Judge's screen §3 conventions; refuses a
   party member in the area unless named with `--include`.
2. **Group actions for large fights: `acks act GROUP --tactic shoot-nearest|close-and-attack|hold|flee|hack DOOR:N`**
   and `acks round-auto --until party-down|judge|round-end`: steps `round-next` and, for each combatant, applies its
   group's standing tactic (attack throws, moves within move-rate, engagement limits by frontage: `state frontage
   PASSAGE 2`), stopping at any party member's own turn unless that member has a standing order, at a felled party
   member, a JUDGE item, or a refusal. Party members get standing orders (`state order ID shoot-nearest --group G`).
   This replaces the per-session drivers in `Playtest/tools/s54_*.py`.
3. **Foes' spells.** Monster and NPC casters (shamans, witch doctors, cult priests, the draugr's spell-like powers)
   need a spell list in the combat state (`state set ID spells="Command,Cause Light Injury x2"`) and `acks cast ID SPELL
   --targets …` resolving the common spells (Slumber, Command, Halt Humanoids, Cause/Cure Injury, Holy Circle and its
   reverse) by their vault notes.
4. **Terrain encounters (JJ pp. 63-68): `acks terrain-encounter [--type T]`** for the dangerous, valuable and unique
   types the engine already rolls: the sub-tables (cache with Treasure Type by Terrain, ruin structure and value,
   trap and hazard as JJ trap levels with the marching-order trigger rolls and bypass hours plus the extra encounter
   throw, challenge type and dimensions, poison type and doses with the identification and harvest throws, magical
   place spell and frequency, magical resource value and weight, double), all hidden and logged, with the Judge's
   choices as options.
5. **Domains (RR Domains and Realms, Keeping the Peace, Experience from Domains): `acks domain init|month|show`.**
   A domain record (hexes, classification, land value per hex, families, stronghold value and minimum, garrison,
   ruler and magistrates, taxes, liturgies, tithes, morale base and current, investments, construction projects with
   labor rates). `domain month` does revenue, expenses, domain income, personal authority, base and current morale
   (the roll with its modifiers), effects of morale, population growth and loss (exploding), agricultural investment
   families, prestige immigration (only when secure and the ruler adventured), domain XP above the threshold, and
   construction progress, writing the coins through the inventory. The Sakkara rulings S51-S54 on the Barony of the
   Ford are the test case (21 families at month 28's end).
6. **Mounts' feed.** A catalog row for animal feed (RR Surviving the Wild: 2sp a stone), consumed at the rollover from
   the animals' loads by their daily food (normal load / 10; grazers excepted unless force-marched), with the
   underfed and starving conditions for animals; refuse `travel` when non-grazers carry no feed (override with ACKS_ACK).
7. **Spoilage warning.** Standard rations carried in the wild spoil; print the days left at each rollover and warn a
   day ahead.

## C. Skill scripts (`.claude/skills/acks2-judge/scripts/`)
1. **`play.py depart --route … --return-day N`**: the pre-march checklist as one command: wages through the return
   plus a month (lists what to pay), food and water days per member, waterskins per member, feed per animal, mounts'
   loads and the column's speed (which animal sets it), light, spells, the weekly and month-end items that fall on the
   road. Refuses to report ready while any line fails.
2. **`play.py march DAYS --route … [--hours-per-day N] [--watches …]`**: the S54 march helper as a supported command:
   travel, evening wait, feed and water at the day's source, camp, with stops at any encounter (benign civilized and
   herd encounters passed by after their reaction), lost status, CON loss, a missed wage, a due schedule item. Uses the
   classification overrides from campaign data, never per call.
3. **`play.py city-week`**: prints the six entries' template for the week's secrets, refuses the run until World State
   holds them, runs the weekly block, and writes the results line into World State in the established format.
4. **`play.py month-end`**: runs the month-end item and the domain month (B5), posts the bank fee, the Family's take
   by Rulings S46 (full or half by Vettius' location; the usurpation roll when away), Lucilla's income and
   investments, and writes the World State and Rulings lines.
5. Fix `brief.py` to print only the parts the resume prompt names (it prints 1,000 lines now), and `handoff.py` to
   list party members who are left behind (Tiberius at the fort was missing from S54's table).
6. Escalated lessons in the handoff (wage-days, surprise-members, npc-rolls-hidden, driver-loop-stop): move each into
   a refusal or a script per `references/memory.md`, so the ESCALATE lines clear.

## D. Still open from the SOTN sessions (S29-S48; after the S29 engineering pass, engine 7.16.0-7.17.7)
`Playtest/OPEN-ITEMS.md` closed most of the S08-S28 findings in 7.16-7.17.7; these came after it, or were left open there.
1. `encounter fight --set hp=N` does not set the keyed hp (monsters keep rolled hp) (S30, judge-notes l. 552).
2. `explore force-door --door-kind` is case-sensitive ("stone slab" vs the table's "Stone slab") (S31, l. 554).
3. `state end` leaves `Campaign/combat-state.json` in place, so the next `encounter fight` refuses ("a fight in
   progress") and `throw`/`--prof` outside a fight refuse an actor not in the stale file (S38 l. 614, S43 l. 635).
   `state end` should close the fight file; `throw` outside a fight should ignore an ended state.
4. `encounter surprise --members …` without `--party`/`--monsters` reads both sides as no foreknowledge and returns
   NO ENCOUNTER with no dice (S38, l. 615): require both flags.
5. No `state set ID damage=…` override for a module statblock whose damage differs from the MM's (S38, l. 617).
6. `camp --hours N` rolled an encounter mid-camp and ran on to the end without stopping (S39, l. 620): stop at the
   encounter's hour as `camp` does in other cases.
7. `roll` refuses compound dice (`1d8+1d12`) (S40, l. 626).
8. `play.py walk --relight ID` does not refuel and relight a burnt-out lantern when its carrier has oil (S40, l. 628).
   The unsettling-event timer expiring inside `walk` does not stop it (S33, l. 567).
9. A magic weapon recovered with `recover --goods` counts only its apparent value and earns no sale XP when sold
   identified (S42, l. 632): refuse `--goods` for a name that matches a magic item, or warn and point to `--item`.
10. Porters and bearers are not adventure participants: a lot they carry has to sit on a member, who then reads as
    overloaded (`move-rate` refuses, `walk` runs on) (S45, l. 652). Add bearer holders that carry lots.
11. `recover --drop` leaves a dropped lot findable at the site; splitting a lot needs `recover --split L# N` (S45, l. 653).
12. A bag of holding (weightless contents past its capacity) cannot be one holder; it is modelled as a cache plus a
    6-st item (S46, l. 662). Add a container kind with a weight cap.
13. Travel members keep `vehicle`/`passenger` after their cart is unharnessed and stabled (S48, l. 674).
14. Actor modifiers for timed spells (Holy Blessing entered as `actor mod`) never expire (S30, l. 549): give
    `actor mod` an expiry (`--until "day N HH:MM"` or `--turns N`) that the clock removes.
15. Typed defenses in SOTN bestiary notes ('status none', 'judge') are not parsed (S34, l. 575).
16. `state aura add … --fail cowering` keeps the condition with no end and rolls again for creatures already immune
    after a success (MM: cower to the next round; immune 1 turn on a success) (S34).
17. `rebuke` does not add Righteous Rebuke's extra Hit Dice (half the level), only its throw modifier (S34).
18. Battle Magic's +1 initiative when casting is not applied (S34).
19. `restore` keeps no record of a failed attempt's side effect; the next attempt's penalties are passed by hand (S34).
20. An actor's `note.save.*` text is printed on any save made at that actor's initiative, not only his own (S29, l. 535).
21. A monster that ignores armor AC (gelatinous mass, MM p. 234: DEX, magic, natural and spell AC only) is attacked
    against full AC (S29, l. 537): read the note's AC rule into the attack.
22. Magic ammunition lots are not tracked: `--ammo-magic N` applies the bonus, but the arrow is taken from the lot by
    hand (OPEN-ITEMS #15).
23. A paralysed party member could be driven to attack by a script (S32, l. 559): make `attack` refuse any attacker
    whose conditions forbid acting (paralysed, slumbering, unconscious, surprised in round 1) whatever the caller.

## E. Decisions for the user (not engine work)
1. OPEN-ITEMS #24: `level-up` re-rolls hp without the permanent enervation losses; a Judge's correction is pending for
   Brennus (26) and Vettius (25) maximum hp (S20).
2. OPEN-ITEMS #43: Kardakia's `tools.ref` (main) and `tools.min_version` (7.11.0) in its `Campaign/campaign.yaml` are
   untouched; the 7.16-7.17 features (and this work) need them raised before Kardakia uses them.
