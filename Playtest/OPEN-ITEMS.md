# Open items (compiled S28, 2026-11-23)

Source: `Playtest/judge-notes.txt` (findings and slips S13-S28; engine 7.14.0 closed S08-S12), `Playtest/HANDOFF.md`,
this session. Engine = `darkpwns/acks2-tools` (`engine/`), now 7.15.0. Line numbers point at judge-notes.txt.
**Every engine item must be re-checked against the current code before fixing: some may already be closed.**

## Triage (Phase 1, 2026-11-23)

Every item of sections A and B was reproduced or read in the 7.15.0 code on scratch copies of this campaign (never on
the campaign itself). Of the 40: 27 open in full, 8 partly open (a part already fixed in 7.13.6/7.14.0, or a part that
is no bug), 1 fixed in 7.14.0 (36), 4 not bugs (14, 24, 40 and, as designed, the hp re-roll). Items the triage found
beside the list: `rebuke`'s line hides its 2d6 and who was affected; `throw --prof Climbing` refuses a negative target
("-1+"); `actor show --sources` fails for an inventory holder; a refused `inv buy` loses the month's availability roll;
`wait` in a dungeon runs past an encounter; one light record per `light on` (hundreds of burnt-out torches in `clock`).

Work packages, in the order of what costs play time or correctness most often:

| Order | Package | Items | Why here |
| --- | --- | --- | --- |
| 1 | P1 rebuke, surprise, tiers | 1-5, 8, 10 | every undead fight (most of SOTN): wasted rebukes, surprised foes acting, spells doing 0 to shadows |
| 2 | P1 fight end | 6, 7, 9 | after every fight: monsters and hp entered by hand; hp silently lost when forgotten |
| 3 | P4 exploration | 17-22 | every delve and every town night: rest counter, wandering counter, slab heaves, stale loads, bed rest |
| 4 | P3 modifiers and enervation | 23, 31 | standing bonuses and daily saves the Judge must otherwise remember (section D) |
| 5 | P3 treasure, adventure, wages | 25-27, 29, 30 | every haul and payout: names refused, no apparent value, joins overwriting baselines |
| 6 | P2 missiles, routines, flasks | 11-13, 15, 16 | common but each with a workaround |
| 7 | P5 inventory, stabling, recruiting | 32-35 | occasional |
| 8 | B procedures | 37-39 | auras and wards (driver-faked today), the weekly and month-end schedule |
| 9 | C skill | 28, 41-43 | snapshot check, helpers into `scripts/`, master skill in step |

## A. Engine bugs (acks2-tools)

