a = []
n = int(input())
b = []
for i in range(n):
    m = int(input())
    a.append(m)
i1 = a.index(max(a))
i2 = a.index(min(a))
for j in range(n):
    if (i1 < j < i2) or (i2 < j < i1):
        b.append(a[j])
b.reverse()
c = []
if i1 > i2:
    for l in range(i2 + 1):
        c.append(a[l])
    for z in range(len(b)):
        c.append(b[z])
    for x in range(i1, n):
        c.append(a[x])
elif i1 < i2:
    for l in range(i1 + 1):
        c.append(a[l])
    for z in range(len(b)):
        c.append(b[z])
    for x in range(i2, n):
        c.append(a[x])
print(c)
