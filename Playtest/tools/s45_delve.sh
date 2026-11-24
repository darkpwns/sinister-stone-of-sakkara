#!/bin/bash
# S45: start a delve for the nine: adventure start NAME, join all, obedience, the sewer-caves site, lantern lit, auto relight.
# usage: bash Playtest/tools/s45_delve.sh "A### descent N: ..." [members]
A=.claude/skills/acks2-judge/scripts/acks.sh
M=${2:-vettius,vestus-the-unlikely,lucilla,cotta,brennus,neris,aelia,tiberius-maro,phaedra}
rm -f Campaign/combat-state.json
bash $A adventure start --name "$1" 2>&1 | tail -1 | cut -c1-80
for a in ${M//,/ }; do bash $A adventure join $a >/dev/null 2>&1; done
for h in aelia phaedra tiberius-maro; do echo ",$M," | grep -q ",$h," && bash $A obey $h --order "descend: $1" 2>&1 | tail -1 | grep -o "obedience [^:]*: [^;]*-> [^;]*" | cut -c1-120; done
bash $A location --site "Nethercity sewer caves" --hub "Adventure/SOTN/SOTN Hub.md" 2>&1 | tail -1 | cut -c1-60
bash $A light on --kind lantern --carrier vettius 2>&1 | tail -1 | cut -c1-60
bash $A light auto on --carriers vettius,aelia,phaedra >/dev/null 2>&1
