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
- **Built:** 150 hexes: columns 17-26, rows 14-23 around Türos Tem, the Viaspen and the Viamir Marshes, and the east
  road with one hex on each side up to Cyfaraun. Terrain read from the AX3 map; classification (civilized, borderlands,
  outlands, wilderness) from the JJ's classification map of the same sandbox (JJ p. 210); zone from the JJ's
  alignment lines (the forts of the Unbroken Line on the neutral axis; Orn and Cyfaraun lawful); domain: the nearest
  fort's ruler (AX3 entries), none in wilderness. The Viaspen's forest hexes carry AX1's forest check.

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
Not built yet: the west road (Türos Tem - Siadanos - Türos Quell - Cyfaraun) and the rest of the sheet; build them
from the same map the same way before travelling off this corridor.