### Rebuke and undead
| # | Item | Status (engine 7.15.0, checked 2026-11-23) | Package | Finding |
| --- | --- | --- | --- | --- |
| 1 | Felled undead (hp ≤ 0) stay `unconscious`, not destroyed, and `rebuke` spends its Hit Dice on them (S27, l. 505). RR: undead are destroyed at 0 hp. | **open** | P1 rebuke | The damage path destroys undead at 0 hp (RR p. 301, `monster.zero_hp_destroyed`); the fault is `state set ID hp=N` (the drivers' path), which leaves a felled foe `active`, and `rebuke`'s pool, which takes anything active. |
| 2 | `rebuke` gives its HD to undead already frightened or cowering instead of the next un-rebuked ones (days 274, 317, 423; l. 273, 328, 459). | **open** | P1 rebuke | The pool and its HD order ignore an earlier rebuke; RR p. 37 "at least one undead is always rebuked" then fails for the new ones. |
| 3 | `rebuke` refuses a fractional HD such as `2+1` (S28, l. 515). | **open** | P1 rebuke | `float()` on the Judge's `hd`; a 1/2 HD monster also counts as 1. |
| 4 | `rebuke` refuses sepulchral worms ("no undead on the other side") though the MM types them Undead; worms inside a host were also left out of the pool (S18 l. 375, S27 l. 506). | **open** | P1 rebuke | The type is read correctly (MM Sepulchral Worm is Undead); the "rebuked as" reading misses "Rebuke: as skeletons", plurals (mummies), an article ("as a mummy") and Undead Constructs, and an undead with no row drops out with only a NOTE, so the throw goes against the wrong pool. No "inside a host" state exists (MM p. 273: "apart from the host"). |
| 5 | Rebuked + engaged/cornered should be `cowering` (vulnerable), not `frightened` (day 272, l. 259). | **fixed 7.13.6/7.14.0 when engaged; two gaps open** | P1 rebuke | Cowering at the rebuke when engaged (7.13.6) and at `state engage` (7.14.0). Open: an engagement made by a melee `attack` does not convert; no `rebuke --cornered` for an undead that cannot flee (RR p. 37). |

### Combat
| # | Item | Status (engine 7.15.0, checked 2026-11-23) | Package | Finding |
| --- | --- | --- | --- | --- |
| 6 | `encounter fight` / `state end` never record defeated monsters: `recover --monster` is entered by hand after every fight (S28, l. 516). | **open** | P1 fight end | Neither `state end` nor `encounter end` calls the ledger (RR pp. 310-311). |
| 7 | `state end` does not write party hp back to the actors (day 367, l. 409). Verify; hand-copying is still routine. | **open** | P1 fight end | Confirmed: `encounter end` writes hp only to the travel block, and the next `turn` copies the actor's old hp back over it; without the hand step the damage is lost silently. |
| 8 | `encounter fight` does not carry the surprised condition into the combat state (day 354, l. 388; S23 driver slip l. 479). | **open** | P1 rebuke | `encounter fight` does carry it; the first `round-start` deletes every `surprised`, so in round 1 the surprised act (RR p. 282, p. 514). `rebuke` also lacks the cannot-act check. |
| 9 | Statblocks with non-numeric fields: Rat Swarm HD and XP `29/65/135` need `--set hd` and `--xp-each` (day 306, l. 304); a note's AC with prose (Abyssal King "11 (mummy 6 + …)") left unset (day 309, l. 316). | **open** | P1 fight end | HD ranges and XP alternatives need the Judge's HD; AC and XP written "N (prose)" are refused though the number is there (MM 23 AC / 49 XP, SOTN 10 / 13, AX3 32 / 25 notes). The XP table value quoted in the refusal is wrong (counts both asterisks of a range). Rat Swarm's AC reads correctly. |
| 10 | `damage --extraordinary` against shadows printed "immune to mundane" and applied 0 (day 303, l. 299). | **open** | P1 rebuke | An explicit `--extraordinary` on non-weapon damage is downgraded to mundane against any incorporeal creature (MM p. 19 is about natural and non-magical weapons). |
| 11 | A melee weapon attacking at range is resolved as a hit (no reach check) (day 399, l. 435); monsters' thrown weapons default to melee unless `--kind missile` (day 406, l. 439). | **open** | P2 missiles | Melee at range resolves only when no distance is recorded (with one it is refused). Monsters never get a missile kind or range band; `--kind missile` throws a sword and leaks a KeyError. |
| 12 | Multi-attack routine indexes vs damage entries mismatch (giant catfish, `--attack 2` refused) (day 282, l. 277). | **open** | P2 missiles | 19 MM statblocks: attack names outnumber damage pieces (6 by groups, 13 with one piece); 6 more need the Judge. |
| 13 | `state remove` marks a party member "fled"; there is no clean way back (day 309, l. 317). | **open** | P2 missiles | Also: any status string is accepted (typos), and a removed party member counts as a casualty for hireling morale. |
| 14 | A magic bow's +1 does not make its arrows magical/extraordinary (S28 worm vs Cotta); check TT and fix the tier. | **not a bug (Judge slip)** | P2 missiles (note only) | A magic bow already makes the attack extraordinary (TT p. 51 "All magic weapons deal extraordinary damage"; TT p. 251). In S28 the +1 long bow (w72) was on Cotta's belt, never wielded; he shot the mundane composite bow (w67). The engine will now name a carried magic missile weapon on such a shot. |
| 15 | No path for thrown flasks (oil, holy water) (day 317, l. 334); no `holy` damage type (day 343, l. 377); no silvered missiles (day 335, l. 360). | **flasks open; `holy` not a bug; silver missiles: buying not a bug, damage open** | P2 missiles | Flasks: COVERAGE lists RR p. 298 as "later". No `holy` type in the RR's twelve (RR p. 299): holy water is extraordinary luminous (RR p. 298), which `--type luminous --extraordinary` applies. "1 Silver Arrow" is its own row (RR p. 126) and can be bought and shot, but the silver is lost at damage; magic ammunition cannot be shot with its bonus (TT p. 251). |
| 16 | Surprise penalties in monster notes (shadows −3, sage slime −2) give no JUDGE line, so `--apply-note-penalty` refuses (days 303, 322; l. 298, 339). | **open** | P2 missiles | The note filter drops "vs it", "against it", "vs stationary ones" (Shadow, Sage Slime, crab spiders, tarantula, animated statues). |

### Exploration, time, rest
| # | Item | Status (engine 7.15.0, checked 2026-11-23) | Package | Finding |
| --- | --- | --- | --- | --- |
| 17 | `location --site` resets the wandering counter mid-delve (day 274, l. 270); `location` with no arguments overwrites the location with an empty dungeon (day 330, l. 357). | **open (both)** | P4 exploration | The counter belongs to the delve (JJ p. 36). |
| 18 | The turns-since-rest counter survives a night in town and long `wait`s (days 305-306, 312-313; l. 303, 314). | **open** | P4 exploration | `wait` is not rest; outside a dungeon nothing resets the counter (RR p. 271). Live state: 4 turns since rest at day 477 in town. `wait` in a dungeon also runs past an arriving encounter. |
| 19 | `light refuel` on a burnt-out lantern takes the flask but does not relight it (day 322, l. 338). | **not a bug (designed, 7.14.0); one stale line open** | P4 exploration | Filling and lighting are separate (RR p. 146); 7.14.0 says NOT LIT. Still printed: "deduct it from the carrier's gear" though the inventory took the flask. `refuel --light` added as a convenience. |
| 20 | The exploration party's `treasure_stone` is not reduced when lots are sold or leave the carrier (day 287, l. 278). | **open** | P4 exploration | Stale for 10 of the 12 in the live state (Neris 7.67 st against 1.67 carried). |
| 21 | Bed rest stops counting while a member is `party remove`d (days 290, 299; l. 285, 290). | **open** | P4 exploration | The rollover walks only the present party; natural healing is skipped too. |
| 22 | Slab doors: the engine has no door kind; the Judge passed SOTN's −12 though Rulings S18 dropped it (S18 l. 373, S28). Make door penalties campaign data that rulings can override. | **open (feature)** | P4 exploration | The engine's numbers are the RR's (p. 267); a module's door enters only as a free `--mod`. The slip recurs because `Nethercity Features.md` and `SOTN Hub.md` still print the −12 and are read before Rulings.md. |

### Characters, items, treasure
| # | Item | Status (engine 7.15.0, checked 2026-11-23) | Package | Finding |
| --- | --- | --- | --- | --- |
| 23 | `actor mod` accepts `proficiency_throws.X` only for throws already on the sheet; class-skill throws (Hiding, Sneaking) cannot be modified, and a non-proficient wearer's flat 12+ (Elven Ranger items) cannot be entered (S28, l. 512). Worn magic items in general are conditions with prose, not modifiers (Ring of Fire Protection was not applied by `damage`, day 221). | **open; the Ring of Fire Protection part fixed 7.14.0** | P3 modifiers | Modifiers reach attack throws, saves, AC and attribute modifiers only; no throw can be modified and no flat throw entered (TT p. 151 cloak, p. 140 boots). Typed protections work through the actor's `defenses` (7.14.0), in a fight only. |
| 24 | `level-up` re-rolls hp without permanent enervation losses (days 304-306, S20; l. 308) and applies the new maximum to a character on bed rest (day 268). | **not a bug (hp re-roll); bed rest fixed 7.14.0** | — | The engine follows the book: the re-roll with full Hit Dice replaces the reduced maximum when higher (MM pp. 17-18 example: 19 → 30; RR p. 509); nothing is subtracted afterwards. **The Judge's hand reading (Brennus 26 → 23, Vettius 25 → 22) is not the rule and is no ruling: a Judge's correction to decide (judge-notes S29).** |
| 25 | Retinue wage does not follow level (RR p. 168; S16, l. 324); `retinue set wage=` writes a stray key (day 375, l. 419); the level-up loyalty roll runs at the old wage (day 317, l. 336). | **wage by level open; stray key open; loyalty roll not a bug** | P3 treasure | The level's loyalty roll has no wage term (RR pp. 166-168): Gnaeus' natural 2 was Resignation at any wage. `level-up --mod` added for the Judge's adjustment. |
| 26 | `identify --method judge --reveal` leaves `identified` false (days 247, 339, 375; l. 210, 367, 418). | **fixed 7.14.0 without `--reveal`; with `--reveal TEXT` open** | P3 treasure | Only the literal `--reveal identity` identifies. |
| 27 | `recover --item` naming: "Battle Axe +1", "Short Sword +1", "Spear +1" refused; "Sword +1" drew a dagger; magic weapons, potions and bullets have no apparent value, so `payout` refuses (days 306, 313, 381, 392). | **naming open; "Sword +1" drew a dagger: not a bug; apparent value open** | P3 treasure | "Sword +1" is the TT's generic entry and rolls the Sword Type table (TT pp. 51-55): a placed item will now need its type. The vault does give the apparent value the engine says is missing: 650gp plus the mundane item's cost; a magic projectile 32.5gp (TT Swords, Miscellaneous Weapons, Armors). **Rulings S14 (mundane equivalent) is lower than the book: stays a campaign ruling (engine-rulings.yaml) if kept.** Potions were not reproduced (25gp). |
| 28 | Snapshot refuses when an unidentified lot shares a generic true name with an identified one ("Sword +1") (S15, S18, S19; l. 306, 371, 431). | **open (skill: snapshot.py, both copies)** | C skill | The check searches the whole snapshot text for the true name and ignores the lot's status: an identified twin, a weapon on a sheet or a longer name trips it. |
| 29 | `recover --reward` after a payout attaches to the paid-out adventure (day 347, l. 378). | **open** | P3 treasure | `recover`, `join` and monsters never check for a paid adventure; a late reward has no XP path. |
| 30 | Only one adventure can be open; `adventure join` after a refused `start` silently joins the open one (S21, S23, S24; l. 459, 475, 487). | **open (join overwrites a participant); one open adventure is by design** | P3 treasure | `join` on an existing participant resets his one-level-cap baseline. Several open adventures stay a design limit; the late-reward path answers contracts. |
| 31 | Enervation has no engine path: no daily Death save at the rollover, no streak, no pinnacle/Salving Rest modifiers, no max-hp loss (S27-S28; Rulings S10, S14). Build it as a condition the rollover runs. | **open (nothing built)** | P3 enervation | RR p. 509, MM pp. 17-18, RR p. 242 (Salving Rest), JJ pp. 89-90 (pinnacles). |

### Inventory, travel, hiring
| # | Item | Status (engine 7.15.0, checked 2026-11-23) | Package | Finding |
| --- | --- | --- | --- | --- |
| 32 | A spear that breaks its shaft on a natural 1 is removed from the inventory entirely (RR: repairable, 1gp) (day 362, l. 400). | **open** | P5 inventory | RR p. 127 (Long): the shaft breaks, 1gp to repair, usable meanwhile as an off-balance dagger and/or staff. A magic spear was lost with it. |
| 33 | `travel` refuses a cart with no driver, and animals and vehicles cannot be left at a stable (day 362, l. 401). | **driverless cart: not a bug; stabling open** | P5 inventory | A vehicle needs its driver (RR p. 134); a cart is left behind with `inv unharness`. No command takes an animal off the march (RR p. 131 stabling fees). |
| 34 | `inv add … --as` is ignored (day 331, l. 362); `inv buy torch N` buys N packs (day 273, l. 269); vessels are not in the catalog (day 275, l. 274); no command changes a holder's kind (day 196, l. 117). | **`--as` open; torch packs not a bug; vessels not a bug; holder kind fixed 7.14.0** | P5 inventory | `inv buy ID ITEM [PACKS]` is documented (RR "Torches (6)"); the refusal will say the packs. Vessels are outside the catalog by COVERAGE (`inv define`). |
| 35 | `recruit` market totals keyed without the month (day 331, l. 358); `candidate --level --class` writes no draft actor (day 331, l. 361). | **month key open; draft actor not a bug** | P5 inventory | Totals are keyed without the month and the once-a-month limit (JJ p. 118) is only a note: every retry charges a fee and rolls again. The draft is written with `--sheet` (documented); a default folder added as a convenience. |
| 36 | `inv buy --market-class II` still reports "Class III" (day 197, l. 124). Verify. | **fixed 7.14.0** | — | Verified with and without a market note. New finding: a refused `inv buy` loses the month's availability roll, so a retry re-rolls it (P5). |

## B. Module and campaign procedures the engine does not model
| # | Item | Status (engine 7.15.0, checked 2026-11-23) | Package | Finding |
| --- | --- | --- | --- | --- |
| 37 | Area auras with a save at each initiative (the faewyrd's dark whispers, maddened, WIS loss) (S28). | **open (not modelled)** | B auras | As run in S28 the save was rolled at the faewyrd's initiative on two random hearers; SOTN pp. 142-143 has every hearer save at the start of its own initiative, −1 per extra faewyrd, and the maddened lose 1 WIS each initiative (not applied). |
| 38 | Holy Circle and the Underwatch shield ward: per-creature barrier state (Rulings S14: it falls against one creature for the rest of the turn when attacked) (S27-S28 drivers fake it). | **open (not modelled)** | B wards | RR p. 225: the barrier bars natural attacks and expires as a whole; Rulings S14 makes it per creature, for the rest of the turn. The three drivers each fake it differently (never, per round, forever). |
| 39 | The weekly surface procedure (Order assignment roll, Brotherhood, betrayers, Watch, city's link, spies, the week's secret) and month's end (fees, investments, the Family's take and hijink XP, Iulia's report) are ad hoc `roll --hidden` lines rebuilt each session from the last log. Make one campaign script driven by a schedule file (`World State` Scheduled events into data). | **open (not modelled)** | B schedule | As played: three clocks (the Order's roll days ≡ 4 mod 7; the weekly block days ≡ 1 mod 7; month's end every 30 days) plus dated items. Several lines have no ruling or an undefined consequence (listed in the schedule file). |
| 40 | Wage dates: the engine's due dates (Aelia/Marcellus 474, Phaedra 490) differ from the handoff's (473, 489) (S28). | **not a bug (engine right)** | — | Due day = hiring day + k × 30, paid in advance (RR p. 168; reading `wage.timing`): Aelia and Marcellus 474/504, Phaedra 490. The handoff's 473/489/503 are the engine's "paid through day N" read as the due day. Paying a day early is harmless. |

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
