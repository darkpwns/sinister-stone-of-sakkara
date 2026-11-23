# S09 Judge helpers (source from the instance root): f, conds, cadd/crem (read-modify-write conditions), miasma (hourly +4 Death saves), clearmiasma, t (turn with auto-relight by $LC). Set PARTY to the current delvers.
# S09 Judge helpers: source from the instance root
A="bash .claude/skills/acks2-judge/scripts/acks.sh"
f(){ sed 's/ *(src[^)]*)//g;s/ | NOTE.*//' | cut -c1-${1:-400}; }
PARTY="lucilla vettius vestus-the-unlikely neris brennus iulia quirinus phaedra varro hrodvar aelia marcellus gnaeus"
MIASMA="sludge miasma (-1 to attack throws and damage)"
conds(){ python3 -c "import json,sys;d=json.load(open('Characters/'+sys.argv[1]+'.json'));print(json.dumps(d.get('state',{}).get('conditions',[])))" $1; }
cadd(){ # cadd ID "condition" "cause"
  local l=$(python3 -c "import json,sys;d=json.load(open('Characters/'+sys.argv[1]+'.json'));c=d.get('state',{}).get('conditions',[]) or [];c=c+[sys.argv[2]] if sys.argv[2] not in c else c;print(json.dumps(c))" "$1" "$2")
  $A actor set $1 state.conditions "$l" --cause "${3:-condition}" 2>&1 | tail -1 | cut -c1-160; }
crem(){ local l=$(python3 -c "import json,sys;d=json.load(open('Characters/'+sys.argv[1]+'.json'));c=[x for x in (d.get('state',{}).get('conditions',[]) or []) if x!=sys.argv[2]];print(json.dumps(c))" "$1" "$2")
  $A actor set $1 state.conditions "$l" --cause "${3:-condition ends}" 2>&1 | tail -1 | cut -c1-160; }
alive(){ for i in $PARTY; do python3 -c "import json,sys;d=json.load(open('Characters/'+sys.argv[1]+'.json'));import sys as s;s.exit(0 if (d.get('state',{}).get('hp',1) or 0)>0 else 1)" $i 2>/dev/null && echo $i; done; }
miasma(){ # hourly +4 Death saves (cloth over the face); failures gain the miasma condition
  for i in ${@:-$PARTY}; do o=$($A save $i death --mod 4 2>&1 | tail -1 | f 140); echo "$i: $o"
    if echo "$o" | grep -qi "fail"; then grep -q "sludge miasma" <<<"$(conds $i)" || cadd $i "$MIASMA" "failed the sludge miasma save (SOTN, Nethercity Features)" >/dev/null; fi; done; }
clearmiasma(){ for i in $PARTY; do grep -q "sludge miasma" <<<"$(conds $i)" && crem $i "$MIASMA" "a turn's rest away from the sludge" >/dev/null && echo "cleared $i"; done; }
t(){ $A turn "$@" 2>&1 | tail -1 | f 700; }
LC=phaedra
t(){ local o; o=$($A turn "$@" 2>&1 | tail -1); echo "$o" | f 400; if echo "$o" | grep -q "NONE LIT"; then $A light on --kind torch --carrier $LC 2>&1 | tail -1 | f 60; fi; }
