t = int(input())
for j in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = a[0] - 1
    a[0] = 1
    for i in range(1, n):
        if a[i] - 1 > a[i - 1]:
            s += a[i] - a[i - 1] - 1
            a[i] = a[i - 1] + 1
    print(s)
