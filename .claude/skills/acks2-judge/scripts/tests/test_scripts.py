"""Tests of the Judge skill's scripts. They never touch the campaign: each test works on a temporary copy of the
repo (JUDGE_REPO), with the campaign's own files as test material. Run: python3 -m pytest -q <skill>/scripts/tests
(needs the engine installed: setup.sh)."""
import json
import os
import shutil
import subprocess
import sys

import pytest

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.abspath(os.path.join(S, "..", "..", "..", ".."))


@pytest.fixture()
def camp(tmp_path):
    dst = tmp_path / "camp"
    shutil.copytree(REPO, dst, ignore=shutil.ignore_patterns(".git", "__pycache__", "Maps", "*.png",
                                                                 "*.pdf", "archive"))
    return str(dst)


def need(camp, rel, text=None):
    """Skip a test whose material this campaign does not have (the tests travel with the skill to every campaign)."""
    p = os.path.join(camp, rel)
    if not os.path.exists(p) or (text and text not in open(p, encoding="utf-8").read()):
        pytest.skip(f"this campaign has no {rel}" + (f" with {text!r}" if text else ""))


def first_member(camp):
    need(camp, "Campaign/exploration-state.json")
    ids = list(json.load(open(os.path.join(camp, "Campaign", "exploration-state.json"))).get("party") or {})
    if not ids:
        pytest.skip("no exploration party")
    return ids[0]


def sh(camp, *args, script="acks.sh", stdin=None, env=None):
    cmd = ["bash", os.path.join(S, script), *args] if script.endswith(".sh") else [sys.executable, os.path.join(S, script), *args]
    r = subprocess.run(cmd, capture_output=True, text=True, input=stdin,
                       env={**os.environ, "JUDGE_REPO": camp, **(env or {})})
    return r.returncode, r.stdout + r.stderr


def argv_of(camp, *args):
    code, out = sh(camp, "--print-argv", *args, script="jacks.py")
    lines = out.strip().splitlines()
    return dict(l.split("=", 1) for l in lines[:-1]), lines[-1]


def test_each_stage_gets_its_states(camp):
    C = os.path.join(camp, "Campaign")
    env, line = argv_of(camp, "turn", "1")
    assert f"--state {C}/combat-state.json --xstate {C}/exploration-state.json --retinue {C}/retinue-state.json" in line
    assert f"--log {C}/roll-log.jsonl --session " in line
    assert env["ACKS_ACTORS"].split(os.pathsep)[0] == os.path.join(camp, "Characters")
    if os.path.exists(os.path.join(C, "lessons.yaml")):
        assert env["ACKS_LESSONS"].endswith("Campaign/lessons.yaml")
    if os.path.exists(os.path.join(C, "schedule.yaml")):
        assert env["ACKS_SCHEDULE"].endswith("Campaign/schedule.yaml")
    assert "--xstate" not in argv_of(camp, "roll", "x:1d6")[1] and "--state" not in argv_of(camp, "roll", "x:1d6")[1]
    assert "--hexes" in argv_of(camp, "travel", "22.21")[1]
    assert "--astate" in argv_of(camp, "payout")[1] and "--retinue" in argv_of(camp, "payout")[1]
    assert "--party-hp" in argv_of(camp, "encounter", "fight", "--perceived", "x")[1]
    import yaml
    if (yaml.safe_load(open(os.path.join(C, "campaign.yaml"), encoding="utf-8")).get("tools") or {}).get("bestiary"):
        assert "--bestiary" in argv_of(camp, "state", "add", "o", "--side", "foe", "--monster", "Orc", "--perceived", "x")[1]
    assert "--astate" in argv_of(camp, "adventure", "init")[1]
    assert "--xstate" in argv_of(camp, "enervation", "show")[1] and "--xstate" in argv_of(camp, "schedule", "due")[1]


def test_a_foe_joins_only_under_a_perceived_name(camp):
    code, out = sh(camp, "state", "add", "o1", "--side", "foe", "--monster", "Orc")
    assert code == 2 and out.startswith("NOT ALLOWED: pass --perceived")


