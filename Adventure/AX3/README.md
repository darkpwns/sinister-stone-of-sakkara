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
- [ ] Hub (`AX3 Hub.md`) — intro PDF 6-8 and the procedures from the city chapters
- [x] City chapters: `City/Organizations of Cyfaraun.md`, `City/Buildings of Cyfaraun.md` (29 `ax3-building-*` tables), `City/Doing Business in Cyfaraun.md`, `Tables/ax3-rumours.yaml`, `Tables/ax3-borderlands-demand-modifiers.yaml` (reference, not a roll table); merged into `Adventure/Cyfaraun.md` and `Adventure/Markets/Cyfaraun (Market).md` (class III kept; all 31 AX3 demand modifiers) — PDF 36-59, 224-225
- [x] Streets and Undercity: `City/Streets of Cyfaraun.md`, `City/Undercity of Cyfaraun.md`; tables `ax3-city-encounters`, `ax3-undercity-encounters`, `ax3-undercity-special`, `ax3-irritating-rumours`; `Bestiary/Rhagodessa (AX3).md` — PDF 60-69, 203
- [ ] City districts (8): Old 70-99, Festival 100-126, Bridge 127-137, Plaza 138-143, Tower 144-161, Temple 162-178, Lake 179-187, Palace 188-196
- [ ] Tables (district special encounters and the rest)
- [ ] Dungeons (special locations, one note per level)
- [ ] Gazetteer #1-#53 with hexes; `Data/places.csv`, `Data/hexes.csv` — PDF 19-35
- [ ] Bestiary and items; Imperial Vanguard — PDF 193-202
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
