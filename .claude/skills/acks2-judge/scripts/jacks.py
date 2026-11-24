#!/usr/bin/env python3
"""jacks.py CMD [args] : the rules engine (acks2-tools, `acks`) with this campaign's files, in one process.

acks.sh runs this. It adds what the campaign's config names (Campaign/campaign.yaml): the roll log and session
number, the engine rulings, the combat, exploration, retinue, adventure and inventory states, the hex adapter, the
actor folders, the campaign's bestiary, item and table folders, the class and race aliases, the term map and the
lessons index (ACKS_LESSONS). Every roll is logged like dice.py's. Which state a command gets is the table in
`extra_for` (stage by stage, as acks.sh always did); the engine then runs in this same interpreter.

`jacks.py batch [FILE|-] [--keep-going] [--stop-on REGEX] [--stop-on-judge]`: many commands, one per line, written
as after `acks.sh` (blank lines and # comments skipped), run one after the other in this process: each gets its own
dice, log lines, state reads and writes and refusals, exactly as when run alone; the batch stops at the first
refusal or error (or at a stop condition) and says how many commands were not run.

Python helpers import this module and call `run(["turn", "1"])` -> (exit code, output text): no new process per call.
"""
import contextlib
import io
import os
import re
import shlex
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import jlib  # noqa: E402

STAGE2 = {"explore-init", "party", "location", "light", "timer", "explore", "wander-check", "reaction", "move-rate",
          "clock", "disease", "walk"}
STAGE4 = {"travel-init", "travel", "forced-march", "navigate", "weather", "forage", "water", "firewood", "hunt",
          "fish", "eat", "drink", "supplies", "camp", "rest-day", "heal", "mounts", "search", "travel-show",
          "terrain-encounter"}
STAGE5A = {"treasure", "place", "item", "recover", "appraise", "identify", "use", "sell"}
STAGE5B = {"payout", "level-up", "advance-0th", "death"}
STAGE3 = {"retinue", "recruit", "candidate", "offer", "hire", "dismiss", "transfer", "wages", "loyalty", "obey",
          "npc-party", "npc-class", "wait", "spellcasting"}


def context():
    """The campaign's paths and settings, read once per process from Campaign/campaign.yaml and Campaign State."""
    cfg = jlib.config()
    st = cfg["paths"]["state"]
    fm, _ = jlib.read_note(st["campaign_state"])
    t = cfg.get("tools", {}) or {}
    tt = t.get("treasure") or {}
    rul = t.get("engine_rulings")
    rul = jlib.path(rul) if rul and os.path.exists(jlib.path(rul)) else ""
    best = [jlib.path(b) for b in (t.get("bestiary") or [])]
    tables = t.get("tables")
    if tables is None:                       # default: every Tables/ folder under the campaign's sites folder
        base = jlib.path(((cfg.get("paths") or {}).get("sites_folder") or "Adventure/").rstrip("/"))
        tables = sorted((os.path.join(d, "Tables") for d, subs, _f in os.walk(base) if "Tables" in subs),
                        key=lambda p: (p.count(os.sep), p)) if os.path.isdir(base) else []   # shallowest first
    else:
        tables = [jlib.path(x) for x in tables]
    lessons = jlib.path(t.get("lessons", "Campaign/lessons.yaml"))
    schedule = jlib.path(t.get("schedule", "Campaign/schedule.yaml"))
    return {
        "cfg": cfg,
        "log": jlib.path(st["roll_log"]), "session": str(fm.get("session", 0)),
        "state": jlib.path(t.get("combat_state", "Campaign/combat-state.json")),
        "xstate": jlib.path(t.get("exploration_state", "Campaign/exploration-state.json")),
        "cstate": jlib.path(st["campaign_state"]),
        "rstate": jlib.path(t.get("retinue_state", "Campaign/retinue-state.json")),
        "hexes": jlib.path(t.get("hexes", "Campaign/campaign.yaml")),
        "astate": jlib.path(t.get("adventure_state", "Campaign/adventure-state.json")),
        "istate": jlib.path(t.get("inventory_state", "Campaign/inventory-state.json")),
        "actors": os.pathsep.join(jlib.actor_dirs(cfg)),
        "bestiary": best, "items": os.pathsep.join(jlib.path(b) for b in (t.get("items") or [])),
        "tables": os.pathsep.join(tables),
        "term_map": jlib.path(t.get("term_map", "Campaign/term-map.yaml")),
        "tset": str(tt.get("setting", "") or ""), "arms": str(tt.get("arms_setting", "") or ""),
        "rulings": rul,
        "aliases": jlib.path("Campaign/campaign.yaml") if (t.get("class_aliases") or t.get("race_aliases")) else "",
        "lessons": lessons if os.path.exists(lessons) else "",
        "schedule": schedule if os.path.exists(schedule) else "",
    }


