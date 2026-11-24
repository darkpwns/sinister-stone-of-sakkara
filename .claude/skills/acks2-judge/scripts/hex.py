#!/usr/bin/env python3
"""hex.py HEX                 : terrain (and its ACKS type for the engine), zone, classification, river, road, domain, site,
                               climate, neighbours (the campaign's hex source; the engine reads the same table through
                               its hex adapter: campaign.yaml `hexes`)
   hex.py --dist A B           : distance in hexes
   hex.py --sites HEX N        : sites (points of interest) within N hexes, nearest first, with prep status
All columns, files and maps come from campaign.yaml (hexes:). Hex ids are CC.RR."""
import csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import jlib

cfg = jlib.config(); H = cfg["hexes"]; C = H["columns"]
rows = {r[C["hex"]]: r for r in csv.DictReader(open(jlib.path(H["csv"]), encoding="utf-8"))}


def cr(h):
    c, r = h.split("."); return int(c), int(r)


def hid(c, r):
    return f"{c:02d}.{r:02d}"


def neighbours(h):
    c, r = cr(h)
    down = H.get("offset", "even-columns-down") == "even-columns-down"
    shifted = (c % 2 == 0) if down else (c % 2 == 1)
    d = 1 if shifted else -1
    cand = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, d), (1, d)]
    return [hid(c + a, r + b) for a, b in cand if hid(c + a, r + b) in rows]


def cube(h):
    c, r = cr(h)
    if H.get("offset", "even-columns-down") == "even-columns-down":
        z = r - (c + (c & 1)) // 2
    else:
        z = r - (c - (c & 1)) // 2
    return c, z, -c - z


def dist(a, b):
    (x1, z1, y1), (x2, z2, y2) = cube(a), cube(b)
    return max(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))


def roads_at(h):
    w = json.load(open(jlib.path(H["roads"]["file"]), encoding="utf-8"))
    names = [k.replace("|", " – ") for k, path in w[H["roads"]["key"]].items() if h in path]
    nav = any(h in w[k] for k in H.get("navigable_rivers", {}).get("keys", []))
    return names, nav


def climate(h):
    rule = (H.get("climate") or {}).get("by_column")
    if not rule:
        return None
    return rule["west"] if cr(h)[0] < rule["below"] else rule["east"]


def site_note(name):
    hits = []
    for d, _, fs in os.walk(jlib.path(cfg["paths"]["wiki_folders"]["places"])):
        hits += [os.path.join(d, f) for f in fs if f == name + ".md"]
    return os.path.relpath(hits[0], jlib.ROOT) if len(hits) == 1 else None


def prep_status(note):
    if not note:
        return "no note"
    fm, body = jlib.read_note(note)
    if fm.get("prepped_by"):
        return "prepped (" + str(fm["prepped_by"]) + ")"
    if fm.get("type") in ("dungeon", "lair") or "Dungeons and Lairs" in note:
        dev = "\n".join(jlib.section(body, "Development")).strip()
        return "UNPREPPED" if (not dev or dev.startswith("*Map, key and stocking go here")) else "keyed"
    return "settlement/landmark"


_HM = {}


def engine_class(h):
    """The engine's territory classification of the hex (engine 7.18.0: a domain's hexes, classification_map, the
    'wilderness' reading), with its source; None when the engine is not installed or refuses the word."""
    try:
        if "hm" not in _HM:
            from acks import hexmap as HM
            _HM["hm"] = HM.load(jlib.path(cfg.get("tools", {}).get("hexes", "Campaign/campaign.yaml")))
        cls, ref = _HM["hm"].classify(h)
    except Exception as e:  # noqa: BLE001 - the table's own word is still shown
        return f"engine refuses: {e}"
    if not ref or str(ref.get("campaign", "")).startswith("hex table column"):
        return cls
    src = ref.get("campaign") or ref.get("given") or f"{ref.get('book', '')} {ref.get('page', '')} {ref.get('rule', '')}".strip()
    return f"{cls} ({src})"


def site_name(h):
    s = rows[h].get(C["site"], "")
    return re.sub(r"^#\d+\s+", "", s) if s else ""


def describe(h, short=False):
    r = rows[h]; t = r[C["terrain"]]; tm = H["terrain_map"].get(t, {})
    roads, nav = roads_at(h)
    site = site_name(h)
    out = {"hex": h, "terrain": t, "acks_terrain": tm.get("acks") or "impassable",
           "zone": r[C["zone"]], "classification": r[C["classification"]], "river": r[C["river"]] or None,
           "engine_classification": None if short else engine_class(h),
           "navigable_river": nav, "road": roads or None, "domain": r[C["domain"]] or None,
           "site": site or None}
    if site:
        note = site_note(site); out["site_note"] = note; out["site_status"] = prep_status(note)
    if not short:
        out["climate"] = climate(h)
        out["neighbours"] = {n: describe(n, True) for n in neighbours(h)}
    return {k: v for k, v in out.items() if v not in (None, "", False, [])}


a = sys.argv[1:]
if not a:
    print(__doc__); sys.exit(1)
if a[0] == "--dist":
    print(dist(a[1], a[2])); sys.exit(0)
if a[0] == "--sites":
    h, n = a[1], int(a[2]); res = []
    for k in rows:
        if site_name(k) and dist(h, k) <= n:
            note = site_note(site_name(k))
            res.append((dist(h, k), k, site_name(k), prep_status(note)))
    for d, k, s, st in sorted(res):
        print(f"{d}  {k}  {s}  [{st}]")
    sys.exit(0)
if a[0] not in rows:
    jlib.die("no such hex: " + a[0])
d = describe(a[0])
nb = d.pop("neighbours", {})
for k, v in d.items():
    print(f"{k}: {v}")
print("neighbours:")
for k, v in nb.items():
    extra = "".join(f", {x}" for x in [v.get("site"), "road" if v.get("road") else None, v.get("river")] if x)
    print(f"  {k}: {v['terrain']}, {v['classification']}, {v['zone']}{extra}")
