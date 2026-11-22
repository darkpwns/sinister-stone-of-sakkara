# S12 helpers (source after s10_j.sh): slept (clear sleep_due/fatigue after an inn night), dawn (spells reset), innnight DAY N COST
slept(){ python3 - $PARTY <<'PY'
import json,sys
p='Campaign/exploration-state.json'; x=json.load(open(p)); m=x['travel']['members']; out=[]
for i in sys.argv[1:]:
    if i in m:
        if m[i].get('sleep_due') is not None or (m[i].get('cond') or {}).get('fatigued'): out.append(i)
        m[i]['sleep_due']=None; m[i].setdefault('cond',{})['fatigued']=0
json.dump(x,open(p,'w'),indent=1); print('slept (sleep_due/fatigue cleared):',' '.join(out) or 'none')
PY
}
dawn(){ for i in vestus-the-unlikely neris iulia phaedra; do $A actor set $i state.spells_used "[]" --cause "prayers/study day $1" 2>&1 | tail -1 | cut -c1-60; done; }
innnight(){ $A wait --hours ${4:-6} >/dev/null 2>&1; $A eat --in-town >/dev/null 2>&1; $A inv pay vettius ${3:-2gp4sp} --to "Silk Pony Inn (#25)" --cause "beds for ${2:-twelve}, night of day $1" 2>&1 | tail -1 | cut -c1-80; $A wait --hours ${5:-11} 2>&1 | tail -1 | sed 's/(src[^)]*)//g' | grep -o "day [0-9]* begins\|[a-z-]*: bed rest[^;]*\|[a-z-]* heals [0-9]* hp[^;]*\|wage[^;]*\|loyalty[^;]*\|FATIGUED[^;]*\|vagar[^;]*" | tr '\n' ';'; echo; }
