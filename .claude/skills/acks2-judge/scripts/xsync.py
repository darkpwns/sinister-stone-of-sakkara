#!/usr/bin/env python3
"""xsync.py [--party] : (1) generate Campaign State `public.party` from the actors in `paths.characters` (D7, engine
7.x): one entry per character actor (pc or henchman) with its name, file, role, current hp, conditions and spells used
(the actor's `state` block) and its hp maximum and encumbrance (the engine's prepared view, `acks actor show`). Entries
keep the order they had; new ones follow (PCs, then henchmen by hiring date). Monster actors (no state block) are not
listed. Actors that left or died are in Characters/former/ and drop out. Never edit `public.party` by hand: change the
actor (`acks.sh actor set ID state.hp N --cause ...`).
(2) copy the open exploration values (time of day, light sources with bearer and turns left, rest due) from the
engine's exploration state into Campaign State `public.time` and `public.light`, and, while travelling (engine stage
4), the day's weather, the hex the party BELIEVES it is in, its trail (believed hexes) and its supplies into
`public.weather`, `public.hex`, `public.trail` and `public.rations`, so the snapshot shows them. The true hex of a lost
party, navigation, encounter and foraging rolls are never in the engine's player view. Only the engine's player view
is used (`acks clock --player`): wandering checks, encounters and timers marked hidden never reach Campaign State.
Does nothing for (2) if there is no exploration state or the engine is unavailable.
Loyalty and morale stay in the retinue state (Judge only); nothing copies them to the actors.
save.sh runs it before the snapshot; acks.sh runs `--party` before `encounter fight` (it reads current hp from there)."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import jlib


def party(cfg):
    """public.party from the actors' state (D7). Returns True when Campaign State changed."""
    rel = cfg["paths"]["state"]["campaign_state"]
    fm, body = jlib.read_note(rel)
    pub = fm.setdefault("public", {})
    actors = {}
    for f in jlib.actor_files(cfg["paths"]["characters"]):
        a = jlib.load_actor(f)
        if a.get("type") == "character" and a.get("role") in ("pc", "henchman") and not a.get("chargen"):
            # S5: a draft PC (an in-progress `chargen` block) is not in public.party and not in a fight
            actors[a["id"]] = (a, os.path.relpath(f, jlib.ROOT))
    views = jlib.actor_views(list(actors), fields=["name", "hp_max", "encumbrance_st"]) if actors else {}
    old = [jlib.actor_id(m.get("sheet")) for m in pub.get("party") or [] if isinstance(m, dict)]
    rest = sorted((i for i in actors if i not in old),
                  key=lambda i: (actors[i][0]["role"] != "pc", str((actors[i][0].get("hired") or {}).get("date") or ""),
                                 actors[i][0]["name"]))
    out = []
    for i in [i for i in old if i in actors] + rest:
        a, path = actors[i]
        v, st = views.get(i) or {}, a.get("state") or {}
        e = {"name": a["name"], "sheet": path, "role": a["role"], "hp": st.get("hp", a.get("hp_max")),
             "hp_max": v.get("hp_max", a.get("hp_max")), "conditions": list(st.get("conditions") or []),
             "spells_used": list(st.get("spells_used") or [])}
        if v.get("encumbrance_st") is not None:
            e["encumbrance_st"] = v["encumbrance_st"]
        out.append(e)
    if pub.get("party") != out:
        pub["party"] = out
        jlib.write_note(rel, fm, body)
        print("xsync: public.party " + ("; ".join(f"{e['name']} {e['hp']}/{e['hp_max']}" for e in out) or "empty"))
        return True
    return False


cfg = jlib.config()
try:
    party(cfg)
except RuntimeError as e:   # engine unavailable: public.party stays as it was
    print(f"xsync: public.party not generated ({e})", file=sys.stderr)
if "--party" in sys.argv:
    sys.exit(0)
xp = jlib.path(cfg.get("tools", {}).get("exploration_state", "Campaign/exploration-state.json"))
if not os.path.exists(xp):
    sys.exit(0)
try:
    out = subprocess.run(["bash", os.path.join(os.path.dirname(os.path.abspath(__file__)), "acks.sh"), "clock", "--player",
                          "--json"], capture_output=True, text=True, timeout=60)   # acks.sh: the actor folders too
    view = json.loads(out.stdout)["data"]
except Exception as e:  # engine unavailable: leave Campaign State as the Judge wrote it
    print(f"xsync: skipped ({e})", file=sys.stderr)
    sys.exit(0)
rel = cfg["paths"]["state"]["campaign_state"]
fm, body = jlib.read_note(rel)
pub = fm.setdefault("public", {})
hhmm = view["time"].split()[-1]
lights = [f"{x['kind']} ({x['bearer'] or 'set down'}) {x['time_left']} left" if x["lit"]
          else f"{x['kind']} ({x['bearer'] or 'set down'}) out" for x in view["light"]]
light = "; ".join(lights) if lights else "none"
if view.get("winded"):
    light += " | winded: " + ", ".join(view["winded"])
want = {"time": hhmm, "light": light}
# the date follows the engine clock: days the clock advanced since the last sync are added to public.date.day
# (front matter `clock_day` remembers the clock's day; a season or year rollover stays the Judge's)
import re as _re
_m = _re.search(r"day (\d+)", view.get("time") or "")
if _m:
    cday = int(_m.group(1))
    last = fm.get("clock_day")
    if last is None:
        fm["clock_day"] = cday
        want["_clock_new"] = True
    elif cday != last and isinstance(pub.get("date"), dict) and str(pub["date"].get("day", "")).isdigit():
        d = dict(pub["date"]); d["day"] = int(d["day"]) + (cday - int(last))
        want["date"] = d
        fm["clock_day"] = cday
tv = view.get("travel") or {}
# the season follows the engine's calendar (engine 7.13.4: the travel block's season turns every 3 months from its
# season start); the year stays the Judge's
try:
    _xs = json.load(open(jlib.path(cfg["tools"]["exploration_state"]), encoding="utf-8"))
    _sn = ((_xs.get("travel") or {}).get("season") if (_xs.get("travel") or {}).get("season_start") else None)
except Exception:
    _sn = None
if _sn and isinstance(pub.get("date"), dict) and pub["date"].get("season") != _sn:
    d = dict(want.get("date") or pub["date"]); d["season"] = _sn
    want["date"] = d
if tv:
    want["hex"] = tv["hex"]
    want["trail"] = list(tv.get("trail") or [])[-20:]
    if tv.get("weather"):
        w = tv["weather"]
        want["weather"] = w["text"] + (f" ({', '.join(w['conditions'])})" if w.get("conditions") else "")
    sup = tv.get("supplies") or {}
    want["rations"] = "; ".join(
        f"{k}: food {v['food_days']:g} d, water {v['water_days']:g} d" + (f", firewood {v['firewood_st']:g} st" if v.get("firewood_st") else "")
        + (f" ({', '.join(v['conditions'])})" if v.get("conditions") else "")
        if "food_days" in v else f"{k}: fodder {v['fodder_st']:g} st, water {v['water_st']:g} st"
        for k, v in sup.items())
    if tv.get("lost"):
        want["hex"] = tv["hex"]          # the believed hex; the party knows it is lost
changed = any(pub.get(k) != v for k, v in want.items())
want.pop("_clock_new", None)
pub.update(want)
if changed:
    jlib.write_note(rel, fm, body)
    print("xsync: " + "; ".join(f"{k} {v}" for k, v in want.items() if k != "trail"))
