---
type: region
tags:
  - sakkara/region
source: "AX1 Region Map p. 65 (hexes as built into Data/hexes.csv); Türos Tem note; Viaspen Forest note"
---

# Region map — where Türos Tem stands

The campaign's fixed point for any later adventure. Every hex the engine travels through must be a row of
`Data/hexes.csv` (config `hexes`); a hex not in it stops `travel` ("the Judge places the party").

## Grid
- **Numbering:** `CC.RR`, column then row, counted from the north-west corner of the AX1 Region Map (module hex
  `CCRR` = our `CC.RR`, e.g. module 1308 = 13.08).
- **Scale:** 6-mile hexes (RR). North is up; columns run west to east, rows north to south.
- **Offset:** `even-columns-down` (config `hexes.offset`): even-numbered columns sit half a hex lower than odd ones.
  Neighbours of an odd column `C.R`: `C.R-1`, `C.R+1`, `C-1.R-1`, `C-1.R`, `C+1.R-1`, `C+1.R`; of an even column:
  `C.R-1`, `C.R+1`, `C-1.R`, `C-1.R+1`, `C+1.R`, `C+1.R+1`. `hex.py CC.RR` lists them.
- **Built so far:** columns 08-16, rows 02-10 (81 hexes: 54 grassland, 21 forest, 6 swamp).

## Türos Tem — 13.08
- Imperial border fort on a 150' tor between the **Krysivor River** and the **Viaspen Forest**, over a 110' ford;
  grassland, Borderlands, Lawful; Legate Ulrand Valerian's legature (Southern Argollë, Auran Empire). Market class V
  (`Adventure/Markets/Turos Tem (Market).md`). Main gate on the west side.
- Neighbours: 13.07 and 13.09 (N, S); 12.07, 12.08 (NW, SW); 14.07, 14.08 (NE, SE). The Krysivor runs through 12.09,
  13.09, 14.09 and 13.10, just south of the fort.
- Fixed by travel: reaching it fixes a lost party's position (settlement reading); its white walls are visible from
  14.07 (Rulings S04 Judge's call, AX1 p. 5).

## Around it
| Hex | What | Notes |
| --- | --- | --- |
| 13.08 | Türos Tem | the stronghold; inn, hospital, bank (Guildmaster Karanos) |
| 12.07 | farmland edge | the road out to the forest; water found |
| 11.07 | Viaspen crossing | the module's forest check (1d6, 6) each crossing |
| 10.07 | Buried Temple (AX1) | stream camp in the hex; the Lady dead, the Stone destroyed (day 142) |
| 09.06-15.06, 10.04-14.04 | Viaspen Forest | 21 hexes with the module's encounter check (`encounters` column) |
| 09.03-12.03 | Viamir Marshes (swamp) | north of the forest (Lake Laman) |
| 14.04 | Shrine of the White Lady | seed only (unicorn, healing pool; AX1 p. 65) |
| 04.11 | Sinkhole of Evil | seed only, **outside the built map** |
| 17.07 | Ruined Imperial Fortress | bugbear tribe; seed only, outside the built map |
| 17.14 | Watchtower at Eammon Mór | ogre warlord, ~170 beastmen; seed only, outside the built map |
| 22.05 | Ruined Monastery | beastmen and chthonic cultists; seed only, outside the built map |

Places named but not placed (directions not transcribed from the Region Map): **Siadanos** (by the Siadanos highway;
grain, beer, wine, pottery), **Türos Spen** (fish), **Türos Luin** (wood, furs), **Türos Aster** (monster parts), the
**Mirmen** river (the forest's other bound), the dwarves of **Azen Radokh** (mountains), the Dark Wall (cliffs).

## Placing a new adventure
1. Decide where the new module's site lies relative to 13.08 (its own map, a published setting map, or the Judge's
   choice): a hex `CC.RR` on this grid.
2. Add every hex between here and there to `Data/hexes.csv` (terrain from the source map, zone, classification,
   domain, river; `point_of_interest` for the site; `encounters` only for a module's own check) and the site to
   `Data/places.csv`. Keep this numbering: never renumber existing hexes.
3. If the new module has its own hex numbers, convert them with one fixed offset (`ours = theirs + (dC, dR)`). With
   `even-columns-down`, use an **even column offset** or the rows of every other column shift by one.
4. `hex.py <new hex>` and `hex.py --sites 13.08 N` check the result before the first `travel`.

## Secrets of the Nethercity — Cyfaraun (2026-11-21)
- The Nethercity lies under **Cyfaraun**, capital of the Borderlands prefecture (SOTN pp. 4-5; reached through the city's cesspit under the agora).
- **Source map: JJ p. 188 (PDF p. 190), the Borderlands regional map** of the setting-building example (6-mile hexes, 24-mile large hexes; roads dashed). Cyfaraun stands at the north tip of Lake Laman on the Mirmen; the Viamir Marshes lie south of the lake, the Viaspen Forest south-east of the marshes; Türos Tem is at the south-west foot of the Viaspen on the Krysivor.
- **Distance:** measured on that map about **17 hexes (~100 miles), north-north-west** of Türos Tem (calibrated against the JJ's own distances from Cyfaraun: Siadanos 19, Samos 9, Menicos 16, Azen Radokh 20 hexes; measured ±1). SOTN's text says "some fifty miles northwest": the two sources disagree; the map is used.
- **Routes** (hex counts are straight between waypoints, so the roads run a little longer):
  - **East road (recommended):** Türos Tem - road NE to **Türos Aster** (3) - up the Krysivor to **Türos Spen** (4) - road NW past the Viaspen's east edge to **Türos Orn** (9) - road along Lake Laman's east shore to **Cyfaraun** (7): about 23 hexes, ~140 miles, all road, forts every 3-9 hexes for food and water.
  - **West road:** Türos Tem - road W along the south edge of the marshes to **Siadanos** (11) - north up the Mirmen to **Türos Quell** (10) - the lake's west shore to **Cyfaraun** (9): about 30 hexes, ~180 miles.
  - **Shortcuts off-road:** Türos Tem - across the Viamir Marshes to Türos Quell (11, swamp) - road to Cyfaraun (9): ~20 hexes; or Türos Tem - through the Viaspen's east part to Türos Orn (11, thick forest) - road (7): ~18 hexes. Shorter, slower per hex, unroaded and wild.
- **Before travel:** the built map (`Data/hexes.csv`, from the AX1 Region Map) does not reach Cyfaraun and is numbered differently from the JJ sheet. Align the JJ map on Türos Tem = 13.08 (and the Buried Temple = 10.07), then add the route's hexes with terrain, roads (`Data/world.json` roads) and the forts as places. The AX1 map and the JJ map differ in detail (the Viaspen's shape, the marshes); keep the AX1 hexes already built and take the rest from the JJ map.
