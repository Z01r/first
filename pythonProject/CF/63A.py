n = int(input())
a = []
b = []
res = []
r = []
chw = []
m = []
c = []
for i in range(n):
    s = input().split()
    a.append(s[0])
    b.append(s[1])
for d in range(len(b)):
    if b[d] == 'rat':
        r.append(a[d])
    elif (b[d] == 'child') or (b[d] == 'woman'):
        chw.append(a[d])
    elif b[d] == 'man':
        m.append(a[d])
    elif b[d] == 'captain':
        c.append(a[d])
for t in r:
    res.append(t)
for g in chw:
    res.append(g)
for u in m:
    res.append(u)
for l in c:
    res.append(l)
for y in res:
    print(y)