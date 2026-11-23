# Open items (compiled S28, 2026-11-23)

Source: `Playtest/judge-notes.txt` (findings and slips S13-S28; engine 7.14.0 closed S08-S12), `Playtest/HANDOFF.md`,
this session. Engine = `darkpwns/acks2-tools` (`engine/`), now 7.15.0. Line numbers point at judge-notes.txt.
**Every engine item must be re-checked against the current code before fixing: some may already be closed.**

## A. Engine bugs (acks2-tools)

### Rebuke and undead
1. Felled undead (hp ≤ 0) stay `unconscious`, not destroyed, and `rebuke` spends its Hit Dice on them (S27, l. 505). RR: undead are destroyed at 0 hp.
2. `rebuke` gives its HD to undead already frightened or cowering instead of the next un-rebuked ones (days 274, 317, 423; l. 273, 328, 459).
3. `rebuke` refuses a fractional HD such as `2+1` (S28, l. 515).
4. `rebuke` refuses sepulchral worms ("no undead on the other side") though the MM types them Undead; worms inside a host were also left out of the pool (S18 l. 375, S27 l. 506).
5. Rebuked + engaged/cornered should be `cowering` (vulnerable), not `frightened` (day 272, l. 259).

### Combat
6. `encounter fight` / `state end` never record defeated monsters: `recover --monster` is entered by hand after every fight (S28, l. 516).
7. `state end` does not write party hp back to the actors (day 367, l. 409). Verify; hand-copying is still routine.
8. `encounter fight` does not carry the surprised condition into the combat state (day 354, l. 388; S23 driver slip l. 479).
9. Statblocks with non-numeric fields: Rat Swarm HD and XP `29/65/135` need `--set hd` and `--xp-each` (day 306, l. 304); a note's AC with prose (Abyssal King "11 (mummy 6 + …)") left unset (day 309, l. 316).
10. `damage --extraordinary` against shadows printed "immune to mundane" and applied 0 (day 303, l. 299).
11. A melee weapon attacking at range is resolved as a hit (no reach check) (day 399, l. 435); monsters' thrown weapons default to melee unless `--kind missile` (day 406, l. 439).
12. Multi-attack routine indexes vs damage entries mismatch (giant catfish, `--attack 2` refused) (day 282, l. 277).
13. `state remove` marks a party member "fled"; there is no clean way back (day 309, l. 317).
14. A magic bow's +1 does not make its arrows magical/extraordinary (S28 worm vs Cotta); check TT and fix the tier.
15. No path for thrown flasks (oil, holy water) (day 317, l. 334); no `holy` damage type (day 343, l. 377); no silvered missiles (day 335, l. 360).
16. Surprise penalties in monster notes (shadows −3, sage slime −2) give no JUDGE line, so `--apply-note-penalty` refuses (days 303, 322; l. 298, 339).

### Exploration, time, rest
17. `location --site` resets the wandering counter mid-delve (day 274, l. 270); `location` with no arguments overwrites the location with an empty dungeon (day 330, l. 357).
18. The turns-since-rest counter survives a night in town and long `wait`s (days 305-306, 312-313; l. 303, 314).
19. `light refuel` on a burnt-out lantern takes the flask but does not relight it (day 322, l. 338).
20. The exploration party's `treasure_stone` is not reduced when lots are sold or leave the carrier (day 287, l. 278).
21. Bed rest stops counting while a member is `party remove`d (days 290, 299; l. 285, 290).
22. Slab doors: the engine has no door kind; the Judge passed SOTN's −12 though Rulings S18 dropped it (S18 l. 373, S28). Make door penalties campaign data that rulings can override.

### Characters, items, treasure
23. `actor mod` accepts `proficiency_throws.X` only for throws already on the sheet; class-skill throws (Hiding, Sneaking) cannot be modified, and a non-proficient wearer's flat 12+ (Elven Ranger items) cannot be entered (S28, l. 512). Worn magic items in general are conditions with prose, not modifiers (Ring of Fire Protection was not applied by `damage`, day 221).
24. `level-up` re-rolls hp without permanent enervation losses (days 304-306, S20; l. 308) and applies the new maximum to a character on bed rest (day 268).
25. Retinue wage does not follow level (RR p. 168; S16, l. 324); `retinue set wage=` writes a stray key (day 375, l. 419); the level-up loyalty roll runs at the old wage (day 317, l. 336).
26. `identify --method judge --reveal` leaves `identified` false (days 247, 339, 375; l. 210, 367, 418).
27. `recover --item` naming: "Battle Axe +1", "Short Sword +1", "Spear +1" refused; "Sword +1" drew a dagger; magic weapons, potions and bullets have no apparent value, so `payout` refuses (days 306, 313, 381, 392).
28. Snapshot refuses when an unidentified lot shares a generic true name with an identified one ("Sword +1") (S15, S18, S19; l. 306, 371, 431).
29. `recover --reward` after a payout attaches to the paid-out adventure (day 347, l. 378).
30. Only one adventure can be open; `adventure join` after a refused `start` silently joins the open one (S21, S23, S24; l. 459, 475, 487).
31. Enervation has no engine path: no daily Death save at the rollover, no streak, no pinnacle/Salving Rest modifiers, no max-hp loss (S27-S28; Rulings S10, S14). Build it as a condition the rollover runs.

