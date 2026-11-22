"""Guildhouse member balances from the inventory log (S19). Usage: python3 Playtest/tools/gh_balances.py [DAY]
Each event touching holder guildhouse-bank is attributed to a member: the other coin holder of a give, else the
first actor id named in the cause. Prints balances in gp and checks they reconcile with the bank's coins."""
import json, sys, re
x = json.load(open('Campaign/inventory-state.json'))
upto = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
V = {'pp': 5.0, 'gp': 1.0, 'ep': 0.5, 'sp': 0.1, 'cp': 0.01}
val = lambda c: sum(V[k] * c.get(k, 0) for k in V)
ids = sorted(x['holders'].keys(), key=len, reverse=True)
bal, unk, tot = {}, [], 0.0
for e in x['log']:
    if (e.get('day') or 0) > upto: continue
    cs = e.get('coins', [])
    g = [c for c in cs if c.get('who') == 'guildhouse-bank']
    if not g: continue
    d = sum(val(c) for c in g); tot += d
    others = [c['who'] for c in cs if c.get('who') != 'guildhouse-bank']
    who = others[0] if others else None
    if not who:
        cause = e.get('cause', '')
        m = [i for i in ids if re.search(r'\b' + re.escape(i) + r'\b', cause, re.I)] or (['vestus-the-unlikely'] if re.search(r'\bVestus\b', cause) else [])
        who = m[0] if m else None
    if who is None: unk.append((e.get('n'), d, e.get('cause', '')[:80])); continue
    bal[who] = bal.get(who, 0) + d
for k, v in sorted(bal.items()):
    if abs(v) > 0.005: print(f"{k}: {v:,.2f}")
print('sum', round(sum(bal.values()), 2), 'bank', round(tot, 2), 'unattributed', unk)
