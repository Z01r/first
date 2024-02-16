t = int(input())
for _ in range(t):
    f = 0
    n, m = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c and m % 2 == 0:
            f = 1
    if f:
        print('YES')
    else:
        print('NO')
