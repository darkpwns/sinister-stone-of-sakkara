#!/bin/bash
# S45: an Order strike in the streets: Vettius' hide and sneak throws (open), surprise (the engine's, a stand-in
# Bandit entry for the group's count), then a fight state with the members and the target's actor and companions.
# usage: s45_order.sh MEMBERS TARGET_ID "PERCEIVED" N_COMPANIONS [COMPANION_MONSTER]
A=.claude/skills/acks2-judge/scripts/acks.sh
M=$1; T=$2; P=$3; N=${4:-0}; CM=${5:-Bandit}
rm -f Campaign/combat-state.json
bash $A throw vettius --prof hiding 2>&1 | tail -1 | grep -o "Vettius.*\(SUCCESS\|FAIL\)" | cut -c1-80
bash $A throw vettius --prof sneaking 2>&1 | tail -1 | grep -o "Vettius.*\(SUCCESS\|FAIL\)" | cut -c1-80
bash $A encounter start --monster "$CM" --number $((N+1)) --replace >/dev/null 2>&1
bash $A encounter distance 20 >/dev/null 2>&1
bash $A encounter surprise --party fore,los --monsters none --hiding vettius --sneaking vettius --members $M 2>&1 | tail -1 | sed 's/ (src: [^)]*)//g' | grep -o "\[H\] monsters[^;]*\|SURPRISED" | sort | uniq -c | cut -c1-120
bash $A state init >/dev/null 2>&1
for m in ${M//,/ }; do bash $A state add $m --side party >/dev/null 2>&1; done
bash $A state add $T --side foe --group target --perceived "$P" 2>&1 | tail -1 | cut -c1-80
for i in $(seq 1 $N); do bash $A state add c$i --monster "$CM" --group companions --perceived "$P's companion $i" 2>&1 | tail -1 | cut -c1-60; done
