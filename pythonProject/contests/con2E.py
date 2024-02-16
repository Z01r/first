n = int(input())
a = list(map(int, input().split()))
a.sort()
kol = 0
b = []
d = []
for i in range(len(a)):
    c = []
    if (len(c) < 2) and (a[i] not in c):
        c.append(a[i])
    c.sort()
    b.append(c)
for j in b:
    for h in j:
        d.append(h)
print(d)
