# S23 helpers (s22_j.sh with the lit test fixed: it reads light show --json, any light lit with rounds left; the clock line never says NONE LIT)
# S22 helpers (source after s10_j.sh): sup [ids] (supplies), relight (first carrier in $TC with a torch), w N (walk N turns:
# rest when the next turn would pass 5 turns, relight on NONE LIT, stop on encounter/winded/expiry), bank (coin above 150gp to the Guildhouse)
TC="aelia marcellus lucilla hrodvar"
sup(){ for i in ${@:-lucilla vettius vestus-the-unlikely neris brennus iulia phaedra varro hrodvar aelia marcellus cotta}; do $A inv show $i --json 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)['data']; h=list(d['holdings'].values())[0] if d['holdings'] else {}
from collections import Counter; c=Counter()
for slot,its in h.items():
    for k,n in its.items():
        for key,lab in (('torch','torch'),('oil','oil'),('rations, iron','rat'),('holy water','holy')):
            if key in k.lower(): c[lab]+=n; break
co=list(d['coins'].values())[0] if d['coins'] else {}
print('$i',dict(c),int(co.get('gp',0)))"; done; }
relight(){ for c in $TC; do o=$($A light on --kind torch --carrier $c 2>&1 | tail -1); if ! echo "$o" | grep -q "NOT ALLOWED\|has no"; then echo "relit: $(echo "$o" | cut -c1-60)"; return; fi; done; echo "NO TORCH LEFT"; }
restn(){ $A clock 2>&1 | tail -1 | python3 -c "import sys,re;t=sys.stdin.read();m=re.search(r'rest: (\d+) turns?(?: (\d+) rounds?)?',t);n=re.search(r'rest: (\d+) rounds?',t);print(int(m.group(1))*10+int(m.group(2) or 0) if m else (int(n.group(1)) if n else 0))"; }
lit(){ $A light show --json 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin)['data'];sys.exit(0 if any(l['lit'] and l['rounds_left']>0 for l in d['lights']) else 1)" || relight; }
w(){ local n=${1:-1} i o; for ((i=1;i<=n;i++)); do lit
  if [ $(( $(restn) + 10 )) -gt 50 ]; then o=$($A rest 2>&1 | tail -1 | sed 's/ *(src[^)]*)//g'); echo "REST: $(echo "$o" | cut -c1-140)"; echo "$o" | grep -qi "ENCOUNTER" && { echo "-- stop (rest)"; return 1; }; lit; fi
  o=$($A turn 1 2>&1 | tail -1 | sed 's/ *(src[^)]*)//g'); echo "$o" | cut -c1-200
  echo "$o" | grep -qiE "ENCOUNTER|unconscious|dies|begins|expire" && { echo "-- stop after turn $i"; lit; return 1; }; done; lit; }
bank(){ for i in lucilla vettius vestus-the-unlikely neris brennus iulia phaedra varro hrodvar aelia marcellus cotta; do g=$($A inv show $i --json 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin)['data'];c=list(d['coins'].values())[0];print(int(c.get('gp',0)))"); [ $g -gt 150 ] && $A inv give $i guildhouse-bank $((g-150))gp --cause "$i banks coin above 150gp (day $1)" 2>&1 | tail -1 | cut -c1-60; done; }
