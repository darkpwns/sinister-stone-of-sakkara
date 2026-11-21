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
