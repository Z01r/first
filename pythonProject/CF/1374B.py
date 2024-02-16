t = int(input())
for i in range(t):
    n = int(input())
    q = 0
    w = 0
    while n % 2 == 0:
        n //= 2
        q += 1
    while n % 3 == 0:
        n //= 3
        w += 1
    if n == 1 and w >= q:
        print(2 * w - q)
    else:
        print(-1)
