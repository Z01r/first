n, v = map(int, input().split())
k = 0
b = []
for i in range(n):
    a = list(map(int, input().split()))
    g = a.pop(0)
    if min(a) < v:
        k += 1
        b.append(i + 1)
print(k)
print(*b)
