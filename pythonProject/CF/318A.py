n, k = map(int, input().split())
if n % 2 == 0:
    z = n // 2
else:
    z = (n // 2) + 1
if k > z:
    print(((k - z) * 2))
else:
    print((k * 2) - 1)