### Inventory, travel, hiring
32. A spear that breaks its shaft on a natural 1 is removed from the inventory entirely (RR: repairable, 1gp) (day 362, l. 400).
33. `travel` refuses a cart with no driver, and animals and vehicles cannot be left at a stable (day 362, l. 401).
34. `inv add … --as` is ignored (day 331, l. 362); `inv buy torch N` buys N packs (day 273, l. 269); vessels are not in the catalog (day 275, l. 274); no command changes a holder's kind (day 196, l. 117).
35. `recruit` market totals keyed without the month (day 331, l. 358); `candidate --level --class` writes no draft actor (day 331, l. 361).
36. `inv buy --market-class II` still reports "Class III" (day 197, l. 124). Verify.

## B. Module and campaign procedures the engine does not model
37. Area auras with a save at each initiative (the faewyrd's dark whispers, maddened, WIS loss) (S28).
38. Holy Circle and the Underwatch shield ward: per-creature barrier state (Rulings S14: it falls against one creature for the rest of the turn when attacked) (S27-S28 drivers fake it).
39. The weekly surface procedure (Order assignment roll, Brotherhood, betrayers, Watch, city's link, spies, the week's secret) and month's end (fees, investments, the Family's take and hijink XP, Iulia's report) are ad hoc `roll --hidden` lines rebuilt each session from the last log. Make one campaign script driven by a schedule file (`World State` Scheduled events into data).
40. Wage dates: the engine's due dates (Aelia/Marcellus 474, Phaedra 490) differ from the handoff's (473, 489) (S28).

## C. Helpers and skill (sinister-stone-of-sakkara, and the master skill in kardakia-campaign)
41. Playtest/tools holds ~25 one-off helpers (s09…s28): `w` walk, `relight`, `sup`, `bank`, `tday`, fight drivers, ledger copier. Consolidate the proven ones into the skill's `scripts/` with tests; retire the rest. Known helper faults: `w` stops on any timer expiry (S22, S25); the relight test has broken twice (S22, S23); fight drivers resolved actions out of initiative order (S18, S19, S23) and without distances (S28).
42. Payout → Ledger rows copied by an inline loop each session: make `payout --apply` (or save.sh) write them.
43. The 7.15.0 backstab text is only in Sakkara's copy of the skill (`references/combat-totm.md`, `judge-screen.md`); Kardakia's master copy and its `tools.ref`/`min_version` are untouched.

## D. Judge memory: slips that recur after the lesson was recorded
Recorded once, missed again later (each has a judge-notes entry; many have a Ruling):
- `eat --in-town` before every town rollover (S19 deaths; slips S20, S23 day 438).
- After a return: `location --clear`, then the settlement (S17 lesson; repeated).
- `encounter end` before a new encounter (slips days 362, 406); `encounter surprise --members` (day 399).
- Initiative order: actions resolved a count early or late (days 354, 362, 367, 425, 467).
- Surprised combatants acting in round 1 (days 424, 440, 453, 467).
- Spell target counts and HD limits before the saves (days 296, 452).
- Distances set before melee (days 296, 399; S28 G13).
- Backstab (S17 routine, S19 slip check, day 399, day 324 finding; missed again S28; now in the engine).
- Divine Blessing +2 on saves (day 261) and other standing bonuses from items and powers.
- Enervation under the oculus with Salving Rest (Rulings S10, S14; Quirinus S10); missed S27-S28.
- Slab heaves without SOTN's −12 (Rulings S18; missed again S28).
- Henchmen `adventure join --kind henchman` (day 303).
- The Order's weekly roll on schedule (missed day 417).
- NPC rolls hidden, not open (day 429).
- Torches relit on burn-out (days 349, 352, 354, 406, 427, 430).
- Handoff facts copied forward without checking (Thief 9 XP, S22-S23; wage dates S28).

The memory today is prose: Rulings.md (162 rows), judge-notes.txt (523 lines), HANDOFF.md (1,265 lines, each section "supersedes everything above"). Nothing surfaces a lesson at the moment it applies.

## E. Engine speed (measured S28)
- One `acks.sh` call: 1.0-1.5 s (`clock` 1.44 s, `wages show` 1.0 s, `inv show` 1.07 s); a combat round is 20-40 calls, a descent several hundred.
- Python import of the engine is ~30 ms: the time goes to loading and rewriting state and data. State files: exploration 2.3 MB, inventory 1.7 MB, adventure 1.4 MB (all JSON, read and rewritten whole); roll log 4.1 MB / 26,581 lines.
- The larger cost is model round-trips: every roll, turn and attack is one tool call with its own output to read.
