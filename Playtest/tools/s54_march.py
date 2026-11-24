#!/usr/bin/env python3
"""S54 march with the labour column: N days along ROUTE at 4 hours of travel a day (the column's 12 miles; Rulings S54).
Each evening: feed and water (feed.sh), camp 12 h. Stops at any encounter, a CON loss, a missed wage or a lost member.
Usage: python3 Playtest/tools/s54_march.py DAYS HEX,HEX,..."""
import json, re, subprocess, sys
sys.path.insert(0, '.claude/skills/acks2-judge/scripts')
import jacks
CTX = jacks.context()
FEED = '/tmp/claude-0/-home-user/4ce086a7-1656-539c-ba33-f82689527569/scratchpad/feed.sh'
def run(*a):
    return jacks.run([str(x) for x in a], CTX)
def xs(): return json.load(open('Campaign/exploration-state.json'))
route = sys.argv[2].split(',')
STOP = re.compile(r'ENCOUNTER|encounter enc|CON|DEHYDRAT|STARV|missed|LOST|not paid|loyalty|dies|dead', re.I)
for d in range(int(sys.argv[1])):
    x = xs(); hx = x['travel']['hex']
    if hx in route: route = route[route.index(hx) + 1:]
    if not route: print('arrived', hx); break
    day = x['clock']['day']; hr = x['clock']['round_of_day'] // 60
    used = 0
    c, t = run('travel', '--route', ','.join(route), '--hours', '4')
    print(f'day {day}: ' + t.strip().split(' | ')[0][:400])
    if c: print('STOP: refusal'); break
    if 'encounter enc' in t or 'ENCOUNTER (' in t:
        if re.search(r'Herd Animal|Commoner|Merchant|Pilgrim', t) and 'IN LAIR' not in t:
            run('encounter', 'end'); print('  (benign: passed by)')
            c, t = run('travel', '--route', ','.join([r for r in route if r != xs()['travel']['hex']]), '--hours', '4')
            print('   ' + t.strip().split(' | ')[0][:300])
            if 'encounter enc' in t or 'ENCOUNTER (' in t: print('STOP: encounter'); break
        else:
            print('STOP: encounter'); break
    x = xs(); hx = x['travel']['hex']; hr = x['clock']['round_of_day'] // 60
    if hr < 18: run('wait', '--hours', str(18 - hr))
    subprocess.run(['bash', FEED, str(day + 1), hx], capture_output=True, text=True)
    c, t = run('camp', '--hours', '12', '--watches', 'vettius,cotta;ennia-ursa,brennus;lucilla,aelia;neris,phaedra')
    bad = [l for l in t.replace(';', '\n').split('\n') if STOP.search(l) and 'none' not in l and 'Endurance' not in l and 'encounter throw' not in l and 'night encounters' not in l]
    print('  night: ' + ' / '.join(b.strip()[:160] for b in bad[:4]))
    if any(re.search(r'ENCOUNTER|encounter enc|CON|missed|LOST|dies', b) for b in bad): print('STOP: night'); break
