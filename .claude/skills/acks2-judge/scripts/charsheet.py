#!/usr/bin/env python3
"""charsheet.py pdf2actor PDF ID [--role pc|henchman] [--force] : read the fillable PDF's fields into an actor
   Characters/<ID>.json (through the engine's importer: every number the PDF records differently from the rules becomes
   a modifier with source import, and the import's notes list them; gear, coins and weapons stay in the actor's
   possessions block until `inv holder add ID --opening --discard-sheet-gear` moves them into the inventory)
   charsheet.py import FILE ID [--role pc|henchman] [--force] : the same from a sheet-shaped YAML (or markdown front
   matter) file the Judge wrote (the keys `acks actor show` prints), e.g. an AI player's PC built from his choices
   charsheet.py actor2pdf ID OUT.pdf : fill a fresh copy of the template from the actor's prepared player view
   (`acks actor show`), current hp from its state, page 5 from up to six of its henchmen (hiring order)
   charsheet.py fields PDF           : list filled fields the map does not cover
The field map is data/pdf-field-map.yaml (single source)."""
import os, re, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(__file__))
import jlib, yaml
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject

HERE = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(HERE, "..", "data", "pdf-field-map.yaml")


def load_map():
    rows = yaml.safe_load(open(MAP, encoding="utf-8"))["fields"]
    out = []
    for f, k, t in rows:
        if "{h}" in f:
            out += [(f.replace("{h}", f"{h // 3}.{h % 3}"), k.replace("@henchman", f"@henchman[{h}]"), t) for h in range(6)]
        elif "{l}{s}" in f:
            out += [(f.replace("{l}{s}", f"{l}{s}"), k.replace("{l}", str(l)).replace("{s}", str(s - 1)), t)
                    for l in range(1, 7) for s in range(1, 9)]
        elif "{s}" in f:
            out += [(f.replace("{s}", str(s)), k.replace("{s}", str(s - 1)), t) for s in range(1, 9)]
        elif "{i}" in f:
            n = 7 if f.startswith(("Weapon", "Wpn")) else 10
            out += [(f.replace("{i}", str(i)), k.replace("{i}", str(i)), t) for i in range(n)]
        else:
            out.append((f, k, t))
    return out


def steps(key):
    return [int(p) if p.isdigit() else p for p in re.findall(r"[^.\[\]]+", key)]


def put(d, key, v):
    s = steps(key)
    for a, b in zip(s, s[1:]):
        if isinstance(a, int):
            while len(d) <= a: d.append({} if not isinstance(b, int) else [])
            d = d[a]
        else:
            d = d.setdefault(a, [] if isinstance(b, int) else {})
    last = s[-1]
    if isinstance(last, int):
        while len(d) <= last: d.append(None)
        d[last] = v
    else:
        d[last] = v


def get(d, key):
    for p in steps(key):
        try:
            d = d[p]
        except (KeyError, IndexError, TypeError):
            return None
    return d


def parse(v, t):
    v = str(v).strip()
    if v == "":
        return None
    if t == "lines":
        return [x.strip() for x in re.split(r"[\r\n]+", v) if x.strip()]
    if t in ("int", "mod", "bonus"):
        try:
            return int(v.replace("+", ""))
        except ValueError:
            return v
    return v


def fmt(v, t):
    if v is None or v == "":
        return ""
    if t == "lines":
        return "\r".join(v) if isinstance(v, list) else str(v)
    if t in ("mod", "bonus") and isinstance(v, int):
        return f"+{v}" if v > 0 or (v == 0 and t == "bonus") else str(v)
    return str(v)


def prune(x):
    if isinstance(x, dict):
        x = {k: prune(v) for k, v in x.items()}
        return {k: v for k, v in x.items() if v not in (None, {}, [])}
    if isinstance(x, list):
        y = [prune(v) for v in x]
        while y and y[-1] in (None, {}, []): y.pop()
        return y
    return x


