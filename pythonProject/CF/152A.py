n, m = map(int, input().split())
a = []
l = [0] * m
for i in range(n):
    a.append(input())
    for j in range(m):
        l[j] = max(l[j], int(a[-1][j]))
kol = 0
for i in a:
    for j in range(m):
        if int(i[j]) == l[j]:
            kol += 1
            break
print(kol)
