t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = 'YES'
    if not (a[0] % 2) and (1 in [b % 2 for b in a]):
        x = 'NO'
    print(x)