def test_rolls_are_logged_with_session_and_visibility(camp):
    log = os.path.join(camp, "Campaign", "roll-log.jsonl")
    n = sum(1 for _ in open(log)) if os.path.exists(log) else 0
    code, out = sh(camp, "roll", "--hidden", "a guard's morale:2d6")
    assert code == 0 and out.startswith("[H] ")
    recs = [json.loads(x) for x in open(log)]
    assert len(recs) == n + 1 and recs[-1]["vis"] == "hidden" and recs[-1]["label"] == "a guard's morale"


def test_lessons_fire_through_the_wrapper(camp):
    need(camp, "Campaign/lessons.yaml", "npc-rolls-hidden")
    need(camp, "Campaign/lessons.yaml", "slab-no-minus-12")
    code, out = sh(camp, "roll", "a guard's morale:2d6")
    assert code == 1 and "NOT RUN (lesson): [npc-rolls-hidden]" in out
    code, out = sh(camp, "lesson", "check")
    assert code == 0 and "lessons:" in out
    code, out = sh(camp, "lesson", "test", "--", "explore", "force-door", "varro", "--mod", "slab:-12")
    assert "REFUSE [slab-no-minus-12]" in out


def test_batch_runs_in_order_and_stops_at_a_refusal(camp):
    code, out = sh(camp, "batch", stdin="# two rolls, a refusal, one never run\nroll x:1d6\nroll y:1d6\nstate add o --side foe --monster Orc\nroll z:1d6\n")
    assert code == 2 and "$ roll x:1d6" in out and "y: 1d6" in out and "z: 1d6" not in out
    assert "batch: stopped at line 4 (exit 2); 1 command not run" in out


def test_schedule_is_named_by_the_clock(camp):
    need(camp, "Campaign/schedule.yaml", "order-roll")
    lp = os.path.join(camp, "Campaign", "schedule-log.jsonl")
    if os.path.exists(lp):
        os.remove(lp)                      # the campaign's own record has run day 480 long since: a fresh record
    code, out = sh(camp, "schedule", "due", "--day", "480")
    assert "DUE order-roll" in out and "DUE month-end" in out
    code, out = sh(camp, "schedule", "check")
    assert code == 0


def test_play_ledger_rows_are_appended_once(tmp_path):
    sys.path.insert(0, S)
    import play
    led = tmp_path / "Ledger.md"
    led.write_text("# Ledger\n\n## Monster XP\n| Day | Monster | XP |\n| --- | --- | --- |\n| 1 | rat | 5 |\n\n## Wages\n| a |\n")
    rows = play.ledger_rows("## Monster XP\n| Day | Monster | XP |\n| --- | --- | --- |\n| 2 | orc | 10 | (src: RR p. 310)\n| 1 | rat | 5 |\n## Nowhere\n| x |\n")
    assert rows["Monster XP"][-2] == "| 2 | orc | 10 |"
    done = play.append_rows(str(led), {"Monster XP": ["| 2 | orc | 10 |", "| 1 | rat | 5 |"]})
    assert done == {"Monster XP": 1}
    text = led.read_text()
    assert text.count("| 2 | orc | 10 |") == 1 and text.count("| 1 | rat | 5 |") == 1 and "## Wages\n| a |" in text
    assert play.append_rows(str(led), {"Monster XP": ["| 2 | orc | 10 |"]}) == {"Monster XP": 0}


def test_play_supplies_and_walk_stop(camp):
    who = first_member(camp)
    need(camp, "Campaign/inventory-state.json")
    code, out = sh(camp, "supplies", who, script="play.py")
    assert code == 0 and out.startswith(who + ": ") and out.strip().endswith("gp")
    sh(camp, "location", "--clear")
    sh(camp, "location", "--site", "Test halls", "--level", "1")
    code, out = sh(camp, "walk", "3", script="play.py")           # no light lit, no carriers named: it stops
    assert code == 3 and "-- stop: no light is lit" in out


def test_handoff_is_generated_and_keeps_the_judges_notes(camp):
    first_member(camp)
    code, out = sh(camp, "--notes", "Next: the G2b faewyrd.", script="handoff.py")
    assert code == 0
    p = os.path.join(camp, "Campaign", "handoff.md")
    t = open(p, encoding="utf-8").read()
    assert "<!-- generated:start -->" in t and "| Party | Class | XP | hp | Conditions |" in t
    assert "**Wages:**" in t and "Next: the G2b faewyrd." in t
    code, out = sh(camp, script="handoff.py")                      # regenerated: the Judge's block is kept
    t2 = open(p, encoding="utf-8").read()
    assert "Next: the G2b faewyrd." in t2 and t2.count("## Judge's notes for the next session") == 1
    code, out = sh(camp, script="brief.py")
    assert "===== handoff" in out and "Next: the G2b faewyrd." in out


