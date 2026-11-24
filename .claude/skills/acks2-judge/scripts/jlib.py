"""Shared helpers for the Judge scripts: repo root, campaign.yaml, front matter."""
import os, re, sys
import yaml

_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)     # libyaml when installed (engine 7.22, H2): same YAML


def _load(text):
    return yaml.load(text, Loader=_LOADER)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("JUDGE_REPO") or os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))


def path(rel):
    return rel if os.path.isabs(rel) else os.path.join(ROOT, rel)


def config():
    with open(path("Campaign/campaign.yaml"), encoding="utf-8") as f:
        return _load(f)


FM = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


def read_note(rel):
    """Return (front matter dict, body text) of a markdown note."""
    with open(path(rel), encoding="utf-8") as f:
        text = f.read()
    m = FM.match(text)
    if not m:
        return {}, text
    return (_load(m.group(1)) or {}), text[m.end():]


def write_note(rel, fm, body):
    text = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000) + "---\n" + body
    with open(path(rel), "w", encoding="utf-8") as f:
        f.write(text)


def section(body, heading):
    """Lines of a '## heading' section (to the next heading of the same or higher level)."""
    lines, out, lev = body.splitlines(), None, None
    for ln in lines:
        m = re.match(r"^(#+)\s+(.*)$", ln)
        if out is None:
            if m and m.group(2).strip().lower() == heading.lstrip("#").strip().lower():
                out, lev = [], len(m.group(1))
            continue
        if m and len(m.group(1)) <= lev:
            break
        out.append(ln)
    return out or []


def table_rows(lines):
    """Parse a markdown table into a list of dicts (header -> cell)."""
    rows = [l for l in lines if l.strip().startswith("|")]
    if len(rows) < 2:
        return []
    split = lambda l: [c.strip() for c in re.split(r"(?<!\\)\|", l.strip())[1:-1]]
    head = split(rows[0])
    return [dict(zip(head, split(r))) for r in rows[2:]]


def die(msg, code=1):
    print("error: " + msg, file=sys.stderr)
    sys.exit(code)


# ---------------------------------------------------------------- actors (engine 7.x, acks-actor/1)
ACTOR_DIRS = ["Characters/", "Characters/former/", "Campaign/candidates/", "Actors/npc/", "Actors/monsters/"]


def actor_dirs(cfg):
    """The campaign's actor folders (config paths.actors; D14): absolute paths, in order."""
    return [path(d.rstrip("/")) for d in ((cfg.get("paths") or {}).get("actors") or ACTOR_DIRS)]


def actor_files(folder):
    """The actor files directly in `folder` (relative to the repo): <folder>/<id>.json, sorted."""
    import glob as _g
    return sorted(_g.glob(os.path.join(path(folder), "*.json")))


def actor_id(ref):
    """The actor id named by an id or by a file path (Characters/<id>.json)."""
    return os.path.splitext(os.path.basename(str(ref)))[0] if ref else ""


def load_actor(p):
    import json as _j
    with open(path(p), encoding="utf-8") as f:
        return _j.load(f)


def actor_views(ids, player=True, fields=None):
    """Prepared views {id: view} from the engine (`acks actor show ID... --json`, through acks.sh so the campaign's
    actor folders, inventory, adventure ledger and aliases apply). --player drops the judge block (D8)."""
    import json as _j, subprocess as _s
    ids = [i for i in ids if i]
    if not ids:
        return {}
    cmd = ["bash", os.path.join(HERE, "acks.sh"), "actor", "show", *ids, "--json"]
    if player:
        cmd.append("--player")
    if fields:
        cmd += ["--fields", ",".join(fields)]
    r = _s.run(cmd, capture_output=True, text=True, timeout=120)
    try:
        d = _j.loads(r.stdout)
    except ValueError:
        raise RuntimeError(f"acks actor show {' '.join(ids)}: {(r.stdout + r.stderr).strip()[-400:]}")
    if not d.get("ok", True) or "data" not in d:
        raise RuntimeError(f"acks actor show {' '.join(ids)}: {d.get('line') or d}")
    data = d["data"]
    return data["views"] if "views" in data else {ids[0]: data["view"]}
