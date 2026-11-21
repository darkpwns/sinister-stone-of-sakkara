---
type: build-checklist
tags:
  - sakkara/secret
source: "AX3 Capital of the Borderlands (Autarch 2018, ACKS I), 226 PDF pages; printed page = PDF page − 2"
---

# AX3 Capital of the Borderlands — Judge notes: build checklist

Judge only. Prep for the Sakkara campaign, not play: no `Campaign/` state, actors, roll log or inventory are touched.
Source: Library `Adventures/Capital of the Borderlands/_source/AX3_Capital_of_the_Borderlands.pdf`; maps in
`Adventures/Capital of the Borderlands/maps/`. Page references are printed pages ("AX3 p. N" = PDF page N + 2).
Statblocks and rules converted to ACKS II (acks2-conversion method; the rules vault's MM notes and tables, since the
skill's calculator scripts are not in the cloud container). The Secrets of the Nethercity module is a separate job.

## Layout
| Path | Contents |
| --- | --- |
| `AX3 Hub.md` | premise, procedures, links, `Running …` sections |
| `City/` | one note per district (8), organizations, buildings (city-building system), doing business, streets, undercity, the Imperial Vanguard |
| `Dungeons/` | one note per keyed level of each special location |
| `Tables/` | acks-table/1 YAML (`source.campaign: true`) |
| `Gazetteer/` | Borderlands points of interest #1-#53 (except the five with notes in `Adventure/`) |
| `Borderlands Gazetteer.md` | index of all 53 sites with hexes |
| `Bestiary/` | `<Name> (AX3).md` statblock notes |
| `AX3 Magic Items.md` | new magic items |

## Parts (AX3 PDF pages)
- [x] Hub (`AX3 Hub.md`): premise, 14 `Running …` sections (Undercity first, read by `--hub`), links to every note, procedures (city encounters, rumours, factions, hiring, services, city-building, Borderlands) — PDF 6-8 and the city chapters
- [x] City chapters: `City/Organizations of Cyfaraun.md`, `City/Buildings of Cyfaraun.md` (29 `ax3-building-*` tables), `City/Doing Business in Cyfaraun.md`, `Tables/ax3-rumours.yaml`, `Tables/ax3-borderlands-demand-modifiers.yaml` (reference, not a roll table); merged into `Adventure/Cyfaraun.md` and `Adventure/Markets/Cyfaraun (Market).md` (class III kept; all 31 AX3 demand modifiers) — PDF 36-59, 224-225
- [x] Streets and Undercity: `City/Streets of Cyfaraun.md`, `City/Undercity of Cyfaraun.md`; tables `ax3-city-encounters`, `ax3-undercity-encounters`, `ax3-undercity-special`, `ax3-irritating-rumours`; `Bestiary/Rhagodessa (AX3).md` — PDF 60-69, 203
- City districts (8):
  - [x] Old District (PDF 70-99): `City/Old District.md`; dungeons `The Mink - Tavern`, `The Mink - Family Hideout`, `Shrine of the Horned Rat`, `Doppelganger Den`; 13 `ax3-old-*` tables
  - [x] Festival District (PDF 100-126): `City/Festival District.md` (gladiatorial games, betting, Blood Moon); dungeons `Imperial Amphitheater - Arena`, `- Basement`, `Silk Pony Inn - Ground Floor`, `- Top Floor`, `Sand and Bones Hideout`, `Lizardman Sewer Lair`; 21 `ax3-festival-*` tables; 14 bestiary notes
  - [x] Bridge District (PDF 127-137): `City/Bridge District.md`; dungeons `Solar Citadel`, `Catacombs of the Patriarchs`; 5 `ax3-bridge-*` tables
  - [x] Plaza District (PDF 138-143): `City/Plaza District.md`; dungeon `Crocodile Nest`; 4 `ax3-plaza-*` tables
  - [x] Tower District (PDF 144-161): `City/Tower District.md` (joining the Tower, services); dungeons `Tower of Knowledge - Ground Story`, `- Second Story`, `- Third Story`, `- Fourth Story`, `- Fifth Story`, `- Basement`; 3 `ax3-tower-*` tables
  - [x] Temple District (PDF 162-178): `City/Temple District.md`; dungeons `Catacombs of the Ancestors`, `Eclipse Hideout`; 8 tables (`ax3-temple-*`, `ax3-orphan-gifts`, `ax3-eclipse-*`, `ax3-retribution-*`)
  - [x] Lake District (PDF 179-187): `City/Lake District.md`; dungeon `Death Cult Hideout`; 7 `ax3-lake-*` tables
  - [x] Palace District (PDF 188-196): `City/Palace District.md` (no keyed special location); 9 tables (`ax3-palace-*`, `ax3-prefect-dungeon-prisoners`, `ax3-courthouse-trials`)
- [x] Tables: 120+ acks-table/1 files in `Tables/` (listed in the hub)
- [x] Dungeons: 22 notes in `Dungeons/` (one per level or floor), listed with their settings in the hub
- [x] Gazetteer #1-#53 with hexes: 48 notes in `Gazetteer/` (incl. `Buried Temple`), `Borderlands Gazetteer.md` (index), `Borderlands Background.md` (PDF 9-18); tables `ax3-beastman-tribe`, `ax3-borderlands-rumors`; `Data/places.csv` +41 rows; `Data/hexes.csv` +40 rows (454: each outside site's own hex, plus Siadanos road hexes 13.21, 12.20, 13.19, 12.19); `Data/world.json` Siadanos roads extended; record `Playtest/tools/map/extend_ax3.py` — PDF 19-35
- [x] Bestiary and items: 58 notes in `Bestiary/`; `AX3 Magic Items.md` (New Magic Items p. 194, and every placed item by district); `City/Imperial Vanguard.md` — PDF 193-202
- [ ] Final check: `hex.py 18.05`, `brief.py`

## Work in progress
Unticked parts may already have files on main: snapshots of chapters still being written (district notes, dungeons, gazetteer, bestiary, tables). A part is done only when ticked above.

## Open items
- Undercity dungeon level 2 is a Judge's call (AX3 gives none).
- AX3 city table skips 113-114 (p. 62): set to "run 109-112"; escaped prisoner's 1d10 lacks a 5 (p. 67): given to the Argollëan Family. Both Judge's calls.
- AX3 p. 59 prints #73u for the Vagrant Colony (it is #75u); "Noble Charter Inn" read as the Imperial Charter Inn (#74).
- Rhagodessa: no stats in AX3; ACKS I values converted. Ankheg → Giant Acanthaspis (no MM ankheg). Knock / magic rope have no ACKS II spell (battering ram, weave smoke suggested).
- The overview chapter's POI numbers often differ by 1-2 from the district chapters (Palace #78/#80, Temple Barracks #65/#67, Vagrant Colony #73u/#75u): the district chapters' numbers are used.
- Demand modifiers: AX3's arbitrage notes (p. 223) disagree with its table for Cyfaraun (common/precious metals, semiprecious stones, gems) and Siadanos (grain, tea): table values used. The table has no Türos Aster column. Samos is Class VI in AX3 (the JJ example had IV). The Türos Orn and Türos Spen market notes say AX3 gives no demand modifiers; it does (pp. 222-223): those notes are not yet updated.
- Buildings: the "Patrician Family" sub-table is not printed; NPC Class table (p. 53) read as two rolls; ten ACKS I classes there have substitutes named; Plaza/Festival roof table's first row printed 10-50, read as 01-50.
- Dungeon levels: AX3 prints none for the Undercity or its special locations. Judge's calls: Undercity 2; Old District sites 3 (3-4 HD residents); Catacombs of the Patriarchs and Crocodile Nest 1; Death Cult Hideout 2.
- No ACKS II class for ACKS I Mystic (Lubbo keeps AX3's statline) or Anti-Paladin (Rhankur on the Paladin progression); Romus's Apostasy has no ACKS II equivalent. Spells with no ACKS II equivalent: some mapped by effect (summon berserkers → Summon Manes, summon hero → Conjure Imp, ward against elementals → Energy Protection), others keep ACKS I names (unseen servant, ESP, ring of spell turning, cloak of displacement): reconcile.
- AX3 misnumberings: death cult #73u (pp. 128, 182) is #75u; crocodile #44u (p. 130) is #45u. Malthusia's keys "to 4 and 10" (p. 185) read as 9 and 10. Shrine of the Horned Rat: two secret doors in room 2 lead nowhere keyed. Only nine wererat hp printed for ten (p. 92). Celictor's beast table says 1d10, lists 20 (1d20 used).
- No statlines in AX3 for the six minor councillors; no price for Celictor's capture premium.
- Festival: Maximus converted on the MM Devil Boar (limit of 9 thralls vs AX3's 12 charmed beastmen plus Selene); his stable is 15 beastmen on p. 101, 12 on p. 106. Special table prints two 9s (made a 1d2); lift-cargo result 2 missing (folded into the lion). No odds printed for bouts to the death or Blood Moon betting. Mara's detect evil / detect secret doors have no ACKS II arcane equivalent. Monthly games (p. 101) vs seasonal bout procedure: not reconciled in AX3.
- Classed-NPC XP recomputed by ACKS II rules (level as HD plus abilities): several differ from AX3's printed XP (e.g. Mara 200 vs 500).
- Temple/Vanguard: Gabriol run as a Mage (keeps his sword); Irial as Elven Spellsword and Nikolaus as Fighter (their AX3 classes are not in ACKS II); Süromus a Crusader with a shaman's list. Eclipse Hideout pits (text one, map two) set at 10' deep, 1d6; paladin knight ranks built; chest blast runes 16 damage (all Judge's calls). Cellë fights with a sword (printed flail); Valara AC 7 (printed 8). Thelesa villa (Una's home) has no keyed entry.
- Gazetteer: 36 sites lie outside columns 14-31, rows 2-24; only their own hexes were added (plus the Siadanos road), so `travel` cannot yet reach most of them overland (no connecting hexes): extend the block by the README method before a trip there. Classification of the new hexes from AX3's domain records (pp. 27-31) and JJ text (the JJ classification map is not in the container); zone extended by estimate; mountain and Waste terrain read from the map. AX3 names legates Tavic Uctum (Luseatum) and Bellos Ionnicato (Türos Zera); `Data/places.csv` keeps "Legate of …". AX3 misprints: Türos Orn garrison rate (p. 31), Samos "Other" lines (p. 29), Türos Tem peasants 700/725 (p. 32). Dire orcs have no statblock in AX3. Sites detailed in AX4-AX6 are noted, not keyed.
- Tower/Palace: Arcane Vault "six chests", five listed (p. 158); Basement room 11 read as the large laboratory (map p. 217). Essir: `Organizations of Cyfaraun` says he is not to blame for the Prefect's madness, AX3 p. 190 says his curse worsens it (reconcile). Palace is #80 (p. 188; #78 is Tirendoros Harbitan). ACKS II values used over AX3's for Mentenus's throws, Jannion AC 11 (AX3 10), Tarcalus AC 2 (AX3 0), the subaltern's HD. Spells with no ACKS II arcane equivalent marked †. Hurgon (Dwarven Machinist) on Vaultguard throws. Moon Tea save read as vs Death. Barracks Vault payroll and transmogrifiers' presence chance not given.
- Market notes for Türos Orn and Türos Spen say AX3 gives no demand modifiers; AX3 pp. 222-223 give both (see `Tables/ax3-borderlands-demand-modifiers.yaml`).
