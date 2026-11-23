#!/usr/bin/env python3
"""snapshot.py [--check]  : write the player-facing display snapshot (campaign.yaml paths.state.snapshot).
Inputs and their whitelists:
  Campaign State front matter `public:`  -> every key must be in PUBLIC (recursively), else refuse
  actors in paths.characters             -> the engine's prepared player view (`acks actor show ID... --player`, D8: no
                                            judge block), cut to the whitelist of the actor's type: SHEET for a
                                            character (the keys the markdown sheets had, so the VTT page is unchanged),
                                            MONSTER for a monster actor; other keys are not published. Engine
                                            unavailable: the characters of the last snapshot are kept
  World State "## Explored hexes" table   -> Hex and Terrain columns only
  roll log                               -> this session's open rolls only (latest 50)
  rumours note, "heard by the party"     -> its bullet lines
Then the output is scanned for Judge-only note titles (campaign.yaml secrecy) and markers, and for the keys "loyalty",
"retinue_id" and "judge" (engine stage 3: loyalty scores and sheets' Judge blocks); any hit -> refuse.
Nothing is written on refusal (exit 2). --check validates without writing.
--payload prints the display db document for the written snapshot (campaign.yaml display:), compact JSON:
{"schema": 1, "written_at": ..., "snapshot": {...}}; the Judge passes it to db_write as the "set" op's data."""
import glob, json, os, re, sys, time
sys.path.insert(0, os.path.dirname(__file__))
import jlib

ANY = object()
L = lambda x: ("list", x)
PUBLIC = {
    "date": {"year": ANY, "season": ANY, "day": ANY},
    "time": ANY, "weather": ANY, "place": ANY, "hex": ANY,
    "party": L({"name": ANY, "sheet": ANY, "role": ANY, "hp": ANY, "hp_max": ANY, "conditions": L(ANY),
                "spells_used": L(ANY), "encumbrance_st": ANY, "status": ANY}),
    "light": ANY, "rations": ANY,
    "tracker": {"round": ANY, "order": L({"name": ANY, "init": ANY}), "engaged": L(L(ANY)),
                "distances": L({"between": L(ANY), "feet": ANY}), "cover": L(ANY), "formation": L(ANY),
                "light": ANY, "note": ANY},
    "threads": L(ANY),
    "trail": L(ANY),
}
ROLL_CAP = 50   # the snapshot keeps the latest open rolls of the session only
SHEET = {k: ANY for k in (
    "type role name title class occupation level xp xp_next xp_bonus alignment birthplace age gender size hit_die "
    "hp_max attributes ac attack_throw attack_table initiative surprise avoid_surprise saves save_mods movement "
    "encumbrance_st healing_rate mortal_wounds cleaves proficiency_throws weapons proficiencies class_features "
    "languages coins gems gear spells hired treasure "
    "sheet chargen").split()}   # treasure: player records of carried lots (engine stage 5); sheet: class sheet
    # profile at the actor's level (S3); chargen: the draft actor's creation-in-progress block (S4a)
MONSTER = {"name"}   # a monster actor among the characters (a monstrous henchman): its name only; type is set to monster


class Refuse(Exception):
    pass


def check(v, schema, where):
    if schema is ANY:
        return
    if isinstance(schema, tuple):
        if v in (None, ""):
            return
        if not isinstance(v, list):
            raise Refuse(f"{where}: expected a list")
        for i, x in enumerate(v):
            check(x, schema[1], f"{where}[{i}]")
        return
    if v in (None, "", {}):
        return
    if not isinstance(v, dict):
        raise Refuse(f"{where}: expected a mapping")
    for k, x in v.items():
        if k not in schema:
            raise Refuse(f"{where}.{k} is not on the whitelist")
        check(x, schema[k], f"{where}.{k}")


