#!/bin/bash
# acks.sh CMD [args] : the rules engine (acks2-tools, `acks`) with this campaign's files: roll log and session, engine
# rulings, the combat, exploration, retinue, adventure and inventory states, the hex adapter, the actor folders, the
# campaign's bestiary, item and table folders, aliases, the lessons index and the schedule (all from campaign.yaml).
# Which command gets which state: jacks.py `extra_for` (the table this script held until engine 7.16.0). The engine
# runs inside jacks.py's interpreter: one process per call.
#   acks.sh batch [FILE|-] [--keep-going] [--stop-on REGEX] [--stop-on-judge]   many commands, one process, one per
#   line as after `acks.sh`; stops at the first refusal. Python helpers: `import jacks; jacks.run([...])`.
D="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
[ -f "$HOME/acks_env.sh" ] && . "$HOME/acks_env.sh"
exec python3 "$D/jacks.py" "$@"
