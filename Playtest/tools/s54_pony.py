#!/usr/bin/env python3
"""S54 the night at the Silk Pony: steps ONE round in initiative order (round-next), acting for the combatant named.
Usage: python3 Playtest/tools/s54_pony.py ROUND   (round-start must already have been run for that round)
Plan state (gate, postern, who casts what) in Playtest/tools/s54_pony_state.json. Stops when a party member falls."""
import json, os, random, re, sys
sys.path.insert(0, '.claude/skills/acks2-judge/scripts')
import jacks
CTX = jacks.context()
ST = 'Playtest/tools/s54_pony_state.json'
P = json.load(open(ST)) if os.path.exists(ST) else {'gate': 0, 'postern': 0, 'fireballs': 2, 'bolts': 2}
R = int(sys.argv[1])
def run(*a):
    c, t = jacks.run([str(x) for x in a], CTX)
    return c, t
def cs():
    s = json.load(open('Campaign/combat-state.json')); c = s['combatants']
    return c if isinstance(c, dict) else {x['id']: x for x in c}
def alive(i, c=None):
    c = c or cs(); x = c.get(i)
    return x and (x.get('hp') or 0) > 0 and x.get('status', 'active') in ('active', None)
J = [f'brigand{i}' for i in range(1, 41)]; AX = J[:26]; XB = J[26:]
LANE = ['mordax'] + [f'thug{i}' for i in range(1, 14)] + [f'bravo{i}' for i in range(1, 4)]
KF = [f'kf{i}' for i in range(1, 7)]; KB = [f'kb{i}' for i in range(1, 7)]
log = []
def say(s): log.append(s); print(s[:260])
def first_alive(lst, c):
    for i in lst:
        if alive(i, c): return i
def area(caster, dice, targets, label):
    c, t = run('roll', f'{label}:{dice}'); say(t.strip())
    tot = int(re.search(r'= (\d+)\s*$', t.strip()).group(1))
    cc = cs()
    for i in targets:
        if not alive(i, cc): continue
        hp = cc[i]['hp']; dmg = tot
        if tot // 2 < hp:
            _, st = run('save', i, 'blast'); say(st.strip())
            if 'SUCCESS' in st: dmg = tot // 2
        _, o = run('state', 'set', i, f'hp={hp - dmg}'); say(f'  {i}: {dmg} -> hp {hp - dmg}')
while True:
    c, t = run('round-next'); line = t.strip().split('|')[0]
    if 'all combatants have acted' in t or c: say(line); break
    m = re.search(r'count (\d+): (.+?) acts', line)
    who = None
    cc = cs()
    # the engine names the combatant; find it by the turn pointer in the state
    s = json.load(open('Campaign/combat-state.json')); who = s['order'][s['count_index']]
    act = None
    if who is None or not alive(who, cc): say(f'{line}: (no act)'); continue
    if who == 'vestus-the-unlikely' and P.get('fb_round') == R and P['fireballs'] > 0:
        P['fireballs'] -= 1; say('Vestus: Fireball'); area(who, '8d6', P['fb_targets'], 'Vestus Fireball'); continue
    if who == 'phaedra' and P.get('tb_round') == R and P['bolts'] > 0:
        P['bolts'] -= 1; say('Phaedra: Thunderbolt'); area(who, '6d6', P['tb_targets'], 'Phaedra Thunderbolt'); continue
    if who in ('cotta', 'ennia-ursa') + tuple(KB):
        tgt = first_alive(LANE[1:] + LANE[:1], cc); act = ['attack', who, tgt] if tgt else None
    elif who in ('aelia',) + tuple(KF):
        tgt = first_alive(AX + XB, cc); act = ['attack', who, tgt] if tgt else None
    elif who == 'vettius' and P.get('vettius') and alive('mordax', cc):
        if P.get('vettius') == 'strike':
            run('state', 'distance', 'vettius', 'mordax', '5'); act = ['attack', 'vettius', 'mordax', '--rear']
            P['vettius'] = 'engaged'
        else:
            act = ['attack', 'vettius', 'mordax']
    elif who == 'vettius':
        tgt = first_alive(LANE, cc)
        if tgt:
            run('state', 'distance', 'vettius', tgt, '5'); act = ['attack', 'vettius', tgt, '--rear']
    elif who in XB:
        tgt = first_alive(random.sample(KF, len(KF)), cc); act = ['attack', who, tgt, '--cover', 'chest'] if tgt else None
    elif who in ('bravo1', 'bravo2', 'bravo3'):
        tgt = first_alive(['cotta', 'ennia-ursa'], cc); act = ['attack', who, tgt, '--cover', 'waist'] if tgt else None
    elif who in AX or who.startswith('thug') or who == 'mordax':
        say(f'{line}: hacks at the gate' if who in AX else f'{line}: batters the postern'); continue
    if act:
        c2, o = run(*act); say(f'{line}: ' + o.strip().split(' | ')[0])
    else:
        say(f'{line}: holds')
    cc = cs()
    for p in ('cotta','brennus','vettius','lucilla','neris','aelia','phaedra','ennia-ursa','vestus-the-unlikely'):
        if p in cc and (cc[p].get('hp') or 1) <= 0: say(f'STOP: {p} down'); json.dump(P, open(ST, 'w')); sys.exit(3)
json.dump(P, open(ST, 'w'))
open(f'Playtest/tools/s54_round{R}.log', 'w').write('\n'.join(log) + '\n')
