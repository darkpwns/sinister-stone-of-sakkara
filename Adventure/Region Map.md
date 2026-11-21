---
type: region
tags:
  - sakkara/region
source: "AX3 Capital of the Borderlands, Regional Map of the Borderlands (Library: Adventures/Capital of the Borderlands/maps/ACKS_borderlands-amended-GM.tif, player copy beside it); AX1 Region Map p. 65; JJ pp. 188-212 (the same Borderlands sandbox)"
---

# Region map — the Borderlands, and where Türos Tem stands

The campaign's fixed point for travel. Every hex the engine travels through must be a row of `Data/hexes.csv`
(config `hexes`); a hex not in it stops `travel` ("the Judge places the party").

## Grid (since S07, 2026-11-21)
- **Sheet:** the AX3 Regional Map of the Borderlands (51 columns × 32 rows of 6-mile hexes; 24-mile large hexes).
  Numbering `CC.RR`, column then row, **01.01 at the sheet's top-left hex**. North is up.
- **Offset:** `even-columns-down` (config `hexes.offset`): even columns sit half a hex lower. Neighbours of an odd
  column `C.R`: `C.R-1`, `C.R+1`, `C-1.R-1`, `C-1.R`, `C+1.R-1`, `C+1.R`; of an even column: `C.R-1`, `C.R+1`,
  `C-1.R`, `C-1.R+1`, `C+1.R`, `C+1.R+1`. `hex.py CC.RR` lists them.
- **Earlier numbering:** S01-S07 used the AX1 Region Map's numbers (Türos Tem 13.08). Old hex ≈ new hex (+9, +12),
  with the AX1 route fixed to AX3: 13.08 → 22.20, 12.07 → 21.20, 11.07 → 20.19, 10.07 → 19.19 (session logs, the
  roll log, the Judge notes and the Rulings before S07 keep the old numbers). AX1's seed sites land on AX3's: Shrine of
  the White Lady 23.16 (#21), Ruined Imperial Fortress 26.19 (#30).
- **Built:** 414 hexes, **columns 14-31, rows 2-24**: everything from Türos Quell and the Mirmen in the west to the
  Blood River and Türos Zera in the east, and from Mityethtem and Luseatum in the north to the Lusaun Forest and Türos
  Luin in the south (Cyfaraun, Lake Laman, the Viamir Marshes, the Viaspen, the Naungollë). Terrain read hex by hex from
  the AX3 map (S07); classification (civilized, borderlands, outlands, wilderness) from the JJ's classification map of
  the same sandbox (JJ p. 210); zone from the JJ's alignment lines; domain: the nearest fort's ruler (AX3 entries),
  none in wilderness or on the lake. The Viaspen's forest hexes carry AX1's forest check. Lake Laman (18 hexes) is
  impassable. Record of the build: `Playtest/tools/map/` (README, `extend_s07.py`). **AX3 gazetteer extension** (2026-11-21, `extend_ax3.py`): +40 hexes, 454 in all: the hex of each of the 36 AX3 points of interest outside the block (single hexes, not yet joined by travel hexes) and Siadanos (#34, 11.21) with its two road corridors (13.21, 12.20; 13.19, 12.19). Classification from AX3's domain records (the JJ map is not in the container), zone extrapolated. Every AX3 site #1-#53: [[Borderlands Gazetteer]].
- **Roads** (`Data/world.json`): the Imperial road Türos Tem - Aster - Spen - Orn - Cyfaraun (23 hexes); Cyfaraun -
  Türos Quell along the lake's west shore (9); Türos Tem - Siadanos westward along the Lusaun to Siadanos 11.21 (11); Türos Tem
  - Türos Luin (4); Türos Quell - Siadanos down the Mirmen to Siadanos (10). Roads north of Cyfaraun and Orn and east of
  the Krysivor are drawn on AX3 but not entered.
- **Settlement notes:** Türos Tem, Türos Aster, Türos Spen, Türos Orn, Cyfaraun (each with a market note in
  `Adventure/Markets/`). The other forts, towns and sites have short notes in `Adventure/AX3/Gazetteer/` (all
  in `Data/places.csv`).

## Türos Tem — 22.20 (AX3 #28)
- Fort on a 150' tor between the Krysivor and the Viaspen, over a ford; Legate Ulrand Valerian. Outlands on the JJ
  classification map (the AX1 map had borderlands). Neighbours: 22.19, 22.21, 21.20, 21.21, 23.20, 23.21.
- The Buried Temple (#27) is 19.19, three hexes west-north-west: 22.20 → 21.20 → 20.19 → 19.19.

## The east road to Cyfaraun (Secrets of the Nethercity)
The Nethercity lies under **Cyfaraun** (#10, 18.05), capital of the prefecture (SOTN pp. 4-5; AX3). One road,
`Data/world.json` → "Imperial road (Türos Tem - Türos Aster - Türos Spen - Türos Orn - Cyfaraun)", 23 hexes (138 miles):

| Leg | Hexes | Steps | Terrain on the way |
| --- | --- | --- | --- |
| Türos Tem 22.20 → Türos Aster 25.19 (#29, Legate Nicus Balens) | 23.20, 24.19 | 3 | grassland, one hill hex (24.19); outlands |
| Türos Aster → Türos Spen 28.16 (#22, Legate Süromus Drakon) | 26.18, 26.17, 27.17 | 4 | along the Krysivor's north-west bank; outlands |
| Türos Spen → Türos Orn 23.10 (#15, Palatine Valanna Telpirion) | 27.16, 26.15, 26.14, 25.14, 25.13, 24.12, 24.11, 23.11 | 9 | the gap between the Viaspen and the Naungollë; outlands, then borderlands, then civilized |
| Türos Orn → Cyfaraun 18.05 (#10, Prefect Basilio) | 22.09, 21.09, 20.08, 20.07, 19.07, 18.06 | 7 | Lake Laman's north-east shore; civilized |

Forts every 3-9 hexes; Türos Orn is a small town (class IV), Cyfaraun a city (class III).
Beyond the built block (Samos, the Waste, the far north; their site hexes exist, the hexes between do not): extend from the same map the same way first.