def test_snapshot_allows_an_unidentified_twin_of_a_known_name(camp):
    ap = os.path.join(camp, "Campaign", "adventure-state.json")
    need(camp, "Campaign/adventure-state.json")
    adv = json.load(open(ap))
    ident = next((l for l in adv["lots"].values() if l.get("kind") == "item" and l.get("identified")
                  and (l.get("true") or {}).get("name") and l.get("status") == "carried"), None)
    if ident is None:
        pytest.skip("no identified item carried in this campaign's ledger")
    twin = json.loads(json.dumps(ident))
    twin.update(id="L9999", identified=False, status="left")
    twin["player"] = {**twin["player"], "desc": "a blade wrapped in oilcloth"}
    adv["lots"]["L9999"] = twin
    json.dump(adv, open(ap, "w"))
    code, out = sh(camp, "--check", script="snapshot.py")           # the identified twin publishes the name
    assert code == 0, out


def test_hex_shows_the_engines_classification(camp):
    """Engine 7.18.0 (A1): the table's 'wilderness' and a domain's hexes as the engine reads them."""
    import csv as _csv
    cfgp = os.path.join(camp, "Campaign", "campaign.yaml")
    import yaml as _yaml
    cfg = _yaml.safe_load(open(cfgp))
    H = cfg.get("hexes") or {}
    if not H.get("csv"):
        pytest.skip("no hex table")
    col = (H.get("columns") or {}).get("classification")
    rows = list(_csv.DictReader(open(os.path.join(camp, H["csv"]), encoding="utf-8")))
    wild = [r for r in rows if (r.get(col) or "").strip().lower() == "wilderness"
            and r[H["columns"]["hex"]] not in {h for d in (H.get("domains") or []) for h in d.get("hexes", [])}]
    if not wild:
        pytest.skip("no 'wilderness' hex outside a domain")
    code, out = sh(camp, wild[0][H["columns"]["hex"]], script="hex.py")
    assert code == 0 and "engine_classification: unsettled" in out
    for d in H.get("domains") or []:
        if isinstance(d, dict) and d.get("hexes"):
            code, out = sh(camp, d["hexes"][0], script="hex.py")
            assert f"engine_classification: {d['classification']}" in out


def test_play_depart_checklist(camp):
    """C1: the pre-march checklist reads the states, changes nothing and ends READY or NOT READY."""
    need(camp, "Campaign/exploration-state.json")
    before = open(os.path.join(camp, "Campaign", "exploration-state.json")).read()
    xs = json.load(open(os.path.join(camp, "Campaign", "exploration-state.json")))
    day = xs["clock"]["day"]
    code, out = sh(camp, "depart", "--return-day", str(day + 5), script="play.py")
    assert code in (0, 3) and ("READY" in out.splitlines()[-1])
    assert any(ln.startswith(("OK", "WARN", "FAIL")) for ln in out.splitlines())
    assert open(os.path.join(camp, "Campaign", "exploration-state.json")).read() == before


def test_play_march_stops_or_marches(camp):
    """C2: march runs in one process and ends with the route's end, the days marched, or a STOP line saying why."""
    need(camp, "Campaign/exploration-state.json")
    xs = json.load(open(os.path.join(camp, "Campaign", "exploration-state.json")))
    if not xs.get("travel"):
        pytest.skip("no travel block")
    here = xs["travel"]["hex"]
    c, r = (int(x) for x in here.split("."))
    route = f"{c:02d}.{r + 1:02d}"
    code, out = sh(camp, "march", "1", "--route", route, "--hours-per-day", "2", script="play.py",
                   env={"ACKS_ACK": "water-short"})
    assert code in (0, 3), out
    assert out.startswith("day ") or out.startswith("arrived")
    if code == 3:
        assert "STOP:" in out


