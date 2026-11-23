# helpers for the playtest Judge
cd /home/user/sakkara-playtest
A="bash .claude/skills/acks2-judge/scripts/acks.sh"
acks(){ $A "$@"; }
t(){ o=$($A turn "$@" 2>&1 | tail -1); echo "$o" | sed 's/(src.*//' | cut -c1-260; if echo "$o" | grep -q "stopped: encounter"; then enc; fi; }
r(){ o=$($A rest 2>&1 | tail -1); echo "$o" | sed 's/(src.*//' | cut -c1-200; if echo "$o" | grep -q "stopped: encounter"; then enc; fi; }
enc(){ python3 -c "
import json;x=json.load(open('Campaign/exploration-state.json'));e=x.get('encounter') or {};print('ENC',{k:e.get(k) for k in ('id','monster_name','number','distance','status')})"; }
door(){ for i in 1 2 3 4 5 6; do o=$($A explore force-door aulus tarq --crowbar --door "$1" 2>&1 | tail -1); echo "$o" | grep -q FAIL || { echo "$o" | cut -c1-100; break; }; done; echo "door tries: $i"; }
loc(){ $A location --room "$1" | tail -1 | cut -c1-60; }
meet(){ $A encounter distance ${2:-30} >/dev/null 2>&1; $A encounter surprise --party los --monsters los 2>&1 | tail -1 | grep -o "SURPRISED" | head -1; $A reaction --tone ${1:-diplomatic} --face ${3:-lucilla} ${@:4} 2>&1 | tail -1 | grep -o "[A-Z][A-Z]*, [A-Z ]*\|NOT ALLOWED.*" | head -1; }
brawl(){ # brawl "perceived" front-csv rounds
  rm -f Campaign/combat-state.json; $A encounter fight --perceived "$1" >/dev/null 2>&1
  local plan=$(python3 -c "import json,sys;f=sys.argv[1].split(',');print(json.dumps({'plan':{x:'attack' for x in f},'front':f,'cap':2}))" "$2")
  for r in $(seq 1 ${3:-8}); do python3 /tmp/claude-0/-home-user/30a59327-4861-5a0c-baac-51205f2939e8/scratchpad/melee.py "$plan" | grep -o "[a-z0-9-]* -> [^:]*HIT.*hp [0-9-]* -> [0-9-]*\|unconscious\|morale [a-z-]*[^:]*: [0-9d+ ->\[\],=]*[A-Za-z ]*" | cut -c1-150
    left=$(python3 -c "
import json;s=json.load(open('Campaign/combat-state.json'));print(len([k for k,v in s['combatants'].items() if v['side']!='party' and v['hp']>0 and v.get('status','active')=='active']))"); [ "$left" = 0 ] && { echo "foes down after round $r"; break; }; done
  python3 -c "
import json;s=json.load(open('Campaign/combat-state.json'));print({k:v['hp'] for k,v in s['combatants'].items() if v['side']=='party'})"; }
FRONT=aulus,tarq,sabina,quintus-the-rager,zaira-the-beautiful,thorwell,thorcigar,gallus
walk(){ for room in "$@"; do $A location --room "$room" >/dev/null 2>&1; o=$($A turn 1 2>&1 | tail -1)
  if echo "$o" | grep -q "ENCOUNTER"; then $A turn 1 >/dev/null 2>&1; fi
  e=$(python3 -c "
import json;x=json.load(open('Campaign/exploration-state.json'));e=x.get('encounter') or {};print((e.get('status') or '')+'|'+(e.get('monster_name') or '')+'|'+str(e.get('number') or ''))")
  case "$e" in begun*) m=$(echo "$e" | cut -d'|' -f2); echo "[$room] $m x$(echo "$e" | cut -d'|' -f3)"
     $A encounter distance 30 >/dev/null 2>&1; $A encounter surprise --party los --monsters los >/dev/null 2>&1
     case "$m" in "Giant Rat"|"Stirge (Sakkara)"|Zombie|"Grave Ghoul"|Skeleton) brawl "$m" $FRONT 10 | tail -2; $A state end >/dev/null 2>&1; $A recover --monster "$m" --number $(echo "$e" | cut -d'|' -f3) >/dev/null 2>&1; rm -f Campaign/combat-state.json;;
       *) $A reaction --tone intimidating --face aulus 2>&1 | tail -1 | grep -o "[A-Z][A-Z]*, [A-Z ]*" | head -1;; esac
     $A encounter end >/dev/null 2>&1;;
  *) echo "[$room] -";; esac; done; }
