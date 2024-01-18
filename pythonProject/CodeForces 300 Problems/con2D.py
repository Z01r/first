t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    ans = ''
    w = 0
    if n >= d:
        ans = 'YES'
    else:
        if (1 + (d / (1 + 1)) % 1) != 0:
            w = int(1 + (d / 2)) + 1
        else:
            w = int(1 + (d / 2))
    if w <= n:
        ans = 'YES'
    elif w > n:
        ans = 'NO'
    print(ans)
