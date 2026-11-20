#!/usr/bin/env python3
"""npc.py NOTE [--class C] [--level L] [--race R] [--alignment A] [--kit TROOP] [--occupation O] [--hp-max H]
An NPC's numbers, made on demand (engine 7.3.0, actor sheets WP6): the first time an NPC of the people folder (config
paths.wiki_folders.people) needs numbers (a fight, a throw, hiring him), this creates his actor
Actors/npc/<id>.json with `acks.sh actor new --role npc` (what is not given is generated, every roll hidden) and writes
`actor: <id>` into the note's front matter. The note keeps the prose; the actor keeps the numbers (D5). If the note
already names an actor, it prints it and changes nothing.
  NOTE      the note's name (file name without .md) or path
  --level   default: the note's `level:` property; 0 for a 0th-level NPC
  --class   required above 0th level (the note does not say; the Judge chooses, or rolls `acks.sh npc-class`)
The id is the note's name in lower case with dashes (Bessos Half-Hand -> bessos-half-hand)."""
import glob, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import jlib

HERE = os.path.dirname(os.path.abspath(__file__))


def val(args, k):
    return args[args.index(k) + 1] if k in args and args.index(k) + 1 < len(args) else None


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "npc"


def note_path(cfg, name):
    if name.endswith(".md") and os.path.exists(jlib.path(name)):
        return os.path.relpath(jlib.path(name), jlib.ROOT)
    folder = jlib.path(cfg["paths"]["wiki_folders"]["people"])
    hits = [p for p in glob.glob(os.path.join(folder, "**", "*.md"), recursive=True)
            if os.path.basename(p)[:-3].lower() == name.lower()]
    if len(hits) != 1:
        jlib.die(f"{name}: {'no' if not hits else len(hits)} note(s) of that name in {folder}")
    return os.path.relpath(hits[0], jlib.ROOT)


def set_actor(rel, aid):
    """Add `actor: "<id>"` to the note's front matter as one line (the rest of the front matter is left as written)."""
    text = open(jlib.path(rel), encoding="utf-8").read()
    m = jlib.FM.match(text)
    if not m:
        text = f'---\nactor: "{aid}"\n---\n' + text
    elif re.search(r"^actor:.*$", m.group(1), re.M):
        fm = re.sub(r"^actor:.*$", f'actor: "{aid}"', m.group(1), count=1, flags=re.M)
        text = "---\n" + fm + "\n---\n" + text[m.end():]
    else:
        text = "---\n" + m.group(1) + f'\nactor: "{aid}"\n---\n' + text[m.end():]
    with open(jlib.path(rel), "w", encoding="utf-8") as f:
        f.write(text)


def main(a):
    if not a or a[0].startswith("--"):
        print(__doc__); return 1
    cfg = jlib.config()
    rel = note_path(cfg, a[0])
    fm, _ = jlib.read_note(rel)
    name = os.path.basename(rel)[:-3]
    if fm.get("actor"):
        print(f"{name}: actor {fm['actor']} already ({rel}); `acks.sh actor show {fm['actor']}`")
        return 0
    level = val(a, "--level") if "--level" in a else fm.get("level")
    if level in (None, ""):
        jlib.die(f"{name}: no level in the note; pass --level N (0 for a 0th-level NPC)")
    cls = val(a, "--class")
    if int(level) > 0 and not cls:
        jlib.die(f"{name}: level {level}: pass --class C (the Judge's choice from the note, or `acks.sh npc-class`)")
    aid = slug(name)
    folder = next((d for d in (cfg["paths"].get("actors") or []) if d.rstrip("/").endswith("npc")), "Actors/npc/")
    out = os.path.join(jlib.path(folder), aid + ".json")
    cmd = ["bash", os.path.join(HERE, "acks.sh"), "actor", "new", "--role", "npc", "--name", name,
           "--level", str(level), "--out", out]
    for k in ("--class", "--race", "--alignment", "--kit", "--occupation", "--hp-max", "--method"):
        if val(a, k) is not None:
            cmd += [k, val(a, k)]
    for i, x in enumerate(a):              # --attr STR=15 (repeatable: a notable NPC's printed scores)
        if x == "--attr" and i + 1 < len(a):
            cmd += ["--attr", a[i + 1]]
    if "--attr" in a:
        cmd += ["--id", aid]               # given scores: the engine's manual form wants the id
    r = subprocess.run(cmd, capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())
    if r.returncode or not os.path.exists(out):
        return r.returncode or 1
    set_actor(rel, aid)
    print(f"{rel}: actor: {aid}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