def env_for(ctx, cmd, args):
    """The ACKS_* environment of one command."""
    env = {"ACKS_ISTATE": ctx["istate"], "ACKS_INV_XSTATE": ctx["xstate"], "ACKS_INV_ASTATE": ctx["astate"],
           "ACKS_INV_RETINUE": ctx["rstate"], "ACKS_ACTORS": ctx["actors"], "ACKS_INPUT_ALIASES": ctx["term_map"],
           "ACKS_BESTIARY": os.pathsep.join(ctx["bestiary"]), "ACKS_TABLES": ctx["tables"], "ACKS_ITEMS": ctx["items"],
           "ACKS_LESSONS": ctx["lessons"], "ACKS_SCHEDULE": ctx["schedule"], "ACKS_CSTATE": ctx["cstate"],
           "ACKS_LESSONS_STATE": ctx["state"],        # the combat state, for lessons that ask about the fight
           "ACKS_HEXES": ctx["hexes"]}                # the hex adapter (treasure --terrain reads its terrain codes)
    if cmd == "actor" and args[:1] == ["import"] and not os.path.exists(ctx["istate"]):
        env["ACKS_ISTATE"] = None            # no inventory yet: import keeps possessions (D10)
    return env


def refusal(cmd, args):
    """Open-roll labels reach the snapshot: a foe joins a fight only under the name the party perceives (SKILL.md §4)."""
    joined = " " + " ".join(args) + " "
    foe_joins = (cmd == "encounter" and args[:1] == ["fight"]) or (cmd == "npc-party" and " --to-state " in joined) \
        or (cmd == "state" and args[:1] == ["add"] and " --side party " not in joined)
    if foe_joins and not any(a == "--perceived" or a.startswith("--perceived=") for a in args):
        return ("NOT ALLOWED: pass --perceived \"<what the party sees>\" (open-roll labels use it and reach the "
                "snapshot; a monster's true name only once the party knows it)")
    return None


def extra_for(ctx, cmd, args):
    """The options acks.sh adds to a command: log, session, rulings, aliases, bestiary, and the states of its stage."""
    S, X, R, A, H = ctx["state"], ctx["xstate"], ctx["rstate"], ctx["astate"], ctx["hexes"]
    ex = ["--log", ctx["log"], "--session", ctx["session"]]
    if ctx["rulings"]:
        ex += ["--rulings", ctx["rulings"]]
    if ctx["aliases"] and cmd != "check":
        ex += ["--aliases", ctx["aliases"]]
    if cmd in ("state", "encounter", "monster"):
        for b in ctx["bestiary"]:
            ex += ["--bestiary", b]
    if cmd in ("roll", "version", "check", "monster"):
        pass
    elif cmd in ("lesson", "schedule", "compact"):
        ex += ["--xstate", X]
    elif cmd in STAGE2:
        ex += ["--state", S, "--xstate", X] + (["--retinue", R] if cmd == "walk" else [])
    elif cmd in ("evade", "pursue"):
        ex += ["--state", S, "--xstate", X, "--hexes", H]
    elif cmd in ("turn", "rest", "enervate", "enervation"):
        ex += ["--state", S, "--xstate", X, "--retinue", R]
    elif cmd == "encounter":
        ex += ["--state", S, "--xstate", X, "--retinue", R, "--hexes", H]
        if args[:1] == ["fight"]:
            ex += ["--party-hp", ctx["cstate"]]
    elif cmd in STAGE4:
        ex += ["--xstate", X, "--hexes", H, "--retinue", R]
    elif cmd == "adventure":
        ex += ["--astate", A, "--xstate", X]
        if args[:1] == ["init"]:
            if ctx["tset"]:
                ex += ["--setting", ctx["tset"]]
            if ctx["arms"]:
                ex += ["--arms-setting", ctx["arms"]]
    elif cmd in STAGE5A:
        ex += ["--astate", A, "--xstate", X]
    elif cmd in STAGE5B:
        ex += ["--astate", A, "--xstate", X, "--retinue", R]
    elif cmd == "restore":
        pass
    elif cmd == "inv":
        ex += ["--xstate", X, "--astate", A, "--retinue", R]
    elif cmd in STAGE3:
        ex += ["--state", S, "--xstate", X, "--retinue", R]
    elif cmd == "chargen":
        ex += ["--retinue", R]
    elif cmd == "class":
        pass
    else:
        ex += ["--state", S, "--retinue", R]
    return ex


