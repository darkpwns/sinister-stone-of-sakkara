# Judge memory, the schedule, the handoff and running many commands (engine 7.16.0+)

Design: `engine/docs/judge-memory.md` in the tools repo. In short: a lesson is not something to remember, it is
something that happens: the engine or a script does it; or it fires on its trigger; or the brief states it.

## Lessons (`Campaign/lessons.yaml`, Judge only)
- Every `acks.sh` call is checked against the index. ` | REMINDER: [id] text (source)` at the end of a line: the
  lesson applies to what you are doing now; act on it before going on. `NOT RUN (lesson): [id] …`: the command was
  refused and nothing was rolled; fix the command, or put `ACKS_ACK=id` before it when you do mean it.
- `acks.sh lesson list` (all, with slip counts); `lesson test -- CMD ARGS…` (which lessons a command would fire,
  without running it); `lesson brief` (those standing in the current state); `lesson check` (save.sh runs it).
- **A slip** (you notice a recorded lesson was missed): `acks.sh lesson slip ID --day N --note "what happened"`, and
  the judge-notes line as before. A lesson slipped on again is printed as `ESCALATE` in the brief and at every save
  until it is moved into the engine or a script, made a refusal, or its trigger is tightened.
- **A new lesson** (a new kind of slip, or a ruling that must be applied at a certain moment): add an entry with a
  trigger: `on` (the command, e.g. `[save]` or `["encounter start"]`), `args`/`with`/`without`, `where` (facts: the
  place, light, encounter, fight, the actor's conditions …: the list is in `acks/lessons.py`), `text`, `source`,
  `status: remind` (or `refuse` for what cannot be undone once done). Try it with `lesson test`. Prose-only
  (`status: judge`) is the last resort.
- A ruling that changes an engine number still goes into `Campaign/engine-rulings.yaml` (door kinds: its `doors:`
  block); a worn item or standing power goes on the actor once: `acks.sh actor mod ID throws.hiding -8 --flat 12
  --source "Cloak of the Elven Ranger" --rule "TT p. 151" --item L528 --cause "worn"` (bonuses to throws and saves are
  negative; `saves.all`, `damage`, `initiative`, `attack_throw`, `ac.*`; `note.<command>[.<arg>] --text "…"` for what
  the engine cannot apply as a number: it is printed on that command). `actor mod ID --list`; `actor unmod ID --item L#`
  when the item changes hands.

## The schedule (`Campaign/schedule.yaml`, Judge only)
Recurring procedures as data: items that fall every N days, at month's end or on a day, with their rolls (all hidden)
and the Judge's steps. `acks.sh schedule due --ahead 7`; `schedule run --due` (or `run ID`) rolls an item and prints
its steps; `schedule done ID --note "…"` when handled by hand; `schedule skip ID --note "missed: no back-roll"`.
What was done is in `Campaign/schedule-log.jsonl`. Every clock command (`turn`, `wait`, `clock` …) names what is due.
A new recurring thing (a weekly roll a ruling creates, a fee, a dated event) is a new item here, not a line in the
prep queue.

## The handoff (`Campaign/handoff.md`, Judge only)
One file, rewritten each session (`handoff.py`; save.sh runs it at `S## end`): a generated block (date, place, the
party with XP, hp and conditions, the adventure, wages with the engine's due days, the schedule, the standing
reminders, lessons to escalate) and the Judge's notes for the next session (`handoff.py --notes-file FILE`). Never
write a number into the Judge's notes that the generated block can give. `brief.py` prints it at session start.

## Many commands in one call
- `acks.sh batch FILE` (or `-` and a here-document): one command per line, as after `acks.sh`; each runs exactly as
  alone (own dice, logged rolls, refusals); the batch stops at the first refusal or error and says how many were not
  run; `--stop-on REGEX`, `--stop-on-judge` (stop at anything left to the Judge), `--keep-going`. Use it for a
  moment's rolls that do not depend on each other's results, a round's state changes, a town day's purchases. Never
  put a roll after a result that decides whether it happens.
- `python3 $S/play.py walk N --relight A,B` (turn by turn with rests and relights, stopping at anything that needs
  you), `play.py supplies`, `play.py bank --to <holder> --keep 150`, `play.py bank-balances --bank <holder>`,
  `play.py payout [payout options]` (the payout, and its rows into the Ledger note).
- Python helpers for a scripted fight import `jacks` and call `jacks.run(["attack", "a", "b"])` → (exit code, text):
  no process per call. A scripted loop must stop at an arriving encounter, a fallen character, or a JUDGE part.
  A fight of many: `act GROUP --tactic …`, `state order …`, `round-auto` (engine 7.19.1) instead of a driver; days of
  march: `play.py march`; a departure: `play.py depart`; the week's city block: `play.py city-week`; the month's end:
  `play.py month-end`.
- An ESCALATE line clears when the hole is closed in the engine or a script and the lesson's `triggered_since` is set
  to the session the enforcement starts (`enforced_by` says what closes it); the S47-S48 escalations (wage-days,
  surprise-members, npc-rolls-hidden, driver-loop-stop) were closed so in S55.
