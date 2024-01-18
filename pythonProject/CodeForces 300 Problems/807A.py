n = int(input())
c = []
d = []
w = 0
t = 0
p = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        w += 1
    c.append(a)
    d.append(b)
for x in c:
    p.append(x)
for u in d:
    y.append(u)
c.sort()
c.reverse()
d.sort()
d.reverse()
if (c != p) or (d != y):
    t += 1
if w > 0:
    print('rated')
elif t > 0:
    print('unrated')
else:
    print('maybe')
