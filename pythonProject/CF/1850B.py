n = int(input())
u = []
for i in range(n):
    p = int(input())
    z = []
    g = []
    f = []
    d = []
    for w in range(1, p + 1):
        a, b = map(int, input().split())
        z.append(a)
        g.append(b)
    for c in range(len(z)):
        if z[c] <= 10:
            f.append(z[c])
            d.append(g[c])
    u.append(g.index(max(d)))
for y in u:
    print(y+1)
