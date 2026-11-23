# travel helpers for the playtest Judge: source from the instance root
A="timeout 180 bash .claude/skills/acks2-judge/scripts/acks.sh"
WATCH="vettius,quintus-the-rager;aulus,zaira-the-beautiful;tarq,thorwell"
key(){ sed 's/ (src:.*//' | tail -1 | grep -oE "^day [0-9]+ [0-9:]+ -> day [0-9]+ [0-9:]+|[0-9.]+ h travel at [0-9]+ mi/day[^;]*|navigation[^;]*|LOST[^;]*|ENCOUNTER[^;]*|encounter at[^;]*|encounter enc[^;]*|loses [0-9]+ CON[^;]*|DIES[^;]*|DEHYDRATED|HUNGRY|FATIGUED[^;]*|party believes[^;]*|true hex[^;]*|partway[^;]*" | sort -u | tr '\n' '|'; echo; }
march(){ $A water 2>&1 | sed 's/ (src:.*//' | tail -1 | grep -oE "returns to[^(]*|no drinkable[^;]*|NOT ALLOWED.*" | head -1; $A travel "$@" 2>&1 | key; }
night(){ $A camp --watches "$WATCH" --hours 12 2>&1 | key; }
dusk(){ h=$(python3 -c "import json;x=json.load(open('Campaign/exploration-state.json'));r=x['clock']['round_of_day'];print(max(0,(1080-r//6*1)//60))" 2>/dev/null); }
