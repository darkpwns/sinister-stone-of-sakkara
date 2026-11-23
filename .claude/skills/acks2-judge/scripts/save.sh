#!/bin/bash
# save.sh "S## what changed" : snapshot, commit everything, push. Run after every state write.
# Refuses to commit if snapshot.py refuses. Push: pull --rebase then push; on failure retry once,
# then print PUSH FAILED (tell the user). Never force-pushes. "S## end ..." also archives the actors' change logs,
# compacts the exploration state (acks compact) and rewrites the handoff (handoff.py).
D="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"; R="${JUDGE_REPO:-$(cd "$D/../../../.." && pwd)}"
[ -n "$1" ] || { echo "usage: save.sh \"S## message\""; exit 1; }
for ES in "$R/Campaign/exploration-state.json" "$R/Campaign/retinue-state.json" "$R/Campaign/adventure-state.json" "$R/Campaign/inventory-state.json"; do   # engine state (Judge only): must be readable before it is committed
  if [ -f "$ES" ] && ! python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$ES" 2>/dev/null; then echo "NOT SAVED: $ES is not valid JSON"; exit 2; fi
done
if [[ "$1" =~ ^S[0-9]+\ end ]]; then   # between sessions: each actor's change log moves to tools.actor_changes (engine 7.5.0)
  ALL=$(python3 -c "import sys; sys.path.insert(0,'$D'); import jlib; c=jlib.config(); print(' '.join(jlib.actor_id(f) for d in jlib.actor_dirs(c) for f in jlib.actor_files(d)))")
  CD=$(python3 -c "import sys; sys.path.insert(0,'$D'); import jlib; print(jlib.path(jlib.config().get('tools', {}).get('actor_changes', 'Campaign/actor-changes/')))")
  if [ -n "$ALL" ]; then AR=$(bash "$D/acks.sh" actor archive $ALL --out "$CD" 2>&1) || { echo "NOT SAVED: actor archive failed: $AR"; exit 2; }; echo "$AR" | cut -c1-200; fi
fi
IDS=$(python3 -c "import sys; sys.path.insert(0,'$D'); import jlib; c=jlib.config(); print(' '.join(jlib.actor_id(f) for d in jlib.actor_dirs(c) for f in jlib.actor_files(d)))")
if [ -n "$IDS" ]; then   # engine 7.x: every actor file must pass the schema and its checks before it is committed
  AC=$(bash "$D/acks.sh" actor check $IDS --json 2>&1) || { echo "NOT SAVED: actor check failed:"; echo "$AC" | python3 -c "import json,sys
try: print('\n'.join(p['text'] for p in json.load(sys.stdin)['parts'] if not p['text'].endswith(': passed')))
except Exception: print(sys.stdin.read())" | head -20; exit 2; }
fi
if [ -f "$R/Campaign/inventory-state.json" ]; then   # engine stage 6: nothing is saved while the inventory and the actors disagree
  IC=$(bash "$D/acks.sh" inv check 2>&1) || { echo "NOT SAVED: $IC"; echo "fix: record the missing event (acks.sh inv add/remove/give/...)"; exit 2; }
  python3 "$D/ledger_sync.py" || { echo "NOT SAVED: Ledger purchases and sales could not be written"; exit 2; }
fi
# Judge memory (engine 7.16.0): the lessons index and the schedule must be readable; lessons to escalate are printed.
if [ -f "$R/Campaign/lessons.yaml" ]; then LC=$(bash "$D/acks.sh" lesson check 2>&1) || { echo "NOT SAVED: Campaign/lessons.yaml: $LC"; exit 2; }; echo "$LC" | grep -o "ESCALATE[^/|]*" | head -5; fi
if [ -f "$R/Campaign/schedule.yaml" ]; then SC=$(bash "$D/acks.sh" schedule check 2>&1) || { echo "NOT SAVED: Campaign/schedule.yaml: $SC"; exit 2; }; fi
if [[ "$1" =~ ^S[0-9]+\ end ]]; then   # session end: old day ledgers, events and burnt-out lights to the archive; the handoff rewritten
  bash "$D/acks.sh" compact 2>&1 | cut -c1-200
  python3 "$D/handoff.py" || echo "handoff not written"
fi
python3 "$D/check_overlay.py" || { echo "NOT SAVED: class-overlays.yaml refused (overlay check)"; exit 2; }   # S5
python3 "$D/xsync.py"   # actors' state -> public.party (D7); engine exploration state -> public.time, light, weather, believed hex, trail, rations (open values only)
python3 "$D/snapshot.py" || { echo "NOT SAVED: snapshot refused; fix the state, then save again"; exit 2; }
cd "$R" || exit 1
git add -A
if git diff --cached --quiet; then echo "nothing to commit"; else
  git commit -q -F - <<EOF || { echo "commit failed"; exit 1; }
$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
fi
B=$(git branch --show-current)
for try in 1 2; do
  if git pull -q --rebase origin "$B" 2>/dev/null && git -c push.negotiate=true push -q origin "HEAD:$B" 2>/tmp/judge_push.err; then
    git fetch -q origin "$B:refs/remotes/origin/$B" 2>/dev/null || true
    echo "saved and pushed: $(git log --oneline -1)"; exit 0
  fi
  [ $try = 1 ] && sleep 3
done
echo "PUSH FAILED (local commit kept): $(tail -2 /tmp/judge_push.err)"; exit 3