def _engine():
    try:
        from acks import cli
        return cli
    except ImportError:
        return None


def _apply_env(env):
    for k, v in env.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


def run(argv, ctx=None, capture=True):
    """Run one engine command as acks.sh does. Returns (exit code, output text) (text '' when not captured)."""
    cli = _engine()
    if cli is None:
        return 2, "error: engine not installed (run the tools repo setup.sh; fallback: dice.py)\n"
    ctx = ctx or context()
    cmd, args = argv[0], list(argv[1:])
    no = refusal(cmd, args)
    if no:
        return 2, no + "\n"
    _apply_env(env_for(ctx, cmd, args))
    if cmd == "encounter" and args[:1] == ["fight"]:      # current hp come from public.party: regenerate it first
        r = subprocess.run([sys.executable, os.path.join(HERE, "xsync.py"), "--party"], capture_output=True, text=True)
        sys.stderr.write(r.stdout + r.stderr)
    full = [cmd, *args, *extra_for(ctx, cmd, args)]
    buf = io.StringIO()
    try:
        if capture:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                code = cli.run(full)
        else:
            code = cli.run(full)
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else 2
    return int(code or 0), buf.getvalue()


def batch(argv):
    import argparse
    ap = argparse.ArgumentParser(prog="acks.sh batch", description=__doc__.split("\n\n")[2])
    ap.add_argument("file", nargs="?", default="-")
    ap.add_argument("--keep-going", action="store_true", help="run every command; exit 1 if any was refused")
    ap.add_argument("--stop-on", action="append", default=[], metavar="REGEX",
                    help="stop after a command whose output matches (repeatable)")
    ap.add_argument("--stop-on-judge", action="store_true", help="stop after a command that leaves something to the Judge")
    b = ap.parse_args(argv)
    text = sys.stdin.read() if b.file == "-" else open(b.file, encoding="utf-8").read()
    lines = [(n, ln.strip()) for n, ln in enumerate(text.splitlines(), 1)]
    lines = [(n, ln) for n, ln in lines if ln and not ln.startswith("#")]
    stops = [re.compile(x) for x in b.stop_on]
    if b.stop_on_judge:
        stops.append(re.compile(r' \| JUDGE: |"judge": \[\s*"'))
    ctx, worst = context(), 0
    for i, (n, ln) in enumerate(lines):
        try:
            args = shlex.split(ln)
        except ValueError as e:
            print(f"batch: line {n}: {e}")
            return 2
        if args and os.path.basename(args[0]) in ("acks.sh", "acks", "jacks.py"):
            args = args[1:]
        print(f"$ {ln}")
        code, out = run(args, ctx) if args and args[0] != "batch" else (2, "batch: no nested batch\n")
        sys.stdout.write(out)
        sys.stdout.flush()
        why = f"exit {code}" if code and not b.keep_going else ("stop condition met" if any(s.search(out) for s in stops) else None)
        worst = worst or code
        if why:
            left = len(lines) - i - 1
            print(f"batch: stopped at line {n} ({why}); {left} command{'s' if left != 1 else ''} not run")
            return code or 0
    return 1 if worst else 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        argv = ["--help"]
    if argv[0] == "batch":
        return batch(argv[1:])
    if argv[0] == "--print-argv":            # for tests: the command line and environment a call would get
        ctx = context()
        cmd, args = argv[1], argv[2:]
        env = env_for(ctx, cmd, args)
        print("\n".join(f"{k}={env[k] or ''}" for k in sorted(env)))
        print(shlex.join([cmd, *args, *extra_for(ctx, cmd, args)]))
        return 0
    if argv[0].startswith("-"):
        cli = _engine()
        if cli is None:
            print("error: engine not installed (run the tools repo setup.sh; fallback: dice.py)")
            return 2
        try:
            return int(cli.run(argv) or 0)
        except SystemExit as e:
            return e.code if isinstance(e.code, int) else 2
    code, out = run(argv, capture=False)     # not captured: `out` is only a refusal made here
    sys.stdout.write(out)
    return code


if __name__ == "__main__":
    sys.exit(main())
