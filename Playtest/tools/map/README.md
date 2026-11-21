# Map tools: the AX3 Borderlands sheet

`ax3grid.py` (grid parameters in `ax3_grid.json`) puts the campaign's hex numbers on the AX3 Regional Map of the
Borderlands in the Library repo (`Adventures/Capital of the Borderlands/maps/`). How the built hexes were made
(S07, 2026-11-21), and how to extend `Data/hexes.csv` the same way:

1. **Route:** `ax3grid.py crop C1.R1 C2.R2 out.png` and follow the dashed road hex by hex; check each step is a
   neighbour (`hex.py`) and the leg counts match the map.
2. **Terrain:** `ax3grid.py tiles out.png HEX ...` and read each tile: grass (open), forest (crowns and squiggles),
   swamp (tufts), lake (shore and wave lines; `terrain=lake`, `lake=yes`, impassable), hills (hill symbol); rivers by
   name in `river`.
3. **Classification:** the JJ's classification map of the same sandbox (JJ p. 210, PDF p. 211, embedded image 1014×784:
   white civilized, light grey borderlands, dark grey outlands, red wilderness), registered to this grid through the
   forts' markers. **Zone:** the JJ's alignment lines (JJ p. 188): lawful north and west of the blue line, neutral
   between, chaotic east of the red line (the engine does not read zone).
4. **Domain:** the nearest fort's ruler (AX3 gazetteer entries), none in wilderness; **places** in `Data/places.csv`;
   roads as paths in `Data/world.json` (`{name: [hex, ...]}`, consecutive neighbours).
5. Check with the engine's hex map: every road step adjacent and `on_road`, every hex present.
