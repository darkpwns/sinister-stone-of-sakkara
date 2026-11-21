#!/usr/bin/env python3
"""AX3 gazetteer extension of Data/hexes.csv (2026-11-21): one hex for each AX3 point of interest outside the S07 block
(columns 14-31, rows 2-24), plus the road corridors from the block's edge to Siadanos (#34). Run from the repo root.
Site hexes are the printed markers on the GM map (ax3grid.py crop/hex); terrain read hex by hex from the map
(ax3grid.py tiles; the forts' and lairs' symbols checked against AX3's text). The JJ classification map is not in the
container, so classification comes from AX3's domain records (AX3 pp. 27-31: civilized -> civilized, border ->
borderlands, wild -> outlands for a fort's own hex; Siadanos and Menicos borderlands as JJ p. 210 says), unsettled sites
wilderness; zone extrapolates the S07 alignment lines (lawful north-west, chaotic beyond the Krysivor's east and the
Dark Wall); domain is the site's own ruler, none in wilderness. Also extends the two Siadanos roads in Data/world.json.
Kept as the record of how these hexes were set; re-running adds nothing already present."""
import csv, io, json
def S(s): return s.split()
terrain = {**{h: "grass" for h in S("08.02 14.01 33.02 39.04 43.01 03.08 10.08 36.07 34.09 07.15 39.16 11.21 18.25 "
                                     "13.21 12.20 13.19 12.19")},
           **{h: "forest" for h in S("45.04 40.08 47.13 13.23")},
           **{h: "hills" for h in S("09.22 11.27 15.27 26.26 46.27")},
           **{h: "mountains" for h in S("04.19 43.20 32.24 38.21 04.25 30.27 08.29 21.30")},
           **{h: "barrens" for h in S("35.24 41.23 40.28 44.25 32.29")},
           "36.27": "scrub"}
river = {**{h: "Krysivor" for h in S("39.04 43.01 36.07 34.09 18.25")},
         **{h: "Mirmen" for h in S("11.21 11.27 08.29 13.19 12.19")}, "40.28": "Tiamak"}
zone = {**{h: "lawful" for h in S("08.02 14.01 33.02 03.08 10.08 07.15 04.19 11.21 13.21 12.20 13.19 12.19 09.22")},
        **{h: "neutral" for h in S("39.04 43.01 36.07 34.09 13.23 11.27 15.27 18.25 21.30")}}
cls = {**{h: "civilized" for h in S("14.01 10.08 04.19")},
       **{h: "borderlands" for h in S("08.02 33.02 39.04 43.01 03.08 34.09 07.15 11.21 13.21 12.20 13.19 12.19")},
       **{h: "outlands" for h in S("36.07 11.27 15.27 18.25")}}
ruler = {"08.02": "Legate Cadom Stodius", "14.01": "Legate Achon Staios", "33.02": "Palatine Attenus Korbus",
         "39.04": "Legate Vandelus Pylon", "43.01": "Legate Retunus Natherian", "03.08": "Legate Daros Elpides",
         "10.08": "Palatine Vason Krateros", "36.07": "Legate Marcan Hilerno", "34.09": "Legate Peristo Pelagios",
         "07.15": "Legate Manthus Mirasca", "04.19": "Norden Radokh", "11.21": "Palatine Theremus Augilian",
         "13.21": "Palatine Theremus Augilian", "12.20": "Palatine Theremus Augilian",
         "13.19": "Palatine Theremus Augilian", "12.19": "Palatine Theremus Augilian",
         "11.27": "Legate Aurius Mennictor", "15.27": "Legate Lammirio Nuvicerres", "18.25": "Legate Jonus Tacillus"}
poi = {"08.02": "#1 Sarotem", "14.01": "#2 Kruantem", "33.02": "#4 Menicos", "39.04": "#5 Turos Veren",
       "43.01": "#6 Turos Aure", "45.04": "#7 Lair of the Manticores", "03.08": "#8 Andrastem", "10.08": "#9 Samos",
       "36.07": "#12 Turos Gundan", "40.08": "#13 Lair of the Warlock", "34.09": "#18 Turos Augil", "07.15": "#19 Zelictum",
       "39.16": "#24 Burial Mound of the Empyreans", "47.13": "#25 Ruined City of Cyfandir", "04.19": "#26 Azen Radokh",
       "43.20": "#32 Fortress of Gorgbad", "09.22": "#33 Dragon's Tor", "11.21": "#34 Siadanos", "13.23": "#35 Sinkhole of Evil",
       "32.24": "#37 Wyvern Cliffs", "35.24": "#38 Nurgarog", "38.21": "#39 Temple of the Stone Horns",
       "41.23": "#40 Fist of Telith", "04.25": "#41 Ruins of Azen Kairn", "11.27": "#42 Turos Telle", "15.27": "#43 Turos Erin",
       "18.25": "#44 Turos Drav", "26.26": "#45 Watchtower at Eammon Mor", "30.27": "#46 Eyrie of the Dread Eye",
       "36.27": "#47 Arwia Oasis", "40.28": "#48 Ruins of Zahar", "44.25": "#49 Morgot",
       "46.27": "#50 Valley of the Sorcerer Kings", "08.29": "#51 Redoubt on the Earthway",
       "21.30": "#52 Sepulcher of the Sorceress-Queen", "32.29": "#53 Nabu-Kudur"}
rows = list(csv.DictReader(open("Data/hexes.csv", encoding="utf-8")))
have = {r["hex"] for r in rows}
added = 0
for h, t in terrain.items():
    if h in have:
        continue
    rows.append({"hex": h, "terrain": t, "zone": zone.get(h, "chaotic"), "river": river.get(h, ""),
                 "domain_ruler": ruler.get(h, ""), "domain_kind": "", "classification": cls.get(h, "wilderness"),
                 "land_revenue_gp": "", "point_of_interest": poi.get(h, ""), "encounters": "", "lake": ""})
    added += 1
rows.sort(key=lambda r: (int(r["hex"][:2]), int(r["hex"][3:])))
out = io.StringIO(); w = csv.DictWriter(out, fieldnames=list(rows[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rows)
open("Data/hexes.csv", "w", encoding="utf-8").write(out.getvalue())
# roads: on from the block's edge to Siadanos
W = json.load(open("Data/world.json", encoding="utf-8"))
ext = {"Road Türos Tem - Siadanos (west, along the Lusaun)": ["13.21", "12.20", "11.21"],
       "Road Türos Quell - Siadanos (down the Mirmen)": ["13.19", "12.19", "12.20", "11.21"]}
for k, tail in ext.items():
    if W["roads"][k][-1] != "11.21":
        W["roads"][k] += tail
open("Data/world.json", "w", encoding="utf-8").write(json.dumps(W, ensure_ascii=False, indent=1))
print(added, len(rows))
