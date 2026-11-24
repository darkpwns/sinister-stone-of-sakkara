#!/bin/bash
# S39: run up to N rounds with s38_trogs.py; party members it cannot act for hold (no action). Stops at a fallen
# party member or when no foe stands (lesson driver-loop-stop).
A=.claude/skills/acks2-judge/scripts/acks.sh
for r in $(seq 1 ${1:-3}); do
  bash $A round-start 2>&1 | tail -1 | grep -o "^round [0-9]*"
  while true; do
    o=$(python3 Playtest/tools/s38_trogs.py 2>&1 | grep -v "state set\|^NEXT: count [0-9]*: .* (cannot act\|is surprised)" | sed 's/ (src: [^)]*)//g' | cut -c1-200)
    echo "$o" | grep "^  \\$ attack" | grep -v " miss" | cut -c1-200
    echo "$o" | grep -q "FALLEN\|ALL FOES DOWN" && { echo "$o" | tail -2; exit 3; }
    echo "$o" | grep -q "all combatants have acted" && break
  done
  bash $A round-end 2>&1 | tail -1 | sed 's/ (src: [^)]*)//g' | grep -o "morale[^;]*" | cut -c1-120
done
