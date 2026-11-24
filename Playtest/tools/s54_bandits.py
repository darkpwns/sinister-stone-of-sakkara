#!/usr/bin/env python3
"""S54 the bandits of 20.07 on the labour column: one round in initiative order. Usage: s54_bandits.py ROUND"""
import json, os, random, re, sys
sys.path.insert(0, '.claude/skills/acks2-judge/scripts')
import jacks
CTX = jacks.context()
ST = 'Playtest/tools/s54_bandits_state.json'
P = json.load(open(ST))
R = int(sys.argv[1])
def run(*a): return jacks.run([str(x) for x in a], CTX)
def cs():
    c = json.load(open('Campaign/combat-state.json'))['combatants']
    return c if isinstance(c, dict) else {x['id']: x for x in c}
def alive(i, c): x = c.get(i); return x and (x.get('hp') or 0) > 0 and x.get('status', 'active') == 'active' and not any(k['name'] in ('unconscious',) for k in x.get('conditions') or [])
B = [f'bandit{i}' for i in range(1, 30)]
PARTY = ['cotta','brennus','vettius','lucilla','neris','aelia','phaedra','ennia-ursa','vestus-the-unlikely']
def first(lst, c):
    for i in lst:
        if alive(i, c): return i
def area(dice, targets, label):
    c, t = run('roll', f'{label}:{dice}'); print(t.strip()[:120])
    tot = int(re.search(r'= (\d+)\s*$', t.strip()).group(1)); cc = cs()
    for i in targets:
        if not alive(i, cc): continue
        hp = cc[i]['hp']; dmg = tot
        if tot // 2 < hp:
            _, st = run('save', i, 'blast')
            if 'SUCCESS' in st: dmg = tot // 2
        run('state', 'set', i, f'hp={hp - dmg}'); print(f'  {i}: {dmg} -> {hp - dmg}')
while True:
    c, t = run('round-next'); line = t.strip().split('|')[0]
    if c or 'all combatants have acted' in t: print(line); break
    s = json.load(open('Campaign/combat-state.json')); who = s['order'][s['count_index']]; cc = cs()
    if not alive(who, cc): continue
    act = None
    if who == 'vestus-the-unlikely' and P.get('fb') == R: area('8d6', P['fb_t'], 'Vestus Fireball'); continue
    if who == 'phaedra' and P.get('tb') == R: area('6d6', P['tb_t'], 'Phaedra Thunderbolt'); continue
    if who in ('aelia', 'cotta', 'ennia-ursa'):
        tg = first(B, cc); act = ['attack', who, tg, '--cover', 'waist'] if tg else None
    elif who in ('brennus', 'lucilla', 'vettius') and R >= P.get('melee_from', 2):
        tg = first(B[::-1] if who == 'vettius' else B, cc)
        if tg: run('state', 'distance', who, tg, '5'); act = ['attack', who, tg]
    elif who.startswith('bandit'):
        tg = random.choice([p for p in PARTY if alive(p, cc)])
        eng = [e for e in (s.get('engaged') or []) if who in e]
        act = ['attack', who, tg] if not eng else None
    if act:
        c2, o = run(*act); print(f'{line}: ' + o.strip().split(' | ')[0][:200])
    cc = cs()
    down = [p for p in PARTY if p in cc and (cc[p].get('hp') or 1) <= 0]
    if down: print('STOP: down', down); json.dump(P, open(ST, 'w')); sys.exit(3)
json.dump(P, open(ST, 'w'))
