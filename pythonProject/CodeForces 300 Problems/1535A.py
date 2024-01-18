n = int(input())
mx1 = 0
mx2 = 0
mx3 = 0
mx4 = 0
z = []
for j in range(1, n + 1):
    a, b, c, d = map(int, input().split())
    mx1 = max(a, b)
    mx2 = max(c, d)
    mx3 = max(mx1, mx2)
    mx4 = max(((a + b) - mx1), ((c + d) - mx2))
    if ((mx1 + mx2) - mx3) < mx4:
        z.append('NO')
    if ((mx1 + mx2) - mx3) > mx4:
        z.append('YES')
for i in z:
    print(i)
