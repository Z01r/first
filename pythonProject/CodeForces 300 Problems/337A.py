n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
mn = 100000000001
for i in range(m - n+1):
    mn = min(mn, a[i + n - 1] - a[i])
print(mn)
