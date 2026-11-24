#!/usr/bin/env python3
"""S54 the crypt stair battle (Ruined Monastery R3): one round in initiative order. Usage: s54_crypt.py ROUND
The party holds the landing at the stair foot (a 10' passage: two abreast, Brennus and Lucilla in front)."""
import json, random, re, sys
sys.path.insert(0, '.claude/skills/acks2-judge/scripts')
import jacks
CTX = jacks.context()
ST = 'Playtest/tools/s54_crypt_state.json'; P = json.load(open(ST)); R = int(sys.argv[1])
def run(*a): return jacks.run([str(x) for x in a], CTX)
def S(): return json.load(open('Campaign/combat-state.json'))
def cs():
    c = S()['combatants']; return c if isinstance(c, dict) else {x['id']: x for x in c}
def alive(i, c): x = c.get(i); return bool(x) and (x.get('hp') or 0) > 0 and x.get('status', 'active') == 'active'
def dist(a, b):
    d = S().get('distances') or {}
    for k in (f'{a}|{b}', f'{b}|{a}'):
        if k in d: return d[k]
    for k, v in d.items():
        if a in k and b in k: return v
    return None
PARTY = ['cotta','brennus','vettius','lucilla','neris','aelia','phaedra','ennia-ursa','vestus-the-unlikely']
FRONT = ['brennus', 'lucilla']
for i in P.get('returns', {}).get(str(R), []): run('state', 'return', i)
def area(dice, targets, label):
    c, t = run('roll', f'{label}:{dice}'); print(t.strip()[:110])
    tot = int(re.search(r'= (\d+)\s*$', t.strip()).group(1)); cc = cs()
    for i in targets:
        if not alive(i, cc): continue
        hp = cc[i]['hp']; dmg = tot
        if tot // 2 < hp:
            _, st = run('save', i, 'blast')
            if 'SUCCESS' in st: dmg = tot // 2
        run('state', 'set', i, f'hp={hp - dmg}'); print(f'  {i}: {dmg} -> {hp - dmg}')
def foes(c): return [i for i, x in c.items() if x.get('side') == 'foe' and alive(i, c)]
while True:
    c, t = run('round-next'); line = t.strip().split('|')[0]
    if c or 'all combatants have acted' in t: print(line[:100]); break
    s = S(); who = s['order'][s['count_index']]; cc = cs()
    if not alive(who, cc): continue
    sp = P.get('spells', {}).get(f'{R}:{who}')
    if sp:
        tg = sp['targets'] if sp['targets'] != 'nearest' else sorted([f for f in foes(cc)], key=lambda f: dist(f, 'brennus') or 999)[:sp.get('n', 8)]
        print(f'{who}: {sp["label"]}'); area(sp['dice'], tg, sp['label']); continue
    act = None
    if who in FRONT:
        near = [f for f in foes(cc) if (dist(f, who) or 99) <= 5]
        if near: act = ['attack', who, near[0]]
    elif who in ('cotta', 'aelia', 'ennia-ursa'):
        cand = sorted([f for f in foes(cc) if (dist(f, who) or 99) > 5], key=lambda f: dist(f, who) or 999)
        for f in cand[:3]:
            c2, o = run('attack', who, f)
            if c2 == 0: print(f'{line}: ' + o.strip().split(' | ')[0][:170]); break
        continue
    elif who == 'neris' and P.get('cure') == R:
        c2, o = run('roll', 'Neris Cure Light Injury on Vettius:1d6+1'); print(o.strip()[:100])
        v = cs()['vettius']['hp'] + int(re.search(r'= (\d+)\s*$', o.strip()).group(1)); run('state', 'set', 'vettius', f'hp={min(v, 34)}'); continue
    elif cc[who].get('side') == 'foe':
        d = min([dist(who, p) or 99 for p in FRONT])
        if d > 40:
            nd = max(5, d - 120)
            for p in PARTY: run('state', 'distance', who, p, str(nd if p in FRONT else nd + 10))
            print(f'{line}: runs in ({nd}\')'); continue
        busy = [f for f in foes(cc) if f != who and (dist(f, 'brennus') or 99) <= 5]
        tgt = random.choice(FRONT) if len(busy) < 4 else None
        if tgt and alive(tgt, cc):
            for p in PARTY: run('state', 'distance', who, p, '5' if p == tgt else '10')
            act = ['attack', who, tgt]
        else:
            for p in PARTY: run('state', 'distance', who, p, '10' if p in FRONT else '15')
            print(f'{line}: presses behind'); continue
    if act:
        c2, o = run(*act); print(f'{line}: ' + o.strip().split(' | ')[0][:170])
    cc = cs()
    down = [p for p in PARTY if p in cc and (cc[p].get('hp') or 1) <= 0]
    if down: print('STOP: down', down); json.dump(P, open(ST, 'w')); sys.exit(3)
json.dump(P, open(ST, 'w'))
