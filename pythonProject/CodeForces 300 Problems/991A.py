a, b, c, n = map(int, input().split())
a -= c
b -= c
if (a + b + c >= n) or (a < 0 or b < 0):
    print(-1)
    exit()
else:
    print(n - (a + b + c))
