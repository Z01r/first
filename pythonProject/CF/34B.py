n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 0
p = [0]
for i in range(0, m):
    s += a[i] * (-1)
    p.append(s)
print(max(p))