def values(pdf):
    out = {}
    for k, f in (PdfReader(pdf).get_fields() or {}).items():
        v = f.get("/V")
        if v not in (None, "", "/Off"):
            out[k] = str(v)
    return out


def acks(*args):
    r = subprocess.run(["bash", os.path.join(HERE, "acks.sh"), *args], capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def day_no(h):
    m = re.search(r"\d+", str((h.get("hired") or {}).get("date") or ""))
    return int(m.group(0)) if m else 10 ** 9


a = sys.argv[1:]
if len(a) < 2:
    print(__doc__); sys.exit(1)
M = load_map()
cfg = jlib.config()
if a[0] in ("pdf2actor", "fields", "import"):
    fm = {"type": "character", "role": "pc"}
    if a[0] == "import":
        text = open(a[1], encoding="utf-8").read()
        m = jlib.FM.match(text)
        fm.update(yaml.safe_load(m.group(1) if m else text) or {})
        vals = {}
    else:
        vals = values(a[1])
    if "--role" in a: fm["role"] = a[a.index("--role") + 1]
    mapped = set()
    for f, k, t in M:
        if k.startswith("@"):
            continue
        mapped.add(f)
        if f in vals and parse(vals[f], t) is not None:
            put(fm, k, parse(vals[f], t))
    unmapped = sorted(f for f in vals if f not in mapped and f != "Hit Points")
    if a[0] == "fields":
        print("\n".join(unmapped) or "(all filled fields are mapped)"); sys.exit(0)
    if len(a) < 3 or a[2].startswith("--"):
        print(__doc__); sys.exit(1)
    aid = jlib.actor_id(a[2])
    out = os.path.join(jlib.path(cfg["paths"]["characters"]), aid + ".json")
    fm = prune(fm)
    with tempfile.TemporaryDirectory() as tmp:          # the importer reads the old sheet shape (D9); never kept
        md = os.path.join(tmp, aid + ".md")
        with open(md, "w", encoding="utf-8") as f:
            f.write("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n")
        code, text = acks("actor", "import", md, "--out", out, *(["--force"] if "--force" in a else []))
    print(text)
    if code:
        sys.exit(code)
    if a[0] == "import":
        sys.exit(0)
    print(f"{sum(1 for f, k, t in M if f in vals)} mapped fields; current hp in PDF: {vals.get('Hit Points', '-')} "
          f"(the actor starts at its hp maximum: `acks.sh actor set {aid} state.hp N --cause ...` if it differs)")
    if unmapped:
        print("filled but not mapped:", ", ".join(unmapped))
elif a[0] == "actor2pdf":
    if len(a) < 3:
        print(__doc__); sys.exit(1)
    aid = jlib.actor_id(a[1])
    me = jlib.load_actor(os.path.join(cfg["paths"]["characters"], aid + ".json"))
    hench = []
    for p in jlib.actor_files(cfg["paths"]["characters"]):
        h = jlib.load_actor(p)
        if h.get("type") == "character" and h.get("role") == "henchman" \
                and str((h.get("hired") or {}).get("employer", "")) in (me["name"], aid):
            hench.append(h)
    hench = sorted(hench, key=lambda h: (day_no(h), h["name"]))[:6]
    views = jlib.actor_views([aid] + [h["id"] for h in hench], player=True)
    src = {"@henchman": [views[h["id"]] for h in hench]}
    view = views[aid]
    data = {}
    for f, k, t in M:
        v = get(src, k) if k.startswith("@") else get(view, k)
        if v not in (None, ""):
            data[f] = fmt(v, t)
    hp = (me.get("state") or {}).get("hp")
    if hp is not None:
        data["Hit Points"] = str(hp)
    r = PdfReader(jlib.path(cfg["party"]["pc_pdf_template"])); w = PdfWriter()
    w.append(r)
    for page in w.pages:
        w.update_page_form_field_values(page, data, auto_regenerate=False)
    w._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)
    with open(a[2], "wb") as f:
        w.write(f)
    print(f"wrote {a[2]}: {len(data)} fields filled")
else:
    print(__doc__); sys.exit(1)
