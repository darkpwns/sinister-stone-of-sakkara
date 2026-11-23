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