def characters(cfg):
    """The characters as players see them: each actor's prepared player view, cut to its type's whitelist."""
    kinds = {}
    for f in jlib.actor_files(cfg["paths"]["characters"]):
        a = jlib.load_actor(f)
        if jlib.actor_id(f) != a.get("id"):
            raise Refuse(f"{os.path.relpath(f, jlib.ROOT)}: its id {a.get('id')!r} is not its file name")
        kinds[a["id"]] = a.get("type")
    try:
        views = jlib.actor_views(list(kinds), player=True)
    except RuntimeError as e:
        try:
            old = json.load(open(jlib.path(cfg["paths"]["state"]["snapshot"]), encoding="utf-8")).get("characters") or []
        except (OSError, ValueError):
            old = []
        print(f"snapshot: engine unavailable, characters of the last snapshot kept ({e})", file=sys.stderr)
        return old
    out = []
    for aid, kind in kinds.items():
        v = views[aid]
        if kind == "character":
            out.append({k: x for k, x in v.items() if k in SHEET})
        else:
            out.append({"type": "monster", **{k: x for k, x in v.items() if k in MONSTER}})
    return out


def build(cfg):
    st = cfg["paths"]["state"]
    fm, _ = jlib.read_note(st["campaign_state"])
    pub = fm.get("public") or {}
    check(pub, PUBLIC, "public")
    sheets = characters(cfg)
    _, wbody = jlib.read_note(st["world_state"])
    hexes = [{"hex": r.get("Hex", ""), "terrain": r.get("Terrain", "")}
             for r in jlib.table_rows(jlib.section(wbody, "Explored hexes")) if r.get("Hex")]
    rolls = []
    try:
        for line in open(jlib.path(st["roll_log"]), encoding="utf-8"):
            r = json.loads(line)
            if r["vis"] == "open" and r["session"] == fm.get("session"):
                rolls.append({"label": r["label"], "spec": r["spec"], "rolls": r["rolls"], "total": r["total"]})
    except FileNotFoundError:
        pass
    rn = cfg["logs"]["rumours"]
    _, rbody = jlib.read_note(rn["note"])
    rumours = [l.strip()[2:].strip() for l in jlib.section(rbody, rn["section"]) if l.strip().startswith(("- ", "* "))]
    return {"campaign": cfg["campaign"]["name"], "session": fm.get("session"), "generated": int(time.time()),
            **{k: pub.get(k) for k in PUBLIC}, "explored_hexes": hexes, "characters": sheets,
            "open_rolls": rolls[-ROLL_CAP:], "rumours_heard": rumours}


def wall(cfg, text):
    sec = cfg["secrecy"]; banned = []
    for folder in sec["judge_only_folders"]:
        if folder.startswith("Campaign"):
            continue
        banned += [os.path.basename(p)[:-3] for p in glob.glob(jlib.path(folder) + "/*.md")]
    banned = [b for b in banned if b not in sec.get("revealed", [])]
    banned += [sec["judge_only_tag"], "[!danger]", "Judge only", "[H] "]
    banned += ['"loyalty"', '"retinue_id"', '"judge"']   # stage 3: loyalty scores and the sheets' Judge blocks never published
    hits = [b for b in banned if b.lower() in text.lower()]
    if hits:
        raise Refuse("Judge-only text in output: " + ", ".join(hits))
    # stage 5: an item's true identity and the Judge-only fields of a lot never reach the players before it is identified
    ap = jlib.path(cfg.get("tools", {}).get("adventure_state", "Campaign/adventure-state.json"))
    if os.path.exists(ap):
        adv = json.load(open(ap, encoding="utf-8")) or {}
        lots = list((adv.get("lots") or {}).values())
        # Names the players already know are no leak: the true name of an identified lot (a second "Sword +1" still
        # unidentified shares it), every lot's player description, and the note names of identified lots. They are
        # taken out of the text before it is searched, longest first ("Short Sword +1" holds "Sword +1") (S15, S18, S19).
        known = set()
        for l in lots:
            t, p = l.get("true") or {}, l.get("player") or {}
            if p.get("desc"):
                known.add(str(p["desc"]).lower())
            if l.get("identified"):
                if t.get("name"):
                    known.add(str(t["name"]).lower())
                if t.get("note"):
                    known.add(os.path.basename(t["note"])[:-3].lower())
        low = text.lower()
        for k in sorted(known, key=len, reverse=True):
            low = low.replace(k, " ")
        for l in lots:
            t, p = l.get("true") or {}, l.get("player") or {}
            nm = t.get("name") or ""
            if l.get("kind") == "item" and not l.get("identified") and nm and nm != p.get("desc") and nm.lower() in low:
                raise Refuse(f"unidentified item {l['id']}'s true name is in the output")
            if t.get("note") and not l.get("identified") and os.path.basename(t["note"])[:-3].lower() in low:
                raise Refuse(f"unidentified item {l['id']}'s vault note name is in the output")
        for k in ('"rarity"', '"base_gp"', '"base_cost_text"', '"subtable"', '"true"'):
            if k in text:
                raise Refuse(f"Judge-only treasure field {k} in output")
    # stage 4: while the party is lost, its true hex never reaches the players (only the hex it believes it is in)
    xp = jlib.path(cfg.get("tools", {}).get("exploration_state", "Campaign/exploration-state.json"))
    if os.path.exists(xp):
        tr = (json.load(open(xp, encoding="utf-8")) or {}).get("travel") or {}
        true = tr.get("hex")
        if tr.get("lost") and true and true != tr.get("believed"):
            snap = json.loads(text)
            if snap.get("hex") == true:
                raise Refuse(f"public.hex is the lost party's true hex {true} (it must be the believed hex {tr.get('believed')})")
            trail = snap.get("trail") or []
            believed_trail = tr.get("trail") or []
            if trail and trail != believed_trail[-len(trail):]:
                raise Refuse("public.trail is not the believed trail of the lost party (xsync writes it from the engine)")
            # elsewhere the true hex may appear only as a hex the party knowingly passed through before
            if true not in believed_trail:
                rest = dict(snap, trail=None)
                if f'"{true}"' in json.dumps(rest, ensure_ascii=False, default=str):
                    raise Refuse(f"the lost party's true hex {true} is in the output")


