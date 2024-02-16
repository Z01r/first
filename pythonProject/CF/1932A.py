t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = 0
    for i in range(1, len(a)):
        s += a[i-1] - a[i]
    print(-s)