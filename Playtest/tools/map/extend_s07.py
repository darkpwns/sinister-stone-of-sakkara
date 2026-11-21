#!/usr/bin/env python3
"""S07 extension of Data/hexes.csv: columns 14-31, rows 2-24 of the AX3 sheet (terrain read from the map by the Judge,
2026-11-21; classification and zone from the JJ maps, precomputed in CLS). Kept as the record of how the hexes were set."""
import csv, io, json, sys
CLS = sys.argv[1]                      # {hex: {cls, zone}} for the new hexes
def S(s): return set(s.split())
forest = S("14.17 14.18 14.19 14.21 14.22 14.23 14.24 15.17 15.18 15.19 15.22 15.23 15.24 16.21 16.22 16.23 22.13 22.24 23.24 "
           "26.09 26.10 26.11 26.24 27.07 27.08 27.09 27.10 27.11 27.12 27.13 27.20 27.21 27.22 27.23 27.24 "
           "28.06 28.07 28.08 28.09 28.10 28.11 28.12 28.13 28.14 28.18 28.19 28.20 28.21 28.22 28.23 28.24 "
           "29.07 29.08 29.09 29.10 29.11 29.12 29.13 29.14 29.19 29.20 29.21 29.22 29.23 "
           "30.06 30.07 30.08 30.09 30.10 30.11 31.07 31.08 31.14 31.15 31.16")
swamp = S("15.14 15.15 15.16 16.13 16.14 16.15 16.16 16.17 16.18 17.13 18.13 19.13 20.13 21.13")
lake = S("17.08 18.08 17.09 17.10 17.11 17.12 18.09 18.10 18.11 18.12 19.10 19.11 19.12 20.10 20.11 20.12 21.11 21.12")
hills = S("31.17")
river = {**{h: "Mirmen" for h in S("21.02 20.02 20.03 19.03 19.04 16.07 16.08 16.09 16.10 16.11 16.12 15.12 15.13 14.13 14.14 14.15")},
         **{h: "Krysivor" for h in S("30.13 30.14 31.13 30.15 21.24")},
         **{h: "Blood" for h in S("30.16 30.17 31.18 31.19 31.20 31.21 31.22 31.23 31.24")}}
poi = {"15.13": "#20 Turos Quell", "24.02": "#3 Mityethtem", "29.06": "#11 Luseatum", "30.14": "#23 Turos Morn",
       "31.12": "#17 Turos Zera", "28.10": "#16 Collapsed Elven Keep", "20.10": "#14 Ruined Wizard's Tower",
       "31.17": "#31 Ruined Monastery"}
forts = {"22.20": "Legate Ulrand Valerian", "25.19": "Legate Nicus Balens", "28.16": "Legate Süromus Drakon",
         "23.10": "Palatine Valanna Telpirion", "18.05": "Prefect Basilio", "20.23": "Legate Victir Syrenictor",
         "15.13": "Legate Caros Lubbo", "24.02": "Legate Zeodarë Cellëppes", "29.06": "Legate of Luseatum",
         "30.14": "Legate Darbellus Opiternian", "31.12": "Legate of Türos Zera"}
def ax(h):
    c, r = map(int, h.split(".")); return c, r - (c + (c & 1)) // 2
def dist(a, b):
    (q1, r1), (q2, r2) = ax(a), ax(b); return max(abs(q1 - q2), abs(r1 - r2), abs((q1 + r1) - (q2 + r2)))
C = json.load(open(CLS))
rows = list(csv.DictReader(open("Data/hexes.csv")))
have = {r["hex"]: r for r in rows}
for h in ("17.08", "18.08"):                       # lake hexes first built as shore grass (if built)
    if h in have and h not in C:
        have[h].update(terrain="lake", lake="yes", domain_ruler="")
if "16.07" in have and "16.07" not in C:
    have["16.07"]["river"] = "Mirmen"
have["20.23"]["domain_ruler"] = "Legate Victir Syrenictor"
for h, v in C.items():
    t = "forest" if h in forest else "swamp" if h in swamp else "lake" if h in lake else "hills" if h in hills else "grass"
    dom = "" if (v["cls"] == "wilderness" or t == "lake") else forts[min(forts, key=lambda f: dist(h, f))]
    rows.append({"hex": h, "terrain": t, "zone": v["zone"], "river": river.get(h, ""), "domain_ruler": dom, "domain_kind": "",
                 "classification": v["cls"], "land_revenue_gp": "", "point_of_interest": poi.get(h, ""), "encounters": "",
                 "lake": "yes" if t == "lake" else ""})
rows.sort(key=lambda r: (int(r["hex"][:2]), int(r["hex"][3:])))
out = io.StringIO(); w = csv.DictWriter(out, fieldnames=list(rows[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(rows)
open("Data/hexes.csv", "w").write(out.getvalue())
print(len(rows))
