#!/usr/bin/env python3
"""build_site.py SPEC.yaml [--dry-run] : the unprepped-site steps as a script (7.25.0 proposals, C4).

Refuses to start while Campaign State's `session:` is stale (the S16 build's rolls landed under session 15). From a
small spec it rolls, through the engine (hidden, labelled "Site build: NAME ..."):
  - each population entry's number (its dice, or the note's lair number with `number: lair`) and each creature's hp
    (the statblock's Hit Dice; a leader's from the bestiary's leader table or ecology line, `leader: chieftain`);
  - each room's treasure (`treasure: {W6: G}`: the Treasure Type rolled by `treasure --type`);
and writes, in `folder`: the hub note (front matter, Running section, the `## Route graph` from the rooms' links,
the population), a skeleton note per room (its population with hp, its treasure, its links), the wandering table
from the population (acks-table/1; one row per kind, weighted by count), the roster (`roster add` into the
exploration state, so encounters draw from it), and a Rulings row naming the build. Every [[link]] written is
checked to resolve. Spec:

    site: Troglodyte Warren
    folder: Adventure/Troglodyte Warren
    level: 3
    wandering: "1d6 every 2 turns, 6+"
    rooms:
      W1: {name: The Crack, links: {W2: 60}}
      W2: {name: The Long Slope, links: {W3: 250}}
      W3: {name: Guard Cave, links: {W4: 40, W6: 150}, stop: true}
    population:
      - {monster: Troglodyte, number: 2d4, where: W3}
      - {monster: Troglodyte, leader: chieftain, where: W6}
    treasure: {W6: G}
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jacks  # noqa: E402
import jlib  # noqa: E402


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def rolled(out):
    m = re.findall(r"=\s*(-?\d+)\s*$", out.strip().splitlines()[-1]) or re.findall(r"=\s*(-?\d+)", out)
    return int(m[-1]) if m else None


def links_resolve(text):
    names = set(re.findall(r"\[\[([^\]|#]+)", text))
    have = set()
    for d, _s, fs in os.walk(jlib.ROOT):
        if "/.git" in d:
            continue
        have |= {f[:-3] for f in fs if f.endswith(".md")}
    try:
        from acks import monsters as M
        for n in list(names - have):
            try:
                M.find_note(n)
                have.add(n)
            except Exception:  # noqa: BLE001
                pass
    except ImportError:
        pass
    return sorted(names - have)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--dry-run", action="store_true", help="check the spec and the session; roll and write nothing")
    a = ap.parse_args(argv)
    import yaml
    spec = yaml.safe_load(open(a.spec, encoding="utf-8"))
    ctx = jacks.context()
    stale = jacks.stale_session(ctx)
    if stale:
        print("NOT STARTED: " + stale)
        return 2
    site, folder = spec["site"], spec.get("folder") or f"Adventure/{spec['site']}"
    rooms = spec.get("rooms") or {}
    for r, rec in rooms.items():
        for to in (rec.get("links") or {}):
            if to not in rooms:
                print(f"NOT STARTED: room {r} links to {to}, which is not in rooms")
                return 2
    for p in spec.get("population") or []:
        if p.get("where") not in rooms:
            print(f"NOT STARTED: population {p.get('monster')} in {p.get('where')}, not a room")
            return 2
    if a.dry_run:
        print(f"spec ok: {site}: {len(rooms)} rooms, {len(spec.get('population') or [])} population entries; "
              f"session {ctx['session']}")
        return 0
    from acks import monsters as M
    from acks import data as D
    jacks._apply_env(jacks.env_for(ctx, "state", []))
    tag = f"Site build: {site}"
    pop = {}
    roster_cmds = []
    for p in spec.get("population") or []:
        name, where = p["monster"], p["where"]
        note = M.find_note(name, ctx["bestiary"])
        sb = M.load(name, ctx["bestiary"])
        lead = None
        if p.get("leader"):
            lead = M.leader_row(note, p["leader"])
            n = 1
        elif str(p.get("number", 1)).lower() == "lair":
            spec_n = (M.statblocks(note)[0][0] or {}).get("dungeon_enc") or "1"
            m = re.search(r"Lair\s*\((\d*d\d+[^)]*)\)", str(spec_n)) or re.search(r"(\d*d\d+)", str(spec_n))
            code, out = jacks.run(["roll", f"{tag}: {name} in {where} (number):{m.group(1) if m else '1d6'}",
                                   "--hidden"], ctx)
            n = rolled(out) or 1
        elif re.search(r"d\d", str(p.get("number", ""))):
            code, out = jacks.run(["roll", f"{tag}: {name} in {where} (number):{p['number']}", "--hidden"], ctx)
            n = rolled(out) or 1
        else:
            n = int(p.get("number", 1))
        hps = []
        if lead and lead.get("hp"):
            hps = [int(lead["hp"])]
        else:
            hd = D.hd_parse(str(p["hd"])) if p.get("hd") else (sb.get("hd") if isinstance(sb.get("hd"), dict)
                                                                 else D.hd_parse(str(sb.get("hd") or "1")))
            dice = int(hd.get("dice") or 1)
            bonus = int(hd.get("bonus") or 0)
            for i in range(n):
                code, out = jacks.run(["roll", f"{tag}: {name} {i + 1} in {where} hp:{dice}d8"
                                       + (f"{bonus:+d}" if bonus else ""), "--hidden"], ctx)
                hps.append(max(1, rolled(out) or dice * 4))
        pop.setdefault(where, []).append({"monster": name, "n": n, "hp": hps, "leader": p.get("leader")})
        roster_cmds.append(["roster", "add", "--site", site, "--monster", name, "--count", str(n), "--hp",
                            ",".join(map(str, hps)), "--where", where]
                           + (["--prefix", slug(f"{p['leader']}")] if p.get("leader") else []))
    treasure = {}
    for r, tt in (spec.get("treasure") or {}).items():
        code, out = jacks.run(["treasure", "--type", str(tt)], ctx)
        treasure[r] = jacks_text(out)
    os.makedirs(jlib.path(folder), exist_ok=True)
    graph = []
    done = set()
    for r, rec in rooms.items():
        for to, ft in (rec.get("links") or {}).items():
            if (to, r) not in done:
                graph.append(f"- {r} - {to}: {ft}")
                done.add((r, to))
    stops = [r for r, rec in rooms.items() if rec.get("stop") or pop.get(r)]
    if stops:
        graph.append(f"- stop: {', '.join(stops)}")
    kinds = {}
    for r, ps in pop.items():
        for p in ps:
            kinds[p["monster"]] = kinds.get(p["monster"], 0) + p["n"]
    table_path = os.path.join(folder, f"{slug(site)}-wandering.yaml")
    tot = sum(kinds.values()) or 1
    rows, lo = [], 1
    order = sorted(kinds.items(), key=lambda x: -x[1])
    for j, (k, c) in enumerate(order):
        if lo > 6:
            break
        hi = 6 if j == len(order) - 1 else min(6, lo + max(1, round(6 * c / tot)) - 1)
        rows.append((f"{lo}-{hi}" if hi > lo else f"{lo}", f"[[{k}]] (1d4)"))
        lo = hi + 1
    with open(jlib.path(table_path), "w", encoding="utf-8") as f:
        f.write(f"schema: acks-table/1\nid: {slug(site)}-wandering\ntitle: Wandering Monster Table - {site}\n"
                f"source: {{campaign: true, book: \"build_site.py (session {ctx['session']})\", printed_pages: []}}\n"
                f"columns: [\"1d6\", \"Monster\"]\nrows:\n" + "\n".join(f'  - ["{r}", "{m}"]' for r, m in rows) + "\n")
    hub = [f"---\ntype: site\ntags:\n  - {(ctx['cfg'].get('secrecy') or {}).get('judge_only_tag', 'secret')}\n"
           f"dungeon_level: {spec.get('level', 1)}\nprepped_by: build_site.py\n---\n# {site}\n",
           f"Judge only. Built by build_site.py in session {ctx['session']}; its rolls are labelled \"{tag}\".\n",
           f"## Running {site}\n- Dungeon level: {spec.get('level', 1)}\n- Wandering monsters: "
           f"{spec.get('wandering', '1d6 every 2 turns, 6+')}\n- Encounter table: {os.path.basename(table_path)}\n"
           f"- Wanderers come from the roster (`roster show --site \"{site}\"`).\n",
           "## Rooms\n" + "\n".join(f"- [[{site} {r} {rec.get('name', r)}]]" for r, rec in rooms.items()) + "\n",
           "## Route graph\n" + "\n".join(graph) + "\n"]
    hub_rel = os.path.join(folder, f"{site}.md")
    with open(jlib.path(hub_rel), "w", encoding="utf-8") as f:
        f.write("\n".join(hub))
    for r, rec in rooms.items():
        body = [f"---\ntype: room\nsite: \"[[{site}]]\"\nroom: {r}\n---\n# {r} {rec.get('name', r)}\n",
                rec.get("text", "(description: the Judge writes it)") + "\n", "## Population"]
        for p in pop.get(r, []):
            body.append(f"- [[{p['monster']}]] x{p['n']}" + (f" ({p['leader']})" if p.get("leader") else "")
                        + f": hp {', '.join(map(str, p['hp']))}")
        if not pop.get(r):
            body.append("- none")
        body.append("\n## Treasure\n" + (treasure.get(r) or "- none"))
        body.append("\n## Ways\n" + "\n".join(f"- {to}: {ft}'" for to, ft in (rec.get("links") or {}).items()))
        with open(jlib.path(os.path.join(folder, f"{site} {r} {rec.get('name', r)}.md")), "w", encoding="utf-8") as f:
            f.write("\n".join(body) + "\n")
    for c in roster_cmds:
        code, out = jacks.run(c, ctx)
        if code:
            print(f"roster: {out.strip()[:200]}")
    rp = jlib.path("Campaign/Rulings.md")
    if os.path.exists(rp):
        import datetime
        with open(rp, "a", encoding="utf-8") as f:
            f.write(f"| {datetime.date.today().isoformat()} | S{ctx['session']} | {site}: how was it stocked? | Built "
                    f"by build_site.py (the unprepped-site steps): population, hp and treasure rolled hidden as "
                    f"\"{tag}\"; the roster drives its encounters | Judge's procedure (JJ ch. 8, interim) |\n")
    bad = []
    for d, _s, fs in os.walk(jlib.path(folder)):
        for f in fs:
            if f.endswith(".md"):
                bad += links_resolve(open(os.path.join(d, f), encoding="utf-8").read())
    print(f"built {site}: hub {hub_rel}, {len(rooms)} room notes, table {table_path}, roster of "
          f"{sum(kinds.values())}")
    if bad:
        print("UNRESOLVED LINKS: " + ", ".join(sorted(set(bad))))
        return 3
    return 0


def jacks_text(out):
    return "\n".join("- " + x.strip() for x in re.sub(r" *\(src:[^)]*\)", "", out).split(" | ")
                     if x.strip() and not x.strip().startswith(("NOTE", "REMINDER")))[:2000]


if __name__ == "__main__":
    sys.exit(main())
