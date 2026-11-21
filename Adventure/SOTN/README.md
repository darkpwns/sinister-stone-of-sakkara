---
type: build-checklist
tags:
  - sakkara/secret
source: "AX2 Secrets of the Nethercity (Autarch, ACKS I), 186 PDF pages; printed page = PDF page − 2"
---

# AX2 Secrets of the Nethercity — Judge notes: build checklist

Judge only. Prep for the Sakkara campaign, not play: no `Campaign/` state, actors, roll log or inventory are touched, and
the adventure is not opened in the engine. Source: Library `Adventures/_source/Secrets_of_the_Nethercity.pdf` (186 PDF
pages; page references are printed pages, "SOTN p. N" = PDF page N + 2; the whole map is on pp. 23 and 182-183).
Statblocks and rules converted from ACKS I to ACKS II by the acks2-conversion method with the rules vault's Monstrous
Manual notes and the engine's tables (the skill's scripts are not in the cloud container); notes structured by the
module-vault method. The city above is AX3 (`Adventure/AX3/`), linked, not repeated.

## Layout
| Path | Contents |
| --- | --- |
| `SOTN Hub.md` | premise, getting in, procedures, links, four `Running …` sections (sewer caves first, read by `--hub`) |
| `Nethercity History.md` | background, the three cities, timeline, the Awakening, the gods (SOTN pp. 5-10, 174-175) |
| `Nethercity Features.md` | standing rules: doors, inscriptions, sarcophagi, sludge and miasma, sinkholes, teleport wards, wall graves, necromancy by era, treasure (pp. 10-18) |
| `Nethercity Factions.md` | groups inside and above, their NPCs (traits, voice) |
| `Areas/` | one note per area A-T, room by room (`Nethercity X - Name.md`, hex 18.05) |
| `Tables/` | acks-table/1 YAML (`source.campaign: true`) |
| `Bestiary/` | `<Name> (SOTN).md` statblock notes (new monsters, named NPCs) |
| `Classes/` | JJ ch. 12 builds of the corrupt-elf classes, `sotn-class-builds.yaml` |
| `SOTN Magic Items.md`, `SOTN Spells.md` | Appendices A and C |

## Parts (SOTN PDF pages)
- [x] Hub (`SOTN Hub.md`), `Nethercity History.md`, `Nethercity Features.md` — PDF 6-24, 176-177
- [x] Tables: 4 wandering columns (2d10), unsettling events, mummy reaction, 5 wall-grave tables — PDF 16-22
- Areas (PDF 26-130):
  - [x] A, B, C (PDF 26-35): A1-A4, B1-B5, C1-C12; A 30 gp / 517 XP, B 3,603 gp / 1,050 XP, C 5,545 gp / 3,388 XP
  - [x] D, E (PDF 35-44): D1-D9, E1-E9 with sub-keys; D 11,216 gp / 1,974 XP, E 6,616 gp / 3,680 XP
  - [x] F (PDF 45-53): F1-F19 (+F11a-c); 18,290 gp, 6,759 XP
  - [x] G (PDF 53-65): G1-G27 with sub-keys; 70,195 gp / 14,288 XP
  - [x] H (PDF 65-79): H1-H26 with sub-keys; 32,550 gp + ~2,232 gp graves / 9,963 XP (+ up to 6,240 for the 480 H14 skeletons)
  - [x] I, J (PDF 79-92): I1-I14, J1-J15; I 13,172 gp as printed (9,497 corrected) / 3,725 XP, J 24,300 gp / 6,714 XP
  - [x] K, L (PDF 92-102): K1-K12, L1-L20; K 43,688 gp / 7,540 XP, L 3,789 gp / 4,504 XP
  - [x] M, N (PDF 102-113): M1-M22, N1-N13; M 37,290 gp / 4,840 XP, N 79,850 gp / 3,800 XP
  - [ ] O, P, Q (PDF 113-125)
  - [x] R, S, T (PDF 125-130): R1-R4, S1-S4, T1-T2; R 15,500 gp / 9,344 XP, S 23,625 gp / 10,630 XP, T 15,000 gp / 5,000 XP
- [x] New monsters (Appendix B, PDF 143-153): 17 notes in `Bestiary/` (plus named NPCs from the area writers)
- [x] Magic items and spells (Appendices A and C, PDF 131-142, 154-162): 47 item entries, 42 spells
- [ ] Classes (Appendix D, PDF 163-175)
- [ ] `Nethercity Factions.md` (NPCs and factions, from the area notes)
- [ ] Merges into the AX3 notes (Old District #12u, Organizations of Cyfaraun, Undercity of Cyfaraun, Cyfaraun)
- [ ] Final checks: tables through `load_campaign_table`, hub through `read_hub`, `hex.py 18.05`, `brief.py`, independent check

## Work in progress
Unticked parts may already have files on main (snapshots of parts still being written). A part is done only when ticked.

## Open items
- **Wandering column per area** (Judge's call; SOTN gives columns by terrain only): sewer caves A, C, L; volcanic caves
  I, M; temple/tomb B, D-H, J, K, N, O, Q-T; river P. **Dungeon levels** 2 / 3 / 4 / 5 by the columns' threat (SOTN
  p. 19: 1-2, 2-3, 3-4, 4-6).
- Wandering table "faewyrd" read as the lesser faewyrd; "jackals of shadow" are SOTN's jackals of darkness (Appendix B).
- SOTN p. 10 dates the cesspit collapse "329 BE"; the timeline (p. 8) and "about fifty years ago" give 329 IY.
- SOTN p. 5: Cyfaraun "some fifty miles northwest of Türos Tem"; the campaign map (AX3 sheet) has 18.05 vs 22.20, 138
  road miles. The map stands.
- **AX3/SOTN:** SOTN p. 18 calls the Undercity syndicate the "Argollëan Brotherhood"; AX3 calls it the Argollëan
  Family (the Mink, Liber Faunus). Read as the same organisation.
- Sludge: SOTN's middle rules used (not the cinematic or "cruel realism" options, p. 12).
- SOTN gives no restocking rate for living groups; the hub suggests AX1's as a model (Judge's call).
