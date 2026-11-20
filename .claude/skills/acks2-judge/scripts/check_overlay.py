#!/usr/bin/env python3
"""check_overlay.py : validate Campaign/class-overlays.yaml against the term map and the reskin notes.
save.sh runs it before the snapshot. Refuses (exit 2):
  - the overlay YAML is not readable or schema != kardakia-class-overlays/1;
  - a `terms` entry's (rulebook, kardakia) pair is not in Campaign/term-map.yaml (every overlay row must be
    grounded in the term map);
  - an `inputs` entry (kardakia -> rulebook) is not in Campaign/term-map.yaml inputs;
  - a `kardakia` value matches a Judge-only note title (campaign.yaml secrecy folders), carries the Judge-only
    tag, or appears as a Judge-only secret term named inside a `> [!danger] Judge only` callout of a class note
    AND is not named outside any callout of that same note (so a planted secret word is refused, while a
    campaign-public term that is also mentioned in a Judge-only callout for engine notes is accepted).
Prints "overlay ok: <n> terms, <m> inputs" on success."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import jlib


class Refuse(Exception):
    pass


def load_yaml(rel):
    import yaml
    try:
        with open(jlib.path(rel), encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except (OSError, ValueError) as e:
        raise Refuse(f"{rel}: {e}")


def class_note_split(cfg):
    """For each class note under paths.class_notes, return (public_text_lower, judge_text_lower):
    public = everything NOT inside a `> [!danger] Judge only` callout; judge = the callout text joined."""
    import glob
    out = []
    cn = (cfg.get("paths") or {}).get("class_notes")
    if not cn or not os.path.isdir(jlib.path(cn)):
        return out
    for f in sorted(glob.glob(os.path.join(jlib.path(cn), "*.md"))):
        with open(f, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        public, judge = [], []
        i = 0
        while i < len(lines):
            if re.match(r"^\s*>\s*\[!danger\]\s*Judge only", lines[i], re.I):
                j = i
                while j < len(lines) and lines[j].lstrip().startswith(">"):
                    judge.append(lines[j])
                    j += 1
                i = j
            else:
                public.append(lines[i]); i += 1
        out.append(("\n".join(public).lower(), "\n".join(judge).lower()))
    return out


def banned_titles(cfg):
    import glob
    sec = cfg.get("secrecy") or {}
    out = []
    for folder in sec.get("judge_only_folders") or []:
        if folder.startswith("Campaign"):
            continue
        for p in glob.glob(jlib.path(folder) + "/*.md"):
            name = os.path.basename(p)[:-3]
            if name not in (sec.get("revealed") or []):
                out.append(name.lower())
    out += [(sec.get("judge_only_tag") or "").lower(),
            "[!danger]", "judge only", "[h] "]
    return [x for x in out if x]


def check(cfg):
    if not (cfg.get("tools") or {}).get("overlay"):     # a campaign without a display overlay (GotFN, module campaigns)
        print("overlay: none configured (tools.overlay)")
        sys.exit(0)
    ov = load_yaml((cfg.get("tools") or {}).get("overlay") or "Campaign/class-overlays.yaml")
    if ov.get("schema") != "kardakia-class-overlays/1":
        raise Refuse(f"schema: want kardakia-class-overlays/1, got {ov.get('schema')!r}")
    tm = load_yaml((cfg.get("tools") or {}).get("term_map") or "Campaign/term-map.yaml")
    tmap = {(t.get("rulebook"), t.get("kardakia")) for t in (tm.get("terms") or []) if isinstance(t, dict)}
    terms = ov.get("terms") or []
    orphan = [t for t in terms if (t.get("rulebook"), t.get("kardakia")) not in tmap]
    if orphan:
        raise Refuse("overlay terms not in term map: " + "; ".join(
            f"{t.get('rulebook')!r} -> {t.get('kardakia')!r}" for t in orphan[:5]))

    tm_inputs = tm.get("inputs") or {}
    ov_inputs = ov.get("inputs") or {}
    for group, pairs in ov_inputs.items():
        src = tm_inputs.get(group)
        if not isinstance(src, dict):
            raise Refuse(f"overlay inputs.{group}: no matching group in term-map.yaml inputs")
        for k, v in pairs.items():
            if src.get(k) != v:
                raise Refuse(f"overlay inputs.{group}.{k!r} -> {v!r} does not match term-map (got {src.get(k)!r})")

    notes = class_note_split(cfg)
    titles = banned_titles(cfg)
    for t in terms:
        kv = (t.get("kardakia") or "").strip()
        if not kv:
            continue
        kvl = kv.lower()
        # judge-only-only: a term that lives in a class note's Judge-only callout AND appears in no public
        # section of ANY class note is a planted secret (e.g. "the Unmother", "the Hollow").
        in_judge = any(kvl in j for _, j in notes)
        in_public = any(kvl in p for p, _ in notes)
        if in_judge and not in_public:
            raise Refuse(f"overlay term {kv!r} appears only in a Judge-only callout of a class note")
        for b in titles:
            # a term matching a Judge-only note title (whole word) or holding a Judge-only marker is refused
            if not b:
                continue
            if b in ("[!danger]", "judge only", "[h] ") and b in kvl:
                raise Refuse(f"overlay term {kv!r} holds Judge-only marker {b!r}")
            if re.search(rf"(?<!\w){re.escape(b)}(?!\w)", kvl):
                raise Refuse(f"overlay term {kv!r} matches Judge-only note title {b!r}")

    return len(terms), sum(len(p) for p in ov_inputs.values())


try:
    nt, ni = check(jlib.config())
except Refuse as e:
    print("overlay REFUSED: " + str(e), file=sys.stderr); sys.exit(2)
print(f"overlay ok: {nt} terms, {ni} inputs")
