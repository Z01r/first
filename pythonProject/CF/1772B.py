t = int(input())
u = []
for i in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if ((a < b) == (c < d)) and ((a<c) == (b<d)):
        u.append('YES')
    else:
        u.append('NO')
for z in u:
    print(z)
