# Sakkara playtest — handoff (2026-11-20)

Playtest of AX1 *The Sinister Stone of Sakkara* as a campaign of the `acks2-judge` skill, engine 7.12.0+.
`REPORT.md` is the per-delve log; `judge-notes.txt` the voids, slips and Judge's calls; `campaign/` the full instance
(state, actors, roll log, module notes in `campaign/Adventure/`); `tools/` the playtest helpers.

## Where play stands (superseded: see the S06 update below)
- Day 95, 23:00. Party inside the Buried Temple at **L1 75** (the dead dragon's vault under the ziggurat), at the head
  of the 35' stair down to **L2 room 1** (the catacombs). Torch put out at the save; relight on resume.
- In the delve: Aulus (F2), Sabina (Cru3), Tarq (Bar2), Lucilla (Ven3), Vettius (Thf3), Marcia (Mag2, Fan of Flames,
  Blinding Flash, Sleep), Gallus (Ven2), Thorwell, Thorcigar (F1), Quintus (F1), Vestus (M1), Zaira (ElvSpellsword 1).
  Hesper (F1) keeps camp at the stream in 10.07 with the donkey.
- Adventure A6 "Buried Temple, delve 6 (the catacombs)" open. Coins banked in town (`karanos-bank` cache).
- Next: descend to L2 1; plan was 1 → rubble passage → 22 Outer Fane (Ur-Namu, 4 catechists) → Lake of Blood 20 → 36
  → 38 Inner Fane (Zakiti, the Stone). Rebuke undead untested so far (Sabina). Legate's 2,000gp reward needs the
  Stone destroyed.

## Resuming
1. Clones at /home/user/{acks2-tools,acks2-rules-vault,kardakia-campaign} on branch claude/sakkara-adventure-playtest-7kql1w;
   `mkdir -p /home/claude && ln -s /home/user/<repo> /home/claude/<repo>` for each.
2. Recreate the instance: copy `campaign/` to /home/user/sakkara-playtest, `git init`, then lay the skill in with
   `bash /home/user/acks2-tools/campaigns/new_campaign.sh <empty kit dir> /home/user/sakkara-playtest /home/user/kardakia-campaign/.claude/skills/acks2-judge`
   (or copy `.claude/skills/acks2-judge` from kardakia-campaign). Run `bash .claude/skills/acks2-judge/scripts/setup.sh`.
3. `. tools/j.sh` (edit the paths at the top: `cd /home/user/sakkara-playtest`; melee.py path) gives `t`, `r`, `loc`,
   `door`, `meet`, `brawl`, `walk`.
4. Party decisions follow `campaign/Party/heuristics.md` and the profiles; the party agent was used once (step 1).

## Engine 7.13.0 (2026-11-20)
Built: magic armor lots worn on `inv claim` (Lucilla's chain mail L28 now worn, AC 6; stand-in removed with
`actor unmod`); `spellcasting` (hired castings); `encounter start --npc` for town reactions; `disease
expose|diagnose|cure|show` with stages on the day rollover; starvation/thirst deaths ask `death` and mark the actor;
`party add` during travel warns on missing supplies (the cause of the henchman losses). Encumbrance difficulty is
intended: use mules, porters, wagons. `min_version` in the instance is 7.13.0.

## S06 update (second chat, 2026-11-20)
- Day 97, 11:08, camped in forest hex 11.07 (on course), marching to Türos Tem (13.08) via 12.07, `--retrace`. No food at all; skins full except Quintus, Vestus, Zaira, Hesper (no skins; drink at sources: `water` once a day in 11.07, 12.07, 13.08). Everyone hungry or underfed.
- Sabina is 10 st with 1.2 days of water (9 st without): she halves the column's speed unless the load is shifted.
- Hesper is now in the exploration/travel party (`party add hesper`). The location is cleared (outside the temple).
- Party agent: Table talk dropped from the declaration (Party/prompt/base.md); `party.py` wall fix (rumours heard count as player-facing) is in kardakia-campaign's skill copy; copy `.claude/skills/acks2-judge` from there when recreating the instance.
- Call dir: `campaign.yaml party.agent.call_dir` points at the current chat's scratchpad; reset it each chat.

## S06 end (2026-11-21, after the replay)
- Day 138, Türos Tem, all healed. The Lady Below (Zakiti) lives at 7 hp (heals) and holds the Stone again; she knows the party. Undead: 8 zombies (two scorched) with her; skeletons of 34 destroyed; Ur-Namu and the acolytes of 22 dead but four new acolytes there (weekly replacement rolls). Ogres dead; Black Fangs friendly.
- Party: Aulus F2, Sabina Cru3, Tarq Bar2, Lucilla Ven3, Vettius Thf3, Marcia Mag2; henchmen Hesper F1, Thorwell F1 (Tarq's), Quintus F1, Vestus M1, Zaira ES1 (one leg). Dead: Gallus, Thorcigar (Characters/former/).
- Lots carried: L58 sword +1 (Aulus, unidentified). Black Fang chest (L2 9), the Lady's chest (L2 39, needle trap), Red Eye loot (L2 15), Drusus (L1 17) all unplundered.
- The first playing of rounds 9+ (surrender, legate's reward, 10,000 Fragment XP, Tarq's death) is void; its rolls stay in the roll log (judge-notes).
- Party agent not used after S06 step 4 (user: Judge plays the party by the profiles and heuristics; no table talk).
- Helpers: tools/fight.py (melee driver with latch and first strike) and tools/day.sh.

## S07 end (2026-11-21)
- Day 161, 06:00, Türos Tem, all healed. **The Lady is dead and the Stone destroyed** (day 142); the legate paid; the Fragments went to Genelen (Mityara's order). The adventure's goal is done; the test continues until a TPK.
- Party: Sabina Cru4 (one eye), Tarq Bar3 (one hand: no two-handed weapons; -10% XP; raspy voice), Lucilla Ven4 (Ring of Fire Protection unidentified, L63), Vettius Thf4 (Deciphering now; carries L47 Death Drinker, L58 sword +1, L31 temple map, L45 scroll, the Lady's unholy symbol), Vestus M1 (3 hp max), Hesper F2 (camp keeper), Zaira ES1 (one leg; stays in town). Genelen is an NPC actor (Actors/npc/priestess-genelen), in the exploration party; she is back at her hospital (remove her with `party remove` before the next march unless she comes).
- **Owed next chat:** two new 1st-level PCs to replace Aulus (Gideon) and Marcia (Priya), built with `acks chargen` (R/characters.md); new henchmen for Tarq/Aulus' successors (recruit). Wages: Vestus and Zaira due day 174, Hesper day 182.
- L2 left: bodies of Aulus, Marcia, Thorwell, Quintus and the Lady (plate +1) in 38 with their gear (`body:` holders); 5 skeletons + 13 zombies at their posts (34, 35, 23); 9 catechists in 22; the Lady's chest (39), Black Fang chest (9, Ur-Shet now Indifferent), Red Eye loot (15), abominations and their nest loot (19), bone lair wand (37), Drusus (L1 17, 750gp bounty). No more replacements (the Lady and the Stone are gone).
- Adventure A8 paid. Open the next adventure before any delve.
- Helpers this chat (scratchpad, not kept): und2.py (undead driver with per-undead target lists; resolve cleaves). The Lady's arcane strike and weapon-focus doubling were done by hand (`damage --dice 1d1 --mod`).
- Engine 7.13.3 on claude/eager-turing-48ne25; min_version 7.13.3.

## Between adventures (2026-11-21, after S07)
- **AX1 is complete.** Day 161, summer (calendar: 30-day months, 3 months a season, spring from day 1; engine 7.13.4 turns the season at the rollover). Türos Tem, hex 22.20 on the AX3 Borderlands sheet (renumbered after S07; old AX1 numbers ≈ +9, +12). `Adventure/Region Map.md`: grid, what is built (150 hexes: the Türos Tem block and the east road to Cyfaraun 18.05, 23 hexes via Türos Aster, Spen and Orn), and how to extend it.
- Campaign State `adventure: between adventures`: start the next module with `R/bootstrap.md` → A new adventure in a running campaign (keeps Table rules, inventory, retinue, rulings, travel block).
- **Party going on:** Sabina Cru4 (Ingrid), Tarq Bar3 (Kwame; one hand, -10% XP), Lucilla Ven4 (Rosa), Vettius Thf4 (Tomasz), henchman Hesper F2 (Lucilla's; wage due day 182). In the exploration party in Türos Tem, healed. Their coins and bank deposits are theirs (bank 13,732gp: see World State).
- **New characters owed:** Gideon and Priya (Aulus and Marcia died). Starting XP (RR Character Death; never more than the prior character's):

  | Player | Prior character (Characters/former/) | Prior XP | Reserve | Funeral | New character starts with |
  | --- | --- | --- | --- | --- | --- |
  | gideon | aulus (dead) | 3,610 | 0 | 1,337 | 1,337 |
  | priya | marcia (dead) | 3,543 | 0 | 1,989 | 1,989 |

  Run `death <prior> --new-character --player <p> --prior-xp <xp>` when each is made (it consumes the funeral XP), then `actor set <id> xp N` and `level-up --sheet <id> --apply` per level reached. Ingrid, Kwame, Rosa and Tomasz have no reserve funds yet.
- Free NPCs in town: Zaira ES1 (retired, one leg), Vestus M1 (rehire by offer); Genelen (Priestess 6, Friendly, actor Actors/npc/priestess-genelen).
- Engine 7.13.4 on claude/eager-turing-48ne25 (min_version 7.13.4). Skill: bootstrap.md new section and xsync season sync, also in kardakia-campaign on claude/eager-turing-48ne25.

## Next session: the journey to Cyfaraun (Secrets of the Nethercity) (done in S08: see the S08 section at the end)
**State on resume (day 161, 06:00, summer, Türos Tem 22.20):** Campaign State `adventure: between adventures`; the
engine's clock, travel block (hex 22.20, believed 22.20, season start spring day 1), inventory, retinue and the hex map
are ready. Engine 7.13.6 (`min_version`; rebuke, note initiative bonus, attack --extra-dice/--double-on-20, food sharing, water --source, early-resolved encounter: see references/judge-screen.md). No open adventure; no combat or encounter open.

**Party (six PCs, no henchmen):**
| Player | PC | Notes |
| --- | --- | --- |
| Ingrid | Sabina, Crusader 4 | one eye (-2 missiles) |
| Kwame | Tarq, Barbarian 3 | one hand (no two-handed weapons), skull wound (-10% XP), raspy voice |
| Rosa | Lucilla, Venturer 4 | lost an eye and an ear; Ring L63 unidentified |
| Tomasz | Vettius, Thief 4 | Deciphering now; carries L47, L58 (swords), L31 (temple map), L45 (scroll), the Lady's unholy symbol |
| Gideon | Hesper, Fighter 2 | Lucilla's henchman, taken over (Aulus died; his Quintus too) |
| Priya | Vestus the Unlikely, Mage 1 | Marcia's henchman, taken over (Marcia died) |
Table rule (S07): a dead PC's player takes over that PC's henchman; else a second-level henchman in the party; else a new
character with reserve XP. No second-level henchmen are free in town (Zaira ES1 retired, one leg); recruiting one is a
week's search in Türos Tem (class V): Lucilla (Ven4) and Sabina (Cru4) may hire up to 2nd level.

**Hook (user, 2026-11-21):** the party has learned what a priestess is worth (Genelen in S02 and S07; see
`Party/heuristics.md` "A priestess is worth a dozen swords") and goes to **Cyfaraun to hire a priestess henchman**:
Genelen will not leave her hospital and order, and Türos Tem (class V) has no henchman above 2nd level. Cyfaraun is
class III: henchmen 1st 1d4, 2nd 1d3, 3rd 1 (85%), 4th 1 (45%) per week's search (1d8+5gp per type), and the
Keepers of the Hearth Fire (Mityara's clergy, Matriarch Aundëmë; `Adventure/AX3/City/Temple District.md`) are where
a priestess candidate is found or vouched for (Judge's call: a letter from Genelen gives +1 or +2 on the hiring
reaction there). The Nethercity follows once the party is in the city. Lucilla (Ven4) and Sabina (Cru4) can hire
up to 3rd level by the RR henchman-level rule (Judge checks with `recruit`).

**Before marching (town, R/town.md):** food is 0 for all but Tarq (1.5 d). A new market month began on day 151:
buy iron rations (they keep), fill waterskins (`water`), torches and oil for the Nethercity; consider mules or a cart
(speeds: Sabina, Tarq, Lucilla, Vettius 12 mi/day; Hesper 18; Vestus 24). Two donkeys (donkey1, donkey2) are with the
party. Bank (Karanos): Sabina 2,242, Tarq 2,200, Lucilla 2,030, Vettius 2,244, Hesper 1,773 gp.

**The march (R/overland.md):** the east road, all on road (no navigation throws on a road), 23 hexes, 138 miles;
forts to resupply at each leg's end (`eat --in-town` and buying there need market notes: none written yet for
Aster, Spen or Orn; Türos Orn is class IV, Cyfaraun class III per the JJ):
```
travel --route 23.20,24.19,25.19                                   # Türos Aster (#29), 3 hexes
travel --route 26.18,26.17,27.17,28.16                             # Türos Spen (#22), 4
travel --route 27.16,26.15,26.14,25.14,25.13,24.12,24.11,23.11,23.10   # Türos Orn (#15), 9
travel --route 22.09,21.09,20.08,20.07,19.07,18.06,18.05           # Cyfaraun (#10), 7
```
(`travel` continues a route in progress with `travel` alone after a camp or an encounter.) The map is built for the
whole region (columns 14-31, rows 2-24: 414 hexes, five roads), so detours and a lost party stay on it. Buying at the
forts: `inv buy … --market "Turos Aster" --market-note "Adventure/Markets/Turos Aster (Market).md"` (likewise Turos
Spen, Turos Orn, Cyfaraun); market classes VI, VI, IV, III.

**Written (S07):** notes and market notes for Türos Aster, Türos Spen, Türos Orn and Cyfaraun (from AX3 and the JJ).
**Not built yet:** the SOTN module notes (needs its own chat: the `module-vault` skill on Library
`Adventures/_source/Secrets_of_the_Nethercity.pdf`: hub with `Running …` lines, level keys, tables), and AX3's city
detail for Cyfaraun (districts, encounters, rumours). Open the adventure (`adventure start --name "Secrets of the
Nethercity"`, `adventure join` each PC) before the first delve.

## S08 (2026-11-21) — start here (supersedes "Next session" above)
**Branch:** S08 is on `ccr-6e7c0096-7nmfvu` (pushed), not the default branch. Check that branch out (or merge it into
the default) before resuming, or the instance resumes from day 161. The same branch name exists (no changes) in
kardakia-campaign and acks2-rules-vault; acks2-tools stays on `claude/eager-turing-48ne25` (7.13.6, unchanged).

**State on resume:** day 186, 08:20, fall (season turned day 181), Cyfaraun (18.05), mode town, Silk Pony Inn
(Festival District #25; beds 2sp, paid through the night of day 185 — pay each night: `inv pay lucilla 1gp 4sp`).
Adventure A9 "Secrets of the Nethercity (journey to Cyfaraun)" open: all PCs and Neris, Ottar joined. No combat or
encounter open. Session log `Session Log/S08 — The road to Cyfaraun.md` (continue it, or close it as S08 and open S09).

**Party (8):** Sabina Cru4 16/16 (1 of 2 spells used today), Tarq Bar3 13/13, Lucilla Ven4 19/19, Vettius Thf4 12/12
(spine restored day 171, no side effect; bed rest done), Hesper F2 10/10, Vestus M1 3/3; henchmen **Neris** (Priestess 1,
Sabina's, 35gp/month, STR 4, 4 hp, both spells used today; Healing proficiency not on the actor) and **Ottar** (0th,
Lucilla's torch-bearer, 12gp, 2 hp, 12 torches). Wages paid through day 204. Food 7-22 days each, skins full.
Animals (mule1 + cart1, donkey1, donkey2) stabled at the Silk Pony, paid through day 188: they stay in town for a
delve (`party` still lists them in the travel block's animals; nobody rides: Hesper and Vettius were seated in cart1 —
`mounts dismount cart1 --rider hesper` / `vettius` before walking, and check `mounts show`: dismount has left stale riders twice).

**Threads (player-facing):** Genelen's letter was coldly received by a sister of the Hearth Fire (Unfriendly); a
priestess henchman found anyway. Rumours (Session Log/Rumours Heard.md): Argollëan Family vs Sand & Bones; Silk Pony
blood sports; the Order of the Eclipse and the river bodies; **Tavus Ionicus with the lepers in the undercity** (the
pointed lead: AX3 rumour 20 → Vagrant Colony #75u, his body, drawings and note). Party intent: down through an Old
District sewer grate into the Undercity, toward the lepers and what lies beneath.

**Next:** load R/dungeon.md and R/encounters.md; the Undercity is AX3's (`Adventure/AX3/AX3 Hub.md` "Running Undercity
of Cyfaraun"; Old District throw 5+; [[Undercity of Cyfaraun]]); the Nethercity proper via Old District #12u =
Nethercity A1 (`Adventure/SOTN/SOTN Hub.md`: `acks.sh location --hub "Adventure/SOTN/SOTN Hub.md"` for the sewer caves;
unsettling events every 12 turns; sludge miasma). Light the torch (`light on --kind torch --carrier ottar`). In town every
day: `eat --in-town` **before** each rollover (`wait`), else the travel block starves and dehydrates the party (S08 slip,
corrected). Rulings added in S08: Genelen's letter (+1/+2), farmstead wells on roads, pointed rumour questions.

**Engine findings S08** (Playtest/judge-notes.txt): `mounts dismount` leaves riders_st (twice, fixed by hand);
`spellcasting` crashes on a null retinue `spellcasting` record (set to {}); `mortal-wounds` outside a fight needs a
combat state, `state set ID status=unconscious` and `--type`; passenger bed rest under a healer is never credited on
travel days (only rest-day sets cared_by); `wait` in a settlement eats carried supplies (use `eat --in-town`); a hired
henchman's proficiencies cannot be set; campaign tables (Adventure/**/Tables/*.yaml) are not found by `acks table roll`
(roll 1d20 and read the row); `throw ID --prof climbing` has no recorded target (use `--target 8`).

## S08 continued (2026-11-21) — day 194 (supersedes the S08 "start here" state above)
- Delve 1 (day 187): grate → A1 (carrion horror driven off, later eaten by the A4 creeper) → A2 swarm burned → A4 door → D1-D7 walked (D5 graves looted L68 48gp; D6b secret door found, not opened: 48 skeletons; troglodytes warned). Way out: 3 rhagodessas (Undercity) killed **Sabina, Tarq, Hesper** (devoured; Characters/former/). Gear, coin and lots recovered day 189; heroic funerals paid from their coin (Ingrid +714, Kwame +775, Gideon +365 funeral XP).
- Successors: **Ingrid → Neris** (Priestess 1, PC); **Kwame → Brennus** (new Fighter 1, Ravager, 775 XP; lost an ear); **Gideon → Iulia** (new Crusader 2, Priest template, 1,702 XP). User's ruling: new PCs start at 1st level; higher-level help is hired.
- Hired day 190: **Quirinus** (Fighter 2, Lucilla's, 50gp) and **Phaedra** (Mage 1, Slumber, Vettius', 40gp). Ottar (0th) still Lucilla's. Caller now Rosa (Lucilla).
- Delve 2 (day 191): A3 swarms burned (87 XP), prawns fled, graves L69 30gp; C1 (3 swarms + 12 shrieking locusts) seen, party withdrew for oil. A3: a sage slime on the ceiling by the east opening (wandering result).
- Day 192: shriekers in the tunnel drew 3 more rhagodessas: 2 slain (430 XP), 1 fled. Days 193-194 healing.
- **Now:** day 194 ~06:30, Silk Pony. All at full hp except as cured; Neris and Iulia 1 spell left each today; Phaedra and Vestus full. Oil: military Brennus 2, Iulia 2, Quirinus 2; common Lucilla 4, Vettius 4; holy water 2 (Iulia). Adventure A9 open: lots L68, L69 + Sabina's L5/L30/L43/L44/L46 (Neris), L62 great axe (Vettius), magic mace and axe (Lucilla); monster XP 652 so far.
- Helpers (scratchpad, recreate): cond.sh (append/remove one condition: `actor set state.conditions` replaces the whole list), miasma.sh (hourly +4 Death saves for the party), tr.sh (travel line filter).
- Engine findings added: Tarq's Arena Armor read as AC 1 (set ac in combat state); monster statblocks with prose damage ("1 piercing", "grab", "2d8 piercing") need `attack --no-damage` + `damage`; AX3/SOTN bestiaries were not in tools.bestiary (added); shriekers' drawn wanderer re-rolled when it repeated.

## S08 continued — day 195 afternoon (supersedes the day-194 block)
- Delve 4 (day 195): in by the **second grate** (Rulings S08: 150' from the Emporium grate, past the shriekers, 150' from 12u: the party's contingency, Party/party-notes.md); Horned Rat wererats (Friendly) passed through 12u and took the hole for a drain; A4 creeper burned (65 XP); rope down the A4 cliff (no throw, Rulings); C2a crossed wide of the moulds; E1/E2 doors forced; graves looted E2a, E2c, E4b, E5, upper E4c, E6b (L70-L75); 11 giant rats (Neutral) and 9 sarcophagal worms avoided; out by the second grate.
- **Payout applied** (A9): 654 treasure + 912 monster XP over 7.5 shares. Open a new adventure (`adventure start`, `join` all nine) before the next delve.
- Left unlooted: C1 graves (48gp; grey ooze there, fire-immune: only weapons, destroys armour), E4c lower 40 graves (80gp, near the troglodytes of I), E6a 40 graves (80gp, worms there); D6b alcove (48 skeletons wake); D5 altar vault (slab -12, jackals); B1 slab; mummy tombs E3, E7-E8, E9, D2.
- Oil left: military Brennus 1, Iulia 1, Quirinus 0... check `inv show`; common Lucilla 3, Vettius 0-1. Market month 181-210: military oil bought 20 so far.
- Party: Lucilla Ven4, Vettius Thf4, Vestus M1, Neris Pr1 (Ingrid), Brennus F1 (Kwame), Iulia Cru2 (Gideon); henchmen Ottar 0th, Quirinus F2 (Lucilla's), Phaedra M1 (Vettius'). Lodging Silk Pony: pay 1gp 8sp a night; `eat --in-town` before each town rollover.

## S08 continued — day 196 evening (latest)
- Lucilla now uses her venturer powers (user, S08): Rulings S08 row (Mercantile Network, Bribery `--bribe`, Rumormongering on a return visit, Magical Engineering on new items, Knowledge (history) where keys name it); trade route Cyfaraun - Türos Tem (textiles, clothing) in World State; Party/memory/rosa.md. L63 Ring of Fire Protection identified and worn; L58 sword +1 and L44 philter identified; L62, L43, L5, L47 unknown to her.
- Delve 5 (A10, paid out day 196: 168 treasure XP): E6a graves (L76 80gp), F1 frescoes (Iulia), F2 graves (L77 88gp). Not entered: F3/F5 (12 skeletons + mummy curate), F4 (mummy cultist, undead swarm, worms), the F11 gallery (128 skeletons wake for anyone carrying F-tomb treasure).
- Still lootable at low risk: E4c lower 40 graves (80gp, near troglodytes), C1 24 graves (48gp, grey ooze there). Everything else left is a mummy tomb, a skeleton-guarded vault or deeper levels (G, H, I troglodyte tribe, L, M...).
- Now: day 196 ~17:10, Cyfaraun, Silk Pony (pay the night). Open a new adventure before the next delve. Party at full hp less minor wounds; check `inv show` for oil (military about 5, common 3).

## Engine 7.13.7 and the next session (2026-11-21)
- acks2-tools 7.13.7 (branch ccr-6e7c0096-7nmfvu, bc189fd): the S08 findings fixed; campaign `tools.ref` ccr-6e7c0096-7nmfvu, `min_version` 7.13.7; acks.sh exports ACKS_TABLES.
- The prompt to start the next session: `Playtest/NEXT-SESSION-PROMPT.md`.


## S09 (2026-11-21) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools unchanged at 7.13.7, bc189fd).

**State on resume:** day 219 ~12:30, fall, Cyfaraun (18.05), mode town, Silk Pony Inn (pay 2gp 6sp a night for 13;
`eat --in-town` before each rollover; after any delve day clear `sleep_due`/fatigue by hand after the inn night:
`wait` records no sleep). No adventure open (A17 paid out; open A18 before the next delve, join PCs `--kind pc` and
henchmen `--kind henchman --retinue-id ID`, then set each PC's `player` in adventure-state by hand).

**Party (13), strength 23:** Lucilla Ven4 19/19 (Rosa, caller), Vettius Thf4 12/12 (Tomasz), Iulia Cru2 13/13
(Gideon), Vestus M2 4/4 (Priya; Mage Missile, Protection from Evil, Fan of Flames), Neris Pr1 4/4 (Ingrid), Brennus F1
1/6 (Kwame; in shock: one night's bed rest due tonight; gruesome scarring, six teeth, an ear). Henchmen: Quirinus F2
9/10 (Lucilla's; ENERVATED by a wraith: max hp 18 -> 10, Death save each morning on waking, fail -1 max hp; three
passes in a row end it: not yet modelled, roll it each morning), Gnaeus Explorer 2 (Lucilla's), Varro F1, Aelia Bard 1
(Inspire Courage; Magical Engineering; Loremastery), Marcellus F1 (all Lucilla's), Phaedra M1 (Vettius'; Slumber),
Hrodvar Dwarven Vaultguard 1 (Iulia's; Engineering, Healing). Dead: Ottar (day 212, eaten by a grey goo), Septima (day
219, burned by her own fumbled flask; body carried to Cyfaraun, burial owed: body:septima). Nysa dismissed (day 211).
Magic weapons in use: Brennus Great Axe +1 (w53), Marcellus Sword +1 Death Drinker (w54), Quirinus Battle Axe +1 (w25),
Lucilla Mace +1 (w29), Vettius Sword +1 (w52). Kept: bag of faerie seeds (L87, Phaedra). Oil low (military sold out
for month 8 after day 219's buys; holy water none until day 241).

**User's instructions in S09 (all in Campaign/Rulings.md):**
- Strength floor per depth band: Upper 18, Lower 24, Deep 30, Abyssal 39, Sub-Abyssal 48 (levels of PCs and
  henchmen; 0th level counts 1 HD; a henchman advanced from 0th counts 1.5 at 1st, 2 at 2nd, then his level). A death
  that drops the party below the floor of the band it is in turns it back.
- Keep only the henchmen the floor needs: dismiss any the party can spare (every henchman is a half share).
- Delve as adventurers: multi-day expeditions to the deepest, richest areas the strength allows; sleep below in a
  sealed, spiked room; spike doors; set traps for known monsters (poured burning oil, caltrops, chokepoints).

**Next:** Brennus' night of bed rest (heal), Quirinus' enervation save each morning. The party needs one more level
(23 -> 24) to go back to the Lower band: hire one 1st-level henchman (Lucilla can hire up to 7; she has 5), or wait for
a level (Iulia 2,831/3,000; Vestus 2,688/5,000; Brennus 1,696/2,000). Then the rest of the temple of the dead (H17
vestry, H18, H19 -> G19), or C5's secret sepulchre (behind C3's centre grave, not found). Pending: unsettling event 7
(a dead baby rabbit floats in the sewage) at the next trip below. Bury Septima.

**Judge reminders from S09's slips (Playtest/judge-notes.txt S09):** only military oil is thrown as a weapon (common
oil is lamp oil); advance one turn at a time so torches are relit when they burn out (the light stays on a dead
carrier); set B/C/H location settings (temple/tomb level 4 for B and H; sewer level 2 for C); grave goods with
`recover --goods … --stone value/100`; after `sell`, the proceeds go nowhere: `inv receive` them and split with
`inv pay A … --to "B (share)"` + `inv receive B … --from A` pairs (there is no coin transfer between holders; `inv pay
--to B` alone loses the coins); `identify --by ID` needs ID in the open adventure; resolve fights in initiative order
(ties: the side with fewer combatants chooses); apply a save before its damage; equip magic weapons before a delve
(`use L#`, `inv give`, `inv wield`); the grey goo's slam destroys armour instead of damaging an armoured target; Neris'
Laying on Hands each day on rest days. Helpers: Playtest/tools/s09_j.sh (source it), choke.py, brawl.py.

## S10 (2026-11-21) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools unchanged at 7.13.7). Helpers: `Playtest/tools/s10_j.sh`
(source it; `LC=phaedra` is the light carrier; `cadd`/`crem`, `miasma`, `clearmiasma`, `t`) and
`Playtest/tools/melee2.py` (one combat round in initiative order: `python3 Playtest/tools/melee2.py a,b,c
"id:NAME:+N"`; it resolves only plain melee: do spells, visage saves, worms, oil and holy water by hand).

**State on resume:** day 243 06:02, fall, Cyfaraun (18.05), mode town, Silk Pony Inn. No adventure open (A22 paid
out). Session 10 ended; start S11.

**Party (12), strength 37** (Deep floor 30; Abyssal 39): Lucilla Ven5 21/21 (Rosa, caller), Vettius Thf5 18/21
(Tomasz), Iulia Cru4 16/23 (Gideon), Vestus M3 9/9 (Priya; Mage Missile, Protection from Evil, Fan of Flames;
Webbing, Burning Sparks), Neris Pr3 4/7 (Ingrid), Brennus F4 9/27 (Kwame). Henchmen: Phaedra M2 6/6 (Vettius';
Slumber, Fan of Flames; the light carrier), Varro F2 8/8, Hrodvar Vaultguard 2 2/5 (Iulia's; Healing), Aelia Bard 3
9/12, Marcellus F2 4/11 (Sword +1 Death Drinker), Gnaeus Explorer 2 2/9 (Battle Axe +1) (Varro, Aelia, Marcellus,
Gnaeus are Lucilla's). Iulia and Neris now have recorded prayerful repertoires (Iulia's had never been recorded
before S10). Retired/let go this session: Quirinus (recovered day 229 at max hp 4; Citadel Guard; epilogue in the
S10 log), Decimus, Calpurnia, Titus. Phaedra and Gnaeus were let go and taken back on day 233.

**Permanent wounds now:** Neris an ear bitten off (day 242); Marcellus two fingers off one hand (242); Brennus one
toe off one foot (242), plus an ear torn off, six teeth, gruesome scarring (S09); Lucilla an eye and an ear (S06-S07),
minor scarring. All in the actors' conditions.

**User's instructions for S11 (also in the next-session prompt):**
1. The party's next aim is to find someone to regenerate the ear, fingers and toes. Leads: *Repair Disfigurement and
   Disability* is a divine 4th-level spell (Crusader repertoire row 8; RR); in Cyfaraun, Prelate Romus (Crusader 7,
   one 4th-level spell a day) and Patriarch Arëtar (Crusader 10) of the Solar Citadel, and the temples
   (`spellcasting --type divine --level 4`, 185gp a casting by RR; availability by market class, Lucilla's network
   makes Cyfaraun class II). The engine's `restore ID ... --limbs N` applies the spell (R/xp-treasure.md §7). The
   vicar of Ammonar is Friendly (day 221); Arëtar wants evidence of the Awakening (the party has plenty: the font
   inscription, the mosaics of H18 and G20, the record scrolls of H17, the family tomb inscription E7).
2. Then the party brainstorms a way around the mummies' horrific visage (it has crippled every mummy fight: Paralysis
   save each round of looking, −1 per extra mummy, −1 per 3 worms; failure cowers; success immune 1 turn). Play the
   brainstorm by the profiles; rules to look up before ruling: RR Fear (Monster Ability) and Horrific Visage (MM
   Mummy), Remove Fear (divine 1st, Iulia and Neris have it), Holy Blessing and Inspire Courage (+1 vs magical fear;
   the "blessed/inspired" bonuses do not stack), the Fearlessness proficiency (if any), averting the eyes / fighting
   blind (no rule found yet: a Judge's ruling, record it), rebuking before the slab opens, missiles and fire from
   out of sight, potions or items against fear. Record what the party settles on in the party notes.

**Money and time:** coin in the Guildhouse (`guildhouse-bank`) and the Silk Pony strongbox (`silk-pony-strongbox`);
the four opals L156-L159 wait in the strongbox for month 10's first selling day (day 271; this month's check is 28%).
Elven relics go to Liber Faunus at 80% (Rulings S10, no tax check, no attention rolls). L126 (the encrypted
transmogrifier's spellbook, worth 31,750gp) is at the Tower of Knowledge: identification ready **day 247** (then sell
it through Liber or openly, or keep it). Wages: Phaedra due **day 250**, Varro and Hrodvar 257, Aelia and Marcellus
263, Gnaeus 270. **Silk Pony stalls (mule1, donkey1, donkey2, cart) paid only through day 242: owed from 243** (2sp a
stall a day; or sell the animals). Lucilla's investments: textile caravan (balanced, 700gp) rolls at each month's end
(next day 270); coast caravan (risky, 700gp) delayed, no return until month 13's end. Military oil and holy water: the
month-9 stock is mostly bought (holy water: none left until day 271).

**Henchman rule (user, S10):** the party keeps its henchmen and hires only when strength falls below the floor of
the band it is working (Rulings S10 supersedes the S09 "keep only what the floor needs").

**Nethercity state:** see World State. Emptied: B, D5, E3, E7-E9, G19-G21, H12, H17, H22 (urn charms and hook taken;
chest of natron, jars and the sarcophagi left), H25 (sarcophagus left; secret door to H26 found, not opened). Still
sealed in H: H6, H7-H8, H13, H16, H21 (the inquisitor, summons berserkers). G: faewyrd (purify at G4 or fight with
magic), G9, G10-G13, G14 (Abyssal), G16 statue. I: the troglodyte tribe (~100; alerted). J: the doom temple.

**Judge reminders from S10's slips (judge-notes S10):** mummy rot bars all magical healing (and Lay on Hands) until
Cure Disease; record it by hand on every slam and every grave-worm bite. Rest every 5 turns before the cliff/rope.
Never let a loop roll past an arriving encounter or a fallen character (check after every roll). Relight torches only
when they burn out. Spell scrolls: set `true.base_gp` by spell level before selling (the engine uses 1st level).
A mage's reading of a spellbook: `identify --method judge --reveal` does not mark it identified: fix `identified`
before `sell`. `inv give A B Ngp` moves coins between party holders. A cache cannot carry lots: drop them "at the
Silk Pony strongbox" and `recover --give` them back.

## S11 (2026-11-21) — in progress
**State:** day 244 06:02, Cyfaraun, town. Session 11 log: `Session Log/S11 — Healers and the stare.md`. Lucilla on
bed rest to day 257 (Keepers' courtyard, pay 1gp a night; inn beds for eleven). Neris' 1st-level repertoire now
recorded. Party notes hold the visage plan (S11); Rulings S11 hold the Repair/Tampering modifiers and the visage
rulings (who saves, averting the eyes, Blessed + Inspired stack, Remove Fear useless against cowering, Righteous Wrath
immune). Remaining wounds to mend (one `spellcasting --market-class II --type divine --level 4` a request, then
`restore ID --alignment A --caster-level 9 --temple --parts N --alive --wil-mod M`, then the condition and
`heal ID --bed-rest`): Brennus toe (parts 0), ear (1), teeth (0); Marcellus fingers (0); Neris ear (1).
**Update day 261 06:02:** all listed wounds mended (Lucilla third eye; Brennus a woman, -10% XP to F5; Marcellus STR 9;
Neris a vision). L126 sold through Liber (25,400gp) and paid out: eight level-ups; strength 45 (Abyssal band open).
Party notes S11 hold the downtime and the full visage plan. A23 is open (joined day 244; no delve yet). Next: choose
the target (Abyssal now allowed), prayers (Iulia: Striking, Holy Blessing, Righteous Wrath; Neris: Holy Blessing,
Augury), equip magic weapons, ration and light, down the far grate. Wages next: Aelia, Marcellus day 264; Gnaeus 271.
**Update day 262 06:02:** expedition 18 (A23) done and paid out (H16 cleared: hierophant + 2 cat mummies). Kept: L169
Crystal Ball (Lucilla; scry 3/day; Rulings S11: scrying a mummy = beholding it), L172 charts and L173 map (Vestus; for
a sage / Arëtar), L174 astrologer's spellbook (Vestus; copy Thunderbolt and Dispel Magic, 6 days, then sell to Liber:
base 25,900, sale XP to A23). Remaining H tombs: H13 (courtier, illusions; slab off H9, west balcony), H6 (princess,
snakes), H7-H8 (8 skeletons + warlord), H21 (inquisitor, berserkers). Divine Blessing +2 is not in the engine's
saves: pass `--mod "Divine Blessing:+2"` (Neris, Iulia). Wages: Aelia, Marcellus day 264.
**Update day 264 06:25:** expeditions 18-19 done (H16, H13 cleared); crystal ball, faerie flute, both spellbooks'
proceeds banked (Liber); H13 ancient coin in the strongbox. Kept: L172 charts, L173 map (Vestus), L174 astrologer's
spellbook (Vestus copying, 1 of 6 days done). Strength 47 (Sub-Abyssal 48 one short). Next targets: H6/H7-H8
(facing slabs in H3b), H21 (by H11). Vettius still overloaded (13 st): share out his gear before the next descent.
Left in H13: 2,000sp, antlers (3 st). Gnaeus wage day 271 (selling day too); month 9 ends day 270.
**Update day 265 05:25:** the ancient coin (16,441gp 258sp 235cp) and opals L156-L159 are in the party's locked chest in
the Grey Sisters' vault (holder `grey-sisters-vault`; Doarë Friendly; 10gp a month paid to day 293; Rulings S11). The
Silk Pony strongbox holds only spare gear. Stalls paid to day 270. Vettius 9.6 st (60'). Vestus copying day 2 done.
**Update day 267 06:18:** expedition 20 done (H6 looted; the princess fled as a swan at 8/27 hp: when the party next
meets her, roll the SOTN mummy reaction table). Vettius (max 19) and Aelia (max 11) cured of enervation. Brennus F5.
Strength 48 (Sub-Abyssal floor reached: Lucilla 5, Vettius 6, Iulia 5, Vestus 4, Neris 4, Brennus 5, henchmen 3+3+3+4+3+3).
Vestus has copied 3 of 6 days. Vault: 17,341gp 258sp 235cp + opals. Next: H7-H8 (8 skeletons + warlord AC 11), H21.
**Update day 268 05:24:** expedition 21 done (H7 skeletons, H8 warlord destroyed; H7-H8 looted). The princess is in her
coffin in H6 (slab open, lid not moved: try with Ogre Strength; her reaction on waking: SOTN mummy reaction table).
H21 untouched. Phaedra's filter masks: use `miasma6` (s11_mend.sh, +6). Neris Pr5 (Cure Disease in her repertoire).
Strength 51. Vestus copying 3 of 6 days done. Vault holds the ancient coin. Day 270: month 9 ends; day 271: selling
day (opals), Gnaeus' wage.

## S11 (2026-11-21) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools unchanged at 7.13.7). Helpers: source
`Playtest/tools/s10_j.sh` (set `PARTY="lucilla vettius vestus-the-unlikely neris brennus iulia phaedra varro hrodvar
aelia marcellus gnaeus"`: its default still lists Quirinus; `LC=phaedra`; `cadd`/`crem`, `miasma`, `clearmiasma`, `t N`)
and `Playtest/tools/s11_mend.sh` (`miasma6`: the +6 save with Phaedra's filter masks; `mendask`; `night`).
`Playtest/tools/melee2.py` runs a plain melee round. Session 11 log: `Session Log/S11 — Healers and the stare.md`.

**State on resume:** day 268 05:24, fall, Cyfaraun (18.05), town, Silk Pony Inn. No adventure open (A26 paid out).
Run `acks.sh rest` once before each descent (the rest count carries over town days: S11 slip). Session 11 ended;
start S12.

**Party (12), strength 51** (Sub-Abyssal floor 48 reached): Lucilla Ven6 22/22 (Rosa, caller; third eye under a
band), Vettius Thf6 19/19 (Tomasz; max hp lowered by a shadow), Iulia Cru5 26/26 (Gideon), Vestus M4 10/10 (Priya),
Neris Pr5 14/14 (Ingrid; Cure Disease now in her repertoire), Brennus F5 28/28 (Kwame; a woman since day 247; keeps the
scarred face). Henchmen: Phaedra M3 11/11 (Vettius'), Varro F4 22/22, Hrodvar Vaultguard 3 11/11 (Iulia's), Aelia Bard
4 11/11 (max lowered), Marcellus F3 19/19 (STR 9), Gnaeus Explorer 3 10/10 (Varro, Aelia, Marcellus, Gnaeus are
Lucilla's). No wounds, rot or enervation. Repertoires recorded: Neris 1st-3rd, Iulia 1st-3rd, Vestus (Ogre Strength
added), Phaedra (Illusory Duplicates added).

**What S11 did:** every listed wound mended by Repair Disfigurement and Disability (Tampering marks: Lucilla's third
eye, Brennus a woman, Marcellus +2 STR, Neris' vision of the Great Teacher); the visage plan (party notes S11) and its
rulings; downtime that sold L126 and raised eight levels; expeditions 18-21 cleared H16 (astrologer), H13 (bard), H6
(looted; the princess fled as a swan) and H7-H8 (skeletons, warlord); the ancient coin moved to a locked chest in the
Grey Sisters' vault (Doarë Friendly); the miasma answer (Phaedra's masks, +6; rest in B1 both ways). Rulings S11: 20 rows.

**Money:** Guildhouse (`guildhouse-bank`) 98,514gp clean coin; the Grey Sisters' vault (`grey-sisters-vault`, 10gp a
month paid to day 293; withdraw when Doarë is in, 60% by day) 18,439gp 258sp 235cp of ancient coin and the opals
L156-L159; the Silk Pony strongbox holds only spare gear (2 lanterns, grappling hook, backpack, waterskins, short
sword). Kept items: L172 star charts, L173 elven map (Vestus; Neris' Knowledge (astrology) 11+ reads the charts:
first try failed), L174 astrologer's spellbook (Vestus copies Thunderbolt and Dispel Magic: 3 of 6 days done; then
sell through Liber at 80%: sale XP to A23). L5/L127/L128 potions of healing with Neris. Elven relics go to Liber at
80%; magic items found are sold unused unless their use is worth more than the XP (Rulings S11).

**Dates:** day 270 month 9 ends (investment 1 vagary; month 10 starts day 271: Lucilla's Rumormongering again,
selling day for the opals, a new month of magic-item stock to roll if the party shops); day 271 Gnaeus' wage; 280
Phaedra; 287 Varro, Hrodvar; 293 vault fee; 294 Aelia, Marcellus. Stalls (mule1, donkey1, donkey2, cart) paid
through day 270.

**Nethercity:** H cleared except H21 (inquisitor of Bel, summons berserkers) and the princess in H6 (8/27 hp, in her
coffin, slab open, stone lid unmoved: forcing -4, up to 3 helpers; Ogre Strength +8; on waking roll the SOTN mummy
reaction table; hard-pressed she flies as a swan). H25's north-fresco secret door to the H26 stair (P5, Sub-Abyssal)
is found, not opened. Left behind: H13 2,000sp and antlers; H7 2 ropes, amphora; H8 cedar chest. Deeper: see the
World State prep queue.

**Routine reminders (S11 slips):** two failed heaves (or lid tries) = stop and wait a turn in silence; rest every 5
turns (a turn's rest also clears the miasma); rearguard watches the side passages while the haulers pull; Divine
Blessing +2 is in the engine's saves from 7.14.0 (before it: `--mod "Divine Blessing:+2"`); keep Vettius under
10 st; never let a loop run past an encounter or a fallen character; resolve every round in initiative order.

## S12 (2026-11-22) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0 since the S12 engine pass: setup must print
`engine: ready: acks 7.14.0`). Helpers: source `Playtest/tools/s10_j.sh`
(then `PARTY="lucilla vettius vestus-the-unlikely neris brennus iulia phaedra varro hrodvar aelia marcellus"`: Gnaeus
is abed and out of the exploration party (`party remove gnaeus` on day 272; `party add gnaeus` when he is up),
`Playtest/tools/s11_mend.sh` (`miasma6`, `mendask`) and `Playtest/tools/s12_town.sh` (`innnight DAY N COST H1 H2`;
its `slept` and `dawn DAY` are not needed on 7.14.0: a `wait` over an inn night records the sleep and the spells). Session 12 log:
`Session Log/S12 — The princess and the inquisitor.md`.

**State on resume:** day 273 06:53, fall, Cyfaraun (18.05), town, Silk Pony Inn. No adventure open (A28 paid out).
Start S13.

**Party (12), strength 48 delving** (Gnaeus abed; 52 with him): Lucilla Ven6 22/22, Vettius Thf6 19/19, Iulia Cru5
26/26 (bears the Rod of the Dawn, L203: once a day, a turn of rebuking and casting as 4 levels higher: `rebuke iulia
--level-mod 4`), Vestus M5 15/15 (Swimming; Thunderbolt and Dispel Magic copied, a week's study each before use),
Neris Pr5 14/14, Brennus F5 28/28. Henchmen: Phaedra M3 11/11, Varro F4 22/22, Hrodvar VG4 15/15, Aelia B4 11/11,
Marcellus F4 20/20, Gnaeus Exp4 1/19 (bed rest to about day 298; speaks with dead once a week). No rot, no wounds.
Holy water: Marcellus 6. Military oil: Aelia 3, Phaedra 5, Vettius 1 (buy more before the next descent). Phaedra has
no torches left (buy).

**What S12 did:** H6 princess destroyed in her coffin (swan cloak L202, very rare, unidentified); H21 inquisitor,
his berserkers destroyed (Gnaeus mortally wounded, saved, throat mended by Arëtar); Arëtar FRIENDLY (the Rod lent; the
regalia bought back); the month-10 selling day; expedition 23 by H25-H26 to the river beach P5 and the P6 burial cave
(the 8th-level Telith mummy rebuked with the Rod and destroyed). Rulings S12: 7 rows.

**Money:** Guildhouse 104,299gp clean coin; Grey Sisters' vault 23,119gp 258sp 235cp ancient coin (10gp a month paid
to day 293). Kept items: L172 star charts (read: the Conjunction in about three years), L173 elven map, L174 the
astrologer's spellbook (copying done: sell through Liber at 80%, sale XP to A23), L202 swan cloak (identify, then
Liber at 80%), L5/L127/L128 potions of healing with Neris.

**Next (by the profiles):** the river beyond P5 needs a boat or raft (no banks): Hrodvar's Engineering (a raft) and
rope, or swimming; the catfish attacks on 6 each turn on the water. Or the four amphorae left in P6 (12 st), H14's
energy crystals (480 skeletons), C5. Gnaeus is up about day 298.

**Routine reminders (S12 slips):** break the turn loop on "rest due" (not only "rest due now"); relight the lantern
after `light refuel` (`light on lantern5`); `--target-wil` is the WIL modifier (`--target-wil-score 16` for a score); Righteous Wrath just before the opening
heave; armor does not count against a gelatinous cube's engulf.

**Engine 7.14.0 (the S12 engine pass; HISTORY "fifth pass"):** `turn`/`rest`/`wait` write the rollover's hp,
deaths and spells to the actors (no hand healing); a `wait` over 8 night hours in town records restful sleep and
spells regained; `save` adds Divine Blessing +2 itself (no `--mod` for Iulia and Neris); `state set hp=N` (N >= 1)
ends a dying timer; `sell` of a lot whose adventure is paid out pays its share-holders (no `inv receive`/`inv pay`
pairs); `restore --apply` writes Tampering with Mortality's result; `inv holder kind`, `retinue employer` for a
successor (Vestus); `explore` refuses while an arrived encounter is unresolved; `explore force-door A B --helpers C`;
`attack --damage-mod`, typed `--extra-dice` (protected separately); a mummy's slam puts mummy rot on the combatant;
`state cond ID enraged` is berserk; actor `defenses` (Lucilla's ring) reach the combatant at `state add`;
`encounter surprise --apply-note-penalty` (a note's penalty on the dice already rolled); `recover --store`;
`item --market-stock`; market class 1-6, `--market-class` wins over the note.

## S13 (2026-11-22) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers: source `Playtest/tools/s10_j.sh`,
`Playtest/tools/s11_mend.sh` and `Playtest/tools/s13_j.sh` (`go N`, `walk N`: a turn loop that rests whenever a
line says "rest due" and stops on encounters, lights out and the like); `Playtest/tools/s13_pudding.py` (a fire-only
foe fought by thrown oil and torches while the line gives ground: RR p. 298 hit/splash/scatter/second burn; env
HOLD, PREF, FANS, SPARKS, CURE, DECL, BLESSED). Session 13 log: `Session Log/S13 — Another way around.md`.

**State on resume:** day 290 07:14, winter, Cyfaraun (18.05), town, Silk Pony Inn. No adventure open (A31 paid
out). Session 13 ended; start S14.

**Party (12), strength 49 delving** (Gnaeus abed to about day 298): Lucilla Ven6 22/22, Vettius Thf6 19/19, Iulia
Cru6 13/31 (Rod of the Dawn), Vestus M5 15/15 (Thunderbolt learned; Dispel Magic copied, not studied), Neris Pr5
14/14, Brennus F5 22/22 (max lowered by a wraith, day 274). Henchmen: Phaedra M4 17/17 (Levitation learned), Varro
F4, Hrodvar VG4, Aelia B4, Marcellus F4, Gnaeus Exp4 abed. Oil: Phaedra 1 (buy a full load before the next descent);
torches low; Vettius has no lamp oil. Holy water: Marcellus 5.

**What S13 did:** L174 sold through Liber (20,720gp, sale XP); expedition 24 (the sloping gallery H23-H24: the well
over P7; the P6 amphorae; two wraiths, one destroyed); four canoes bought (Rulings S13: knocked down for the carry,
no proficiency to paddle); expedition 25 by canoe (a flailing spirit and a mummy destroyed in H25; the catfish driven
off at 12/37; P8b seen); L202 named by the Tower (Cloak of Skinchanging) and sold through Liber (30,400gp, sale XP);
expedition 26 (the black pudding of P8b burned to death; the egg of the earth L223 taken, 25,000gp, unnamed and
unsold: it waits in the vault for the month-11 selling day, day 301; gems are the party's own business: open sale,
tax check). Levels: Phaedra Mag4, Iulia Cru6. Rulings S13: 2 rows (canoes, catfish while hurt).

**Engine findings S13 (judge-notes S13):** `location --site` resets the wandering counter (change only --level/--table
inside a delve); `treasure_stone` from `recover` is not reduced when a lot is sold (reset by hand day 287); a
monster with more attacks than damage entries (the catfish: 5 attacks, 2 damage rows) refuses a hit with index 2-4;
vessels are not catalog items; spells learned are `actor item ID add spell NAME --level N`; a second rebuke spends
its HD on a monster already rebuked.

**Next (by the profiles):** buy oil, torches and lamp oil; sell the diamond on day 301 (or carry it to a dwarf of
Azen Khador descent for more, if the party learns its story); upriver P9-P11 by canoe with the catfish hurt; Gnaeus
back about day 298; Vestus' week of study for Dispel Magic on town days.

## S14 (2026-11-22) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers as S13 (`s13_j.sh`: `walk`, `go`;
`s13_pudding.py`; `fight.py` now resolves fighters' cleaves). Session 14 log: `Session Log/S14 — The white fish.md`.

**State on resume:** day 303 05:48, winter, Cyfaraun, town, Silk Pony Inn. No adventure open (A34 paid out). Start S15.
**Cyfaraun is Class II for every party purchase (Lucilla's Mercantile Network): always `--market-class 2`.**

**Party (12), strength 53:** Lucilla Ven6, Vettius Thf6, Iulia Cru6 (Captain of the Underwatch: spear +2 L233 and
shield +1 L232, the Citadel's, never sold; the Rod of the Dawn L203), Vestus M5 (Thunderbolt, Dispel Magic), Neris Pr5,
Brennus F5 (wears Rhankur's black plate +1, L231). Henchmen Phaedra M4 (Levitation), Varro F4, Hrodvar VG4, Aelia B5
(Naturalism), Marcellus F4, Gnaeus Exp4 (up day 299). Old gear in the Silk Pony strongbox (Iulia's mace and shield,
Brennus' chain and spare axe, the hook and chain is with Gnaeus).

**What S14 did:** downtime (Lucilla's investment 3; Arëtar, Doarë, Liber); the Death Cult Hideout (#75u) cleared
(A32: Malthusia captured to the Citadel; Velus' estate to Vettius; Iulia's office); Celictor's lizardmen captured
alive (A33, 800gp); Gnaeus up; selling day 301 through Liber (diamond 20,000, Shield +1 4,000); Aelia Bard 5; the
giant catfish bewitched by Neris at the P5 beach (A34). Rulings S14: 4 rows (Underwatch regalia, black plate apparent
value, hook and haul, office regalia no XP).

**Engine findings S14:** `party remove` stops a member's bed rest counting (fixed by hand twice); proficiency throws
without recorded targets need `--target` (Healing, Deciphering); `recover --item` needs the "Armor +1 (Plate Armor)"
form; lot claims are `inv claim LOT HOLDER`; selling an unidentified magic item prices it as mundane (identify first).

**Next (by the profiles):** the river by canoe with the fish friendly: upstream P9 (G14 well), P10 (graves, the
inscription), P11 (barge; the elemental on trespass; P14 anointing); downstream P4 (Q6), P3 (Q1). Day 309: the fish's
weekly save. Month 11 ends day 330 (investments 1 and 3). Threads: Celictor's crocodile (#45u, HD 15); the Ionicus
estate (beastmen, near #30); the arena (Celictor recruits champions against Maximus); rumours 14 (Vasan Tikala, the
Doppelgänger Den #14u) and 8.

## S15 plan (user, 2026-11-22) — read with the S14 section above
1. **The charmed catfish:** bewitched by Neris on day 302; its weekly Spells save to break the charm falls on day 309
   (hidden; Rulings S14). Make the most of days 303-309 on the river by canoe while it is friendly: upstream P9 (G14
   well), P10 (24 graves, the Lammala inscription: Vestus reads Ancient Argollëan), P11 (the barge cave: the water
   elemental attacks anyone who sails the barge or enters the P12 tunnel unanointed, and anyone coming back from P12
   with its treasures; P13-P14 anointing font; P12's treasures carry Lammala's curse); downstream P4 (to Q6) and P3
   (to Q1). Feed the fish (a sheep) on each visit; Neris can renew Bewitch Beast if it breaks (+5 to its save if
   threatened). Speak with Beasts gets concrete facts only. Carry the canoes knocked down (Rulings S13).
2. **Iulia's Underwatch mission:** find the Horned Rat cult's shrine (#13u, `Adventure/AX3/Dungeons/Shrine of the
   Horned Rat.md`; Provost Mentenus of the Tower; the wererat wall-tappers met in the sewers, Indifferent day 288) and
   report it to Arëtar **before day 330**, with her monthly report. A sanctioned mission brings 1d4 Knights of the
   Winged Sun (Rulings S14). Fit it around the river days (the catfish window first, then the shrine, or the shrine
   on days the river is not worked).
3. **Saved for later (do not start in S15 unless the table chooses it):** the Ionicus estate at 27.19 beyond the
   Türos Aster ford (bugbears of the Ruined Imperial Fortress 26.19; barony offer; about a week's march; not built);
   Celictor's crocodile (#45u, HD 15, 2,000gp alive); the arena; rumours 14 (Vasan Tikala / Doppelgänger Den #14u) and 8.
4. **Month 11 ends day 330:** investments 1 and 3 vagaries (World State), Iulia's month-end Underwatch rolls (mission
   1d6, Mentenus 1-in-6), wages (Phaedra due day 310: paid to 309), stalls to 316, vault fee to 323.
5. Routine: Cyfaraun is Class II (`--market-class 2`); military oil 70 a month for the party; `walk` rests on "rest
   due"; never `location --site` mid-delve; identify before selling; keep everyone under 10 st (Brennus' plate is 6 st).


## S15 (2026-11-22) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers as S13/S14 (`s10_j.sh`, `s11_mend.sh`,
`s13_j.sh`: `walk`, `go`, `miasma`, `clearmiasma`). **Set `PARTY` after sourcing s10_j.sh** (its default still lists
Quirinus, retired). Session 15 log: `Session Log/S15 — Upriver.md`.

**State on resume:** day 309 05:11, winter, Cyfaraun (18.05), town, Silk Pony Inn. No adventure open (A39 paid out).
Start S16. Cyfaraun is Class II for every party purchase (`--market-class 2`).

**Party (12), strength about 55:** Lucilla Ven6, Vettius Thf7 (22/22), Iulia Cru6 (Captain of the Underwatch; spear
+2, shield +1, Rod of the Dawn), Vestus M5, Neris Pr5, Brennus F6 (23 max; Weapon Focus axes; black plate +1).
Henchmen Phaedra M4, Varro F4 (Lann Dhuille, Sword +1, identified, used), Hrodvar VG4 (max hp 13 after a shadow;
enervation ended day 306), Aelia B5, Marcellus F4, Gnaeus Exp4. Brennus 22/23, Iulia 31/31: all whole or nearly.

**What S15 did:** five descents and two town days. Upriver (A35): P9-P14 seen, P10 graves, four shadows and three
wights destroyed. The P12 basin (A36): 20,900gp carried out past the P11 water elemental inside Neris' Holy Circle,
Sustained (both carriers saved against Lammala's curse); a mummy at P5. Downriver recon (A37): Q6 panel found, P3
slab untouched. The Horned Rat shrine (A38): found by Liber's word, Abimbola's pack killed asleep, a seer captured,
the altar broken, Mentenus's papers to Arëtar: **Iulia's mission done (day 306)**, month-11 report made. The black
barge (A39): rowed out of P11 by its oar pattern to Lake Laman, moored at Tertulla's landing. **The white fish's save
on day 309 succeeded (hidden): the charm is broken; it is Neutral (wild); the party does not know.** Rulings S15: 7 rows.

**Money and goods:** banked after day 306; for the month-12 selling day (day 331): L238 grave goods (strongbox),
L239-L245 the mask and the basin treasure (Grey Sisters' vault), L254 spices and L255 furs (carried by Vestus and
Neris), L258 the barge (identified, used: no sale XP; 68,000gp base; Liber at 80% or keep).

**Next (by the profiles):** the selling day; Terkinos's pack (8) and Mentenus at the full moon (date to set); what
Arëtar does with the papers; G14 (mummy warlord, four bronze statues; constructs and undead are barred by Iulia's
shield: Rulings S14); the Night Captain's tomb under the Citadel; Celictor's crocodile; the Ionicus estate; the arena.

**Engine findings S15 (judge-notes S15):** `adventure join` needs `--kind henchman` for henchmen; no JUDGE line for
the shadow's "-3 to surprise"; `damage --extraordinary` treated as mundane against shadows (fine against a mummy);
the rest counter survives a night in town; Rat Swarm needs `--set hd` and `--xp-each`; `recover --item "Sword +1"`
can draw a dagger (use "Sword +1 (Sword)"); snapshot refuses an unidentified generic "Sword +1" when identified
ones are on other sheets; `level-up` ignores permanent enervation losses.

## S16 (2026-11-22) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` (tools 7.14.0). Helpers as S15 (set `PARTY` after sourcing `s10_j.sh`). Session 16
log: `Session Log/S16 — The bronze guards.md`. `Playtest/tools/s15_ledger.py PAYOUT.txt` copies a saved
`payout --ledger --apply` output's rows into Campaign/Ledger.md.

**State on resume:** day 316 04:32, winter, Cyfaraun, Silk Pony. No adventure open (A43 paid out). Start S17.
**Party (12):** all whole or nearly; Neris Pr6 (15 hp); Marcellus max hp 16 (shadow, day 309); Hrodvar wields
the rune-hafted Battle Axe +1 (L292), Varro Lann Dhuille. The four canoes are hidden at P5 (assembled).
**The white fish:** charmed (day 309); day-316 save failed (hidden); next save day 323.

**What S16 did (days 309-316):** G14 cleared of its king and treasure (A40, A41); the doppelgangers of rumour 14 and
their den (A42; prisoners freed, rewards A43; the Brotherhood's ledger: Liber, Mentenus, Selene as patrons, kept
secret but for Arëtar's copy of the Mentenus entries). Arëtar plans the full-moon ambush on Mentenus (day 328).

**Next (by the profiles):** Q (Marcan) with Ingrid's conditions; the full moon (day 328: the Shrine is empty: Terkinos's pack abandoned it the night of day 306 and warned Mentenus, user's ruling); the selling day (331).
Rulings S16: 4 rows. Engine findings: judge-notes S16.

**S16 after-play rulings (user):** Terkinos's pack abandoned the Shrine (night of day 306); Guildhouse storage fee
0.25% a month posted for months 8-10 (next day 330); henchmen's wages raised to the RR table with 2,100gp back pay
(raise the wage at every henchman level-up: `retinue set ID wage_gp=N`); over-limit henchmen stay until SOTN is
done. All in Rulings S16.

## S17 plan (user, 2026-11-22) — read with the S16 section and the S16 after-play rulings above
**State on resume:** day 316 04:32, winter, Cyfaraun (18.05), town. No adventure open (A43 paid out). Start S17 (new
log in `Session Log/`). Play one week: days 316-323. Party decisions by `Party/profiles` and `Party/heuristics.md`, no
party-agent calls; small checkpoint updates to the user at each milestone (descent, key fight, return, town day).

**1. Lodging: leave the Silk Pony.** Iulia, as Captain of the Underwatch, may lodge and feed herself and up to eleven
companions at the Solar Citadel (Citadel Guard barracks) free on any night in Cyfaraun (Rulings S14). Move the company
there on day 316: no more inn payments (the `innnight` helper and the 2gp4sp a night stop; keep `eat --in-town` and
`wait` over the night). Also: Selene, who owns the Silk Pony, is a Brotherhood patron in the ledger ("ruby lips").
Loose ends: the Silk Pony strongbox (spare gear: chain mail, great axe, mace, shield, lanterns, grappling hook...;
move it to the Citadel or the Grey Sisters' vault, `inv give silk-pony-strongbox <holder> ...`); the mule, two donkeys
and the cart in the Silk Pony stalls (paid to day 332; move them or leave them to then: Judge's call whether the
Citadel stables take them); L238 (grave goods) stored in the strongbox (`recover --give L238 --store
grey-sisters-vault`). Neris and the enervated still sleep under the oculus (free for the Captain's companions).

**2. Use what they learned from the doppelgangers.** The party holds the Assassins' Ledger (sealed in the Grey
Sisters' vault; Arëtar has the Mentenus entries only). It names patrons and passwords: Liber Faunus ("morning dew":
Huranos, Ashera, Vason, Bodilkas), Provost Mentenus ("sludge mold": Gundus, Fionntan, Tomman), Selene of the Silk Pony
("ruby lips": Olyma, Riara). Nobody outside the company knows the Brotherhood is dead. The table decides; options the
module gives or allows (AX3 Old District "Value of information" and Hooks; `Adventure/AX3/City/Organizations of
Cyfaraun.md`):
- Rewards for evidence of the victims' fates: City Watch HQ (Gundus 40gp), Merchant Guildhouse (Huranos, Ashera,
  Vason 120gp), Temple of the Hearth Fire (Riara 40gp), Hall of Travelers (Bodilkas 40gp). The noble survivors went
  home on day 313 (rewards paid by the houses).
- The ledger to Prelate Ezelus of the Temple of Justice (#61): with Iulia and Neris vouching, he puts them in touch
  with the Order of the Eclipse (Destrio, Eclipse Hideout #69u; Calefa's sanctioned deathbringers, who hunt the
  Brotherhood); otherwise 1,500gp and an oath of secrecy.
- Leverage: Liber and Selene ordered murders; each would pay or kill to keep it hidden (Liber is the company's fence;
  Iulia's office: Liber stays Friendly while she does not act against the Family's smuggling, Rulings S14; murder is
  not smuggling). Posing as the Brotherhood (the passwords; the den; doppelgangers' disguise kit in room 2) to learn
  new contracts or draw a patron out. Mentenus's entries strengthen Arëtar's case against the Provost.
- **Check first:** Rulings S14 ("standing with factions") lists the Order of the Eclipse among the Chaotic cults
  hostile to the Captain; AX3 makes it Calefa's sect of sanctioned killers (Empyrean, hunts the Brotherhood). Correct
  that row (a ruling for the user if it matters) before the ledger reaches Ezelus.
- Den leftovers: room 5 (the founders' bodies under a beetle swarm, behind a secret door off the NW sewer tunnel),
  the SW oil trap (armed), the disguise clothing in room 2.

**3. Other threads (table's choice; the week is open):** Marcan's tomb (Q) under Ingrid's conditions; F -> T (the
Great Teacher, the module's centre; F14's hidden stair); Terkinos's pack and Mentenus (gone from the Shrine; the
full moon day 328); the black barge at Tertulla's landing (mooring paid to day 321: pay on or before 321, or move or
sell it); the selling day (day 331, outside this week).

**4. The white fish:** charmed; its weekly save falls on **day 323** (hidden; F4 15+). The canoes are hidden at P5.
On any beach visit bring a sheep and Neris' Bewitch Beast (the party knows it may break).

**5. Scheduled this week:** day 321 Tertulla's mooring; day 323 the fish's save, Aelia (400gp) and Marcellus
(200gp) wages, the Grey Sisters' vault fee (10gp a month). Wages are now the RR table (Rulings S16): raise a
henchman's wage at once on a level-up (`retinue set ID wage_gp=N`).

**Routine (S15-S16 slips):** set `PARTY` after sourcing `s10_j.sh`; a rest counter carries over nights in town
(rest at the first turn below if it says rest due); identify a generic magic weapon before saving if an identified one
of the same name is on a sheet (snapshot collision); unsettling checks every 2 hours below; `adventure join` with
`--kind henchman` for henchmen; never `location --site` mid-delve; `Playtest/tools/s15_ledger.py` for payout rows.

## S17 (2026-11-22) — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers: `s10_j.sh`, `s11_mend.sh`, `s13_j.sh`,
`s12_town.sh` (set `PARTY` after sourcing; Gnaeus is gone). Session 17 log: `Session Log/S17 — The ledger.md`.

**State on resume:** day 323 16:57, winter, Cyfaraun (18.05), the Solar Citadel barracks (free: Captain's privilege).
No adventure open (A47 paid out). Location: Cyfaraun (settlement, no wandering). Start S18 with the night of day 323
(`eat --in-town`, `wait`; `dawn 324` for spells).

**Party (11):** Lucilla Ven7, Vettius Thf7, Iulia Cru6 (Captain; spear, shield, the Rod), Vestus M6 (Magical
Engineering), Neris Pr6, Brennus F6; henchmen Phaedra M5, Varro F5, Hrodvar VG5, Marcellus F5, Aelia B5 (all at
400gp a month). All whole. Gnaeus resigned day 317 (Characters/former). The six PCs are acolytes of the Order of the
Eclipse (initiation: Provost Mentenus); the ledger is the Order's.

**What S17 did (days 316-323):** left the Silk Pony (strongbox and L238 to the Grey Sisters' vault; beasts to the
Citadel stables); Rulings S14 Order of the Eclipse corrected; Marcan's tomb Q cleared and emptied in four descents
(A44-A47: Marcan and his four guards destroyed inside the ward; 56,917gp of goods plus the three magic items, all
in the vault for day 331); Ezelus (day 319) and Destrio (vetting 16: acolytes); the victims' rewards left unclaimed
(the Order's secrecy); Tertulla paid to 335. **The white fish's charm broke on day 323 (hidden), Friendly (12).**

**Next (by the profiles):** the full moon (328: Arëtar's ambush finds the Shrine empty); month 11's end (330:
storage fee, investments, Iulia's rolls); the selling day (331: the tomb's goods; L296, L297 identified and unused,
L295 unidentified); the Mentenus contract; F -> T. Rulings S17: 3 rows. Engine findings and slips: judge-notes S17.

**Routine (S17 slips):** after every return `location --clear` and set the settlement before any `wait`;
`encounter surprise` always with `--party`/`--monsters` (fore,los / los / none); the Rod's +4 lasts one turn
(10 rounds); pass `--target` to `rebuke` for undead not yet rebuked; rest at "rest due in N rounds"; relight a
burnt-out lantern with `light on lanternN` after a refuel.

**S17 addendum (user, day 323):** (1) A tracker for the wererat search: Saturnin (0th-level cantinakeeper with
Tracking 1, Lucilla's henchman, 12gp a month paid to 352, leather, shield, spear) hired day 323, the best the month
offered; search again for an Explorer (levels 4 down, `recruit --class Explorer --level N`) from day 331, when month 12
opens. The tracking job: the pack's trail from the Shrine's NW room-2 secret door into the unkeyed tunnels north (fled
the night of day 306: an old trail), then Mentenus. (2) **Vettius plays the thief:** hide, work to the rear, backstab
every vulnerable target with `attack vettius T --ambush` (add `--rear` when he attacks from behind); cowering,
surprised, helpless, prone, slumbering and paralyzed foes are vulnerable to all. Player-facing note in
`Party/memory/tomasz.md`.

## S17 week 2 (days 324-330) — start here (supersedes the S17 section above)
**State on resume:** day 330 15:53, winter, Cyfaraun, the Solar Citadel. No adventure open (A48 paid out). Location
Cyfaraun (settlement). Party (12): as S17 plus Saturnin (0th, Tracking 1). All whole. Spells: `dawn 331`.
**What it did:** day 324 the Rat Warren (built judge-interim: Adventure/AX3/Dungeons/Rat Warren/): Terkinos's pack
destroyed asleep, ghouls destroyed, the Watch subaltern Caeso Lentulus saved (Friendly); Mentenus's letter to
Arëtar, who wants proof from the Provost's study (Basement 2). Day 325 Vestus applied to the Tower (interview day
339); Destrio's answer (a court's verdict settles the initiation; another would be given). Full moon quiet. Day 330
month end posted (fees, investments: Protector, Iulia's rolls).
**Judge-only, live:** Mentenus knows the Captain's office is filled and the Citadel holds his papers; on day 330 he
left a note for "Vasan Tikala" (sludge mold): meeting at the Nicean outlet, midnight day 333, target Iulia. The
company can learn of it at the Emporium wine stalls (Lucilla asked there in S16) or by Rumormongering (day 331).
**Next:** the selling day (331), the explorer search (331), the Vasan note, Basement 2, Vestus' interview (339).

## S18 plan — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers: source `Playtest/tools/s10_j.sh`,
`s11_mend.sh`, `s13_j.sh`, `s12_town.sh`, then set `PARTY="lucilla vettius vestus-the-unlikely neris brennus iulia
phaedra varro hrodvar aelia marcellus saturnin"` (Gnaeus is gone). Session 17 log: `Session Log/S17 — The ledger.md`
(days 316-330).

**State on resume:** day 330 ~17:00, winter, Cyfaraun (18.05), the Solar Citadel barracks (free). No adventure open
(A48 paid out). Location Cyfaraun (settlement, wandering none). Night of day 330 first (`eat --in-town`, `wait`),
then `dawn 331`. Twelve: Lucilla Ven7, Vettius Thf7 (now wields Marcan's Short Sword +2, Command, L297, used),
Iulia Cru6 (Captain; spear, shield, the Rod), Vestus M6, Neris Pr6, Brennus F6; henchmen Phaedra M5, Varro F5,
Hrodvar VG5, Marcellus F5, Aelia B5 (400gp a month each), Saturnin 0th (Tracking 1, 12gp). All whole. The six PCs
are acolytes of the Order of the Eclipse.

**Days 331 on (the table's open business, by the profiles):**
1. **Selling day (331, month 12):** the vault's goods (Marcan's tomb: crown, collar, fan, sandals, gold sarcophagus,
   throne, chariot, shields, canopic shrine, jars, the guards' four bronze sarcophagi; earlier: the basin treasure,
   the mask, the grave goods, G14's crown, box, gems, jars, throne, chariot and coffin; the den's gems, jewellery and
   cask; the silver rat figurine L319), L296 Helm of Comprehension (identified, unused: sale XP), L295 Marcan's scale
   (unidentified: identify first, Arëtar or the Tower). Elven relics through Liber at 80% (`sell --discount 20`);
   Cyfaraun is Class II for party purchases (`--market-class 2`); hiring uses the market note's Class III.
2. **A woodsman:** month 12 reopens the hiring searches: `recruit --class Explorer --level 4` (down to 1) for
   Lucilla or Vettius (both may hire 4th level); use `hire --publish-to Characters/<id>.json`.
3. **The "Vasan Tikala" note (Judge-only):** Mentenus left it on day 330 at the Emporium's Nicean wine stalls
   ("sludge mold"; meeting at the Nicean outlet, midnight day 333; the work: the Captain of the Underwatch). The
   company learns of it only by asking at the stalls (Lucilla asked for Vasan there in S16) or through Lucilla's
   month-12 Rumormongering. Destrio wants to know of anyone seeking the Brotherhood. Kwame's masquerade (the den's
   disguises, the passwords) fits here.
4. **Arëtar's proof:** the Provost's ciphered journals or the "rat lycanthropy" vials in Tower Basement 2 (wizard
   locked 9th; the sewer gate 10 wizard locked 10th; magic mouth at 9). A sanctioned mission (1d4 knights). Vestus'
   Tower interview is day 339 (before the Provost and the Regent; admission 12+ on 2d6 +6). A court's verdict on
   Mentenus settles the Order's initiation (another would be given).
5. **Scheduled:** 335 Tertulla's mooring; 338 Caeso Lentulus out of bed (Friendly Watch subaltern); 339 Vestus'
   interview; 340 Phaedra's wage, 347 Varro and Hrodvar, 352 Saturnin, 353 Aelia and Marcellus and the vault fee;
   each week the Brotherhood roll (1-in-6); 360 month 12 ends (Guildhouse fees from member balances, investments 1
   and 3, Iulia's month-end rolls and her monthly report to Arëtar).

**Routine (S17 lessons):** after every return `location --clear` and `location --kind settlement --site Cyfaraun
--wandering none` before any `wait`; spells reset with `dawn N`; `encounter surprise` always with `--party` and
`--monsters`; Vettius plays the thief: hide, rear, `attack vettius T --ambush --extra-dice "backstab:2d6"` on every
vulnerable target (cowering, surprised, helpless, prone, slumbering, paralyzed, or from the rear); his command word
("Freeze") makes a living target helpless for a coup de grace; the Rod's +4 lasts one turn (10 rounds); `rebuke
--target` for undead not yet rebuked; rest when a turn says "rest due in N rounds"; relight a burnt-out lantern
with `light on lanternN`; thrown oil and holy water by an open roll and `damage` (no engine path).


## S19 — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers: source `Playtest/tools/s10_j.sh`,
`s11_mend.sh`, `s13_j.sh`, `s12_town.sh`, then `PARTY="lucilla vettius vestus-the-unlikely neris brennus iulia phaedra
varro hrodvar aelia marcellus saturnin cotta"`. Session 18 log: `Session Log/S18 — Sludge mold.md` (days 330-337).

**State on resume:** day 338 00:53, winter, Cyfaraun (18.05), back at the Solar Citadel from the Nicean outlet. No
adventure open (A49 paid out). Location Cyfaraun (settlement, wandering none). First `wait --hours 8` (the night's
sleep: restful in town), then `dawn 338`. Thirteen: as S18 plus **Cotta** (Vettius' Explorer 2, Outrider: Mounted
Combat, Riding; composite bow, sword, scale; horse holder `cotta-horse`; 50gp, paid to 360). All whole. **Iulia is
Crusader 7** (39 hp; a 4th-level divine spell). Vettius' sword: one of its three words used on day 337.

**What S18 did:** day 331 Cotta hired; Lucilla took Mentenus' note for "Vasan" from the wine-seller; word to the
Order. 333 selling day: L295 identified (Chain Mail +1), Liber 97,762gp (incl. L295, L296), open market 16,310gp
(tax 75 vs 5%: none); everything banked; Gnaeus' later shares held in his name at the Guildhouse. Midnight 333: the
first meeting (Mentenus himself; target Iulia, 6,000gp, 2,000 paid; "the rest the third night after she is found").
334: Destrio sanctioned the retribution; Arëtar declined to stage Iulia's death; a second note to the Tower. 335:
Tertulla to 349; silvered spear (Marcellus) and short sword (Aelia). Midnight 337: Mentenus read Varro's mind (no
surprise), Brennus 15, Vettius "Freeze" (save 3), Lucilla's coup de grace; body sunk; A49 paid out (4,298 XP).

**Open (by the profiles):**
1. Tell the Order (Oppius/Ezelus): the initiation is done; Destrio's answer (AX3 pp. 173-175): deathbringers; then
   weekly assignments (1d4 per deathbringer PC in Cyfaraun, a 4; `Tables/ax3-eclipse-contracts.yaml`).
2. The Tower misses its Provost (from 338). Vestus' interview day 339 (admission 12+ on 2d6 +6, AX3 p. 148): Judge's
   call whether it goes ahead before the Regent alone. Prelate Romus learns he is missing.
3. The Provost's items to name and divide or sell: L326 Dagger +1, L327 Ring of Plant Control (very rare), L328 Helm
   of Comprehension, L329 Wand of Magic Discernment (12 charges), L330 AX3 Potion of Giant Strength (item note
   `Adventure/Items/`); L331 keys (Basement 10: the sewer gate is also wizard locked 10th by Aurëus; Ground Story 4),
   L332 cassock (passes the magic mouth at Basement 9), L333 staff.
4. Arëtar's proof from Basement 2 (journals, vials) now explains the Provost's vanishing; a sanctioned mission.
5. The body in the river: weekly 1-in-6 hidden that it comes ashore (first day 344). The new moon is day 342.
6. Scheduled: 338 Caeso up; 339 interview; 340 Phaedra's wage; 344 Brotherhood roll; 347 Varro, Hrodvar; 349
   Tertulla; 352 Saturnin; 353 Aelia, Marcellus, vault fee; 360 month 12 ends.

**Routine (S18 lessons):** never run `location` without arguments (it resets the site; read it with `clock`); a
class search's market cap is stale (Rulings S18: confirm the month's total, `candidate --level N --class C`, then
`candidate ID --sheet Campaign/candidates/<id>.json` before `hire --publish-to`); animals as holders with `inv holder
add ID --kind animal` (not `inv add --as`); find a thief skill's name before throwing it (`Hiding`, `Sneaking`).

## S19 after the second S18 week — start here (supersedes everything above)
**State on resume:** day 344 18:10, winter, Cyfaraun, the Solar Citadel. No adventure open (A51 paid out). Location
Cyfaraun (settlement). Night of day 344 first (`eat --in-town`, `wait --hours 11`), then `dawn 345`. Thirteen, all
whole: as S18 plus Cotta (Vettius', Explorer 2). Iulia Crusader 7 (39 hp). Vestus is a Tower member (thaumaturge).
The six PCs are deathbringers of the Order (day 340).

**Days 338-344:** Order told (rite day 340); items named (L326 Dagger +1, L328 Helm; L330 potion of giant strength by
the Tower's alchemist; L327 ring, L329 wand unknown); vault day 342 (garnets L334-L351, jars L352, L326-L329, L333).
Descent 42 (A50, day 341): F5 cleared. Descent 43 (A51, day 343): F8 spellsword, F9 looted, F4 swarm and martyr.
Day 344: Arëtar asked Iulia; she kept the oath (his next reaction to her -1). Regent opened Basement 2 (Judge-only:
quiet hunt).

**Open:** the Order's weekly assignments from day 347; F beyond (F10, F11 gallery skeleton rule, F12-F19, F14's secret
door to T); the spellsword's spellbook (Fireball; Necromantic Potence vs the Tower's oath); the ring and the wand;
selling day 361 (month 13: garnets, jars, statuette, bowl, tiles, amethysts at 5% tax); wages 347 (Varro, Hrodvar),
352 (Saturnin), 353 (Aelia, Marcellus, vault fee); Tertulla 349; month end 360.

**Routine (S18 lessons, cont.):** the engine's `rebuke` leaves sepulchral worms out of its pool: apply the MM rule by
hand (worms first, lowest HD); never set many distances in one loop (176 calls timed out: set only the pairs a move
needs); SOTN slabs without the −12 (Rulings S18); holy water on undead = luminous extraordinary 1d8 (no holy type);
a hidden slab-heave helper: `force-door A B --helpers C` (STR −2 helpers hurt).

## S19 after the third S18 week — start here (supersedes everything above)
**State on resume:** day 351 18:00, winter, Cyfaraun, the Solar Citadel. No adventure open (A55 paid out). Location
Cyfaraun (settlement). Night of day 351 first (`eat --in-town`, `wait --hours 12`), then `dawn 352`. Thirteen, all
whole. The clock runs about 3 hours early against the narration (town waits of 12+12 from 06:xx): align with a short
`wait` before the next dawn if it matters.

**Days 345-351:** Iulia reconciled with Arëtar (vigil, 1,000gp tithe, service: reaction 13); his task: the Provost's
remnant (Adventure/AX3/NPCs/The Provost's Remnant.md), three taken alive day 347 (A52), gift 750gp (A53); the court
waits for the full moon (356); the Regent gave Arëtar the journals. Descent 45 (A54, day 349): F12 rector, F13, 44 F11
skeletons; Brennus' Ague cured. Descent 46 (A55, day 351): F10. The Provost's body ashore day 351 (wharf robbers).
Goods for day 361 in the Grey Sisters' vault (garnets, jars L352, the Provost's items, keys, cassock) and the Citadel
barracks (L272, L355-L363, L366-L379; L368 shrine, two bearers).

**Open:** the court (356: Iulia testifies; the three change at the moon); the Watch inquiry weekly (358); Order rolls
354; F11c/F18/F19, F14 (secret door to T1: the Great Teacher), F15-F17; the spellbook; selling day 361 (5% tax: month
13); wages 352 Saturnin (Lucilla), 353 Aelia, Marcellus (Lucilla), vault fee.

**Routine (S18 week 3):** after any fight the walk helper can let "rest due" slip: run `rest` by hand after every fight
before `walk`; relight at once when a turn line says NONE LIT; `inv buy Torch N` buys packs of six; a reward found
after a payout needs its own adventure record (A53); multi-bearer items: `recover --drop`, then `--store` at the return.

## S19 after the fourth S18 week — start here (supersedes everything above)
**State on resume:** day 358 ~12:30, winter, Cyfaraun, the Solar Citadel. No adventure open (A58 paid out). Location
Cyfaraun (settlement). Afternoon and night of day 358 (`wait`, `eat --in-town`, `wait`), then `dawn 359`. Thirteen;
Varro 14/23, Brennus 20/23 (heal overnight). Vestus is studying all week (days 353-359: Fireball replaces Thunderbolt
on day 360: `actor item vestus-the-unlikely add spell "Fireball" --level 3` and remove Thunderbolt; he keeps the
formula); he was out of descents 48 and the cellar.

**Days 352-358:** A56 F18 graves, F11 emptied (all 128 skeletons gone), a Horned Rat cultist taken; A57 F14 serpent
door found (left), F15 dome lever, flying disk L386 (unidentified, base 78,000), F17 fragments L387, cases left
shut; ghouls (one fled), worms; Order assignments: Vestus (Una), Brennus (Rufio: done A58); the court day 356; the
Watch's inquiry closed day 358 (Friendly). Contracts: Adventure/AX3/NPCs/Order Contracts (S18).md.

**Open:** day 360: month end (fees, investments 1 and 3, Iulia's rolls and report, Vestus' dues, Cotta's wage),
Oppius with Brennus' 1,500gp (book it as its own record, like A53); day 361 selling day (identify L386 and L327 first;
the disc: Vestus could steer it, energy crystals are in the F17 lance); Order rolls 361; Una's villa (17.06).

**Routine (S18 week 4):** the torch helper relights on any "burns out" even when another torch still burns: check
the light line; `encounter fight` does not set surprised conditions (set them by hand); grave ghoul fever is the
monster's own rule, not `disease expose`.

## S20 — start here (supersedes everything above)
**Branch:** `ccr-6e7c0096-7nmfvu` in all four repos (tools 7.14.0). Helpers: source `Playtest/tools/s10_j.sh`,
`s11_mend.sh`, `s13_j.sh`, `s12_town.sh`, then `PARTY="lucilla vettius vestus-the-unlikely neris brennus iulia phaedra
varro hrodvar aelia marcellus saturnin cotta"`. New: `python3 Playtest/tools/gh_balances.py` (Guildhouse member
balances from the inventory log; reconciles with the bank). Session 19 log: `Session Log/S19 — The Thelesa villa.md`.

**State on resume:** day 365 17:31, spring (the engine's season turned on day 361), Cyfaraun (18.05), the Solar
Citadel barracks. No adventure open (A62 paid out). Location Cyfaraun (settlement, wandering none). Night of day 365
first (`eat --in-town`, `wait --hours 13`), then `dawn 366`. Thirteen, all whole; **Lucilla's max hp is 23** (the
wraith; enervation ended day 365). Iulia holds the Underwatch spear again (w60, restored day 362: judge-notes).
Vestus casts Fireball (Thunderbolt laid aside, formula kept).

**Days 358-365:** 358 the Mink on the villa; 359 Vettius scouted it; Thelesa Villa built (Adventure/AX3/Dungeons/
Thelesa Villa/); 360 month 12 ended (fees, investments 1 Return and 3 Return +50%, Cotta to 390, Vestus' dues,
A59 Rufio's commission), Arëtar's task (1): the Thelesa haunt with 4 knights; 361 selling day (Liber 9,442gp, open
4,940gp, tax none; L386 to the Tower for 2,000gp, ready day 375; L327 kept back: the Provost's); Order rolls none;
362 A60 the villa (Una slain, wraith destroyed, 9 rats, H40 and H41), A61 Arëtar's gift 750gp; 363 Tertulla to 377,
Vestus' archive clue on the Great Teacher and the F17 alarm; 364 A62 the Order's 2,000gp for Una; Brotherhood roll
1: Liber Faunus seeks "Vasan" (World State, Scheduled events).

**Open:** Liber's note at the wine stalls (Destrio's charge vs the company's fence); F17's cases and the Great
Teacher (the table will not open them until it can fight him with a way out); F14's serpent door; F18's east finger
to I7; F19; the disc (375); the jade ring; Iulia's month-13 report by 390. Scheduled: 368 Order rolls; 369 Phaedra;
372 Brotherhood; 375 disc; 376 Varro, Hrodvar; 377 Tertulla; 382 Saturnin; 383 Aelia, Marcellus, vault fee; 390
month 13 ends (investment 2 rolls again); 391 selling day (villa gems and jewels in the barracks).

**Routine (S19 lessons):** `travel` needs a driver for the cart and rebuilds animals from the inventory: take the
cart along (Hrodvar drives) or plan for it; `state end` does not delete Campaign/combat-state.json (remove it before
the next `encounter fight`); end an encounter before rolling surprise for the next; a spear's broken shaft is
repaired for 1gp, not lost (Rulings S19; check an engine `break` line at once); Loremastery has no recorded throw
in the engine: `throw ID --target N` (18+ less 1 per level after 1st).

## S20 after the second S19 week — start here (supersedes everything above)
**State on resume:** day 372 evening (clock advanced to the evening of 372): night of 372 first (`eat --in-town`,
`wait --hours 13`), then `dawn 373`; spring, Cyfaraun, the Solar Citadel. No adventure open (A66 paid out). Location Cyfaraun
(settlement). Thirteen; **Hrodvar on bed rest to day 381** (3/14 hp, lung mended); Brennus, Iulia, Marcellus
healing. Lucilla max hp 23.

**Days 366-372:** 367 descent 49 (A63): I7, 42 troglodytes slain, no treasure; 368 Order rolls: Vestus (Hrad the
Blood Axe) and Iulia (Balkar), both done (A64 night of 369, A65 night of 370); A66 Hrad's commission (day 371);
372 Liber's second note heard and reported; the Watch optio Indifferent about Balkar.

**Open:** 373 Oppius with Balkar's 1,500gp (book as its own record, A65's participants) and Destrio's answer about
Liber (Judge decides: a contract on Liber, or the Order's own work); 375 the disc named and Order rolls; the
troglodyte hive (chieftain in I2 with the hoard; shaman I13); F14/T; F17; F19; 376 Varro, Hrodvar wages; 377
Tertulla; 382 Saturnin; 383 Aelia, Marcellus, vault fee; 390 month 13 ends; 391 selling day.

**Routine (S19 week 2):** after every `state end`, write the party's hp to the actors by hand (the engine does not);
never rename combatant groups; `roll` "xK" repeats, it does not multiply; night errands: the rollover passes while
awake, reset spells after the morning sleep.

## S20 after the third S19 week — start here (supersedes everything above)
**State on resume:** day 379 ~16:45 (clock), the evening of day 379 in the narration, spring, Cyfaraun, the Solar
Citadel. No adventure open (A68 paid out). Location Cyfaraun (settlement). Night of day 379 first (`eat --in-town`,
`wait --hours 13`), then `dawn 380`. Thirteen: Hrodvar on bed rest to day 381 (3/14); Brennus Fighter 7 (31 hp);
Aelia Bard 6 (wage 800, paid to 383).

**Days 373-379:** A67 Balkar's commission and spellbook (retcon); copying (Vestus, Phaedra); Liber a contract (Neris,
day 376); the disc sold through Liber 62,400gp; A68 Nerio (Iulia's contract, done night of 377); Liber watched:
The Mink, then a chair with 4 bravos to a Memorial Street townhouse (unprepped: build it before entry); Selene's
note for Vasan at the wine stalls (week of 379); Hrad ashore, river robbers blamed.

**Open:** Liber (the table's plan: learn the house, strike when sure, never be seen; consequences in the contracts
note); Selene's note; 380 Oppius (Nerio 1,000gp, its own record); 381 Hrodvar up; 382 Order rolls and Saturnin's
wage; 383 Aelia (800), Marcellus, vault fee; 386 Brotherhood weekly; 390 month 13 ends (fees, investments 1, 2 and
3, Iulia's report and task roll, Vestus' dues, Cotta's wage); 391 selling day (villa gems) and Tertulla; below: the
troglodyte hive (chieftain, hoard in I2), F14/T, F17, F19. Vestus' and Phaedra's new formulas need a week's study
each to enter a repertoire.
