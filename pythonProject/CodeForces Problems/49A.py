#ಠ╭╮ಠ
#coded by ZK
s=list(input().split())
glas='a, e, i, o, u, y'
sogl='b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z'
k=s[len(s)-1]
k.lower()
if k=='?':
    k=s[len(s)-2]
u=k[len(k)-1]
if u=='?':
    k=k[:len(k)-1]
    u=k[len(k)-1]
r=k[len(k)-1]
r=r.lower()
if r in glas:
    print('YES')
if r in sogl:
    print('NO')