def test_play_city_week_refuses_then_writes(camp):
    """C3: no six entries -> the template and exit 3; with them -> the weekly block run and the line written."""
    need(camp, "Campaign/schedule.yaml", "weekly-secret")
    need(camp, "Campaign/World State.md")
    code, out = sh(camp, "schedule", "due", "--ahead", "7", "--json")
    d = json.loads(out[out.find("{"):]).get("data") or {}
    occ = [x for x in (d.get("due") or []) if x["id"] == "weekly-secret"] + \
        [x for x in (d.get("ahead") or []) if x["id"] == "weekly-secret"]
    if not occ:
        pytest.skip("no weekly secret due within the week")
    day = occ[0].get("due_day") or occ[0].get("day")
    code, out = sh(camp, "city-week", "--day", str(day), script="play.py")
    assert code == 3 and f"- **Day {day} weekly: the week's secrets**" in out
    p = os.path.join(camp, "Campaign", "World State.md")
    s = open(p, encoding="utf-8").read()
    s = s.replace("## Scheduled events\n", "## Scheduled events\n- **Day %d weekly: the week's secrets** (S99; entries "
                  "written before the roll): 1 a; 2 b; 3 c; 4 d; 5 e; 6 f.\n" % day, 1)
    open(p, "w", encoding="utf-8").write(s)
    code, out = sh(camp, "city-week", "--day", str(day), script="play.py")
    assert code == 0, out
    assert "**rolled" in open(p, encoding="utf-8").read()


def test_play_month_end_dry_run(camp):
    """C4: --dry-run lists the month's end from the campaign's month_end block and changes nothing."""
    need(camp, "Campaign/campaign.yaml", "month_end:")
    before = open(os.path.join(camp, "Campaign", "World State.md"), encoding="utf-8").read()
    code, out = sh(camp, "month-end", "--dry-run", script="play.py")
    assert code == 0 and "month's end, day" in out and "schedule run" in out
    assert open(os.path.join(camp, "Campaign", "World State.md"), encoding="utf-8").read() == before


def test_brief_prints_the_named_parts_only(camp):
    """C5: the brief prints the parts the resume names (not the whole World State and Rulings); --full prints all."""
    code, out = sh(camp, script="brief.py")
    assert code == 0 and "===== handoff" in out and "the last" in out
    ws = open(os.path.join(camp, "Campaign", "World State.md"), encoding="utf-8").read()
    if len(ws.splitlines()) > 200:
        assert len(out.splitlines()) < len(ws.splitlines()) + 200
    code, full = sh(camp, "--full", script="brief.py")
    assert len(full) > len(out)


def test_handoff_lists_members_left_behind(camp):
    need(camp, "Campaign/exploration-state.json", '"staying"')
    xs = json.load(open(os.path.join(camp, "Campaign", "exploration-state.json")))
    if not xs.get("staying"):
        pytest.skip("no one left behind")
    sys.path.insert(0, S)
    code, out = sh(camp, script="brief.py")
    assert "**Left behind:**" in out and next(iter(xs["staying"])) in out


def test_play_walk_stops_at_a_timer_and_refuels_a_lantern(camp):
    """D8: walk stops when a timer runs out; a carrier's burnt-out lantern is refuelled and lit when he has oil."""
    need(camp, "Campaign/exploration-state.json")
    xs = json.load(open(os.path.join(camp, "Campaign", "exploration-state.json")))
    lan = [l for l in xs.get("lights") or [] if l.get("kind") == "lantern" and not l.get("lit")
           and l.get("carrier") in (xs.get("party") or {})]
    if not lan:
        pytest.skip("no unlit lantern in the party")
    who = lan[0]["carrier"]
    sh(camp, "timer", "add", "the unsettling event", "--for", "1t")
    code, out = sh(camp, "walk", "3", "--relight", who, "--kind", "lantern", script="play.py")
    assert "timer 'the unsettling event'" in out and code == 3, out
    assert "relit:" in out, out


def test_capture_and_train_get_the_training_state(camp):
    """Engine 7.20 (S54 F): capture and train run with the training state (ACKS_TSTATE) and the clock."""
    C = os.path.join(camp, "Campaign")
    env, line = argv_of(camp, "capture", "peg", "--how", "slumbering", "--by", "M")
    assert env["ACKS_TSTATE"] == f"{C}/training-state.json"
    assert f"--xstate {C}/exploration-state.json --state {C}/combat-state.json" in line
    env, line = argv_of(camp, "train", "show")
    assert f"--xstate {C}/exploration-state.json" in line and "--state " not in line