def overlay_pairs(cfg):
    """Return [(rulebook, kardakia), ...] from Campaign/class-overlays.yaml, longest rulebook first.
    An empty list if the file is absent (overlay not configured yet) or unreadable."""
    import yaml
    rel = (cfg.get("tools") or {}).get("overlay") or "Campaign/class-overlays.yaml"
    try:
        with open(jlib.path(rel), encoding="utf-8") as f:
            ov = yaml.safe_load(f) or {}
    except (OSError, ValueError):
        return []
    out = []
    for t in ov.get("terms") or []:
        rb, kv = (t.get("rulebook") or "").strip(), (t.get("kardakia") or "").strip()
        if rb and kv and rb != kv:
            out.append((rb, kv))
    out.sort(key=lambda p: -len(p[0]))
    return out


def apply_overlay(obj, pairs):
    """Apply (rulebook -> kardakia) to every string value, in-place. Longest first, whole words,
    case as written (both forms). Dict keys are not rewritten — they are the whitelist's field names."""
    if not pairs:
        return obj
    def sub(s):
        for rb, kv in pairs:
            s = re.sub(rf"(?<!\w){re.escape(rb)}(?!\w)", kv, s)
        return s
    def walk(x):
        if isinstance(x, str):
            return sub(x)
        if isinstance(x, list):
            return [walk(v) for v in x]
        if isinstance(x, dict):
            return {k: walk(v) for k, v in x.items()}
        return x
    return walk(obj)


cfg = jlib.config()
try:
    snap = build(cfg)
    # requests_done: forward-compatible (engine S6); keep an empty list when the engine does not supply one
    snap.setdefault("requests_done", [])
    snap = apply_overlay(snap, overlay_pairs(cfg))
    text = json.dumps(snap, ensure_ascii=False, indent=1, default=str)
    wall(cfg, text)
except Refuse as e:
    print("snapshot REFUSED: " + str(e), file=sys.stderr); sys.exit(2)
if "--payload" in sys.argv:   # the snapshot already written by the last run, exactly as committed
    disp = cfg.get("display") or {}
    written = json.load(open(jlib.path(cfg["paths"]["state"]["snapshot"]), encoding="utf-8"))
    print(json.dumps({"schema": disp.get("schema", 1), "written_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(written["generated"])),
                      "snapshot": written}, ensure_ascii=False, separators=(",", ":")))
    sys.exit(0)
if "--check" in sys.argv:
    print("snapshot ok (not written)"); sys.exit(0)
with open(jlib.path(cfg["paths"]["state"]["snapshot"]), "w", encoding="utf-8") as f:
    f.write(text + "\n")
print(f"snapshot written: {len(snap['characters'])} characters, {len(snap['open_rolls'])} open rolls, {len(snap['explored_hexes'])} hexes")
