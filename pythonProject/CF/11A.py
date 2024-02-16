n, d = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(1, len(a)):
    if a[i - 1] >= a[i]:
        res += (a[i - 1] - a[i]) // d + 1
        a[i] += d * ((a[i - 1] - a[i]) // d + 1)
print(res)
