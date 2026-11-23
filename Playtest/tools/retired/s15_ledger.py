import sys,re
pay=open(sys.argv[1]).read()
L='Campaign/Ledger.md'; s=open(L).read()
secs={}
cur=None
for line in pay.splitlines():
    m=re.match(r'## (.+)',line)
    if m: cur=m.group(1).strip(); secs.setdefault(cur,[]); continue
    if cur and line.startswith('| '):
        secs[cur].append(re.sub(r' \(src:.*$','',line))
for name,rows in secs.items():
    if not rows: continue
    h='## '+name
    i=s.find(h)
    if i<0: print('no section',name); continue
    j=s.find('\n## ',i+1)
    if j<0: j=len(s)
    block=s[i:j].rstrip('\n')+'\n'+'\n'.join(rows)+'\n\n'
    s=s[:i]+block+s[j+1:] if j<len(s) else s[:i]+block
    print(name,len(rows))
open(L,'w').write(s)
