n = int(input())
kol = 0
a = []
for i in range(1, n + 1):
    h, m = map(int, input().split())
    if h != 23:
        kol = (60 - m) + ((24 - h - 1) * 60)
        a.append(kol)
    if h == 23:
        kol = 60 - m
        a.append(kol)
for j in a:
    print(j)
