t = int(input())
a = list(map(int, input().split()))
a.append(a[0])
p = [1, 2]
mn = abs(a[0] - a[1])
for j in range(1, len(a) - 1):
    if mn > abs(a[j] - a[j + 1]):
        p.clear()
        p.append(j + 1)
        p.append(j + 2)
        mn = abs(a[j]-a[j+1])
v = []
for i in p:
    if i > t:
        v.append(i % t)
    else:
        v.append(i)
print(*v)
