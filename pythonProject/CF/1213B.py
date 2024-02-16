t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = a[n - 1]
    kol = 0
    for i in range(n - 2, -1, -1):
        kol += a[i] > mn
        mn = min(mn, a[i])
    print(kol)
