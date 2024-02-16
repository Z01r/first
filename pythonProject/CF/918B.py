n, m = map(int, input().split())
d = dict()
res = []
for _ in range(n):
    n, i = map(str, input().split())
    d[i] = n
for _ in range(m):
    c, p = map(str, input().split())
    l = c + ' ' + p + " " + '#' + str(d[p[:len(p)-1]])
    res.append(l)
for w in res:
    print(w)
