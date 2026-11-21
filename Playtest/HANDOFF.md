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

## Next session: the journey to Cyfaraun (Secrets of the Nethercity) — start here
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
