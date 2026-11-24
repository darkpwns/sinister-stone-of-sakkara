#!/bin/bash
# S45: back in the city: settlement location, every lit light out, combat state removed.
A=.claude/skills/acks2-judge/scripts/acks.sh
rm -f Campaign/combat-state.json
bash $A light auto off >/dev/null 2>&1   # else every light put out is relit from the carriers' packs (S45 slip, days 616-619)
bash $A location --settlement Cyfaraun 2>&1 | tail -1 | cut -c1-60
for l in $(bash $A light show 2>&1 | grep -o "[a-z]*[0-9]* [a-z]* ([^)]*), [0-9]* turn" | awk '{print $1}'); do bash $A light off $l >/dev/null 2>&1; done
bash $A light show 2>&1 | grep -v " out" | head -3 | cut -c1-120
