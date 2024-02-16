from math import gcd

a, b, x, y = map(int, input().split())
gcdxy = gcd(x, y)
while gcdxy > 1:
    x = x // gcdxy
    y = y // gcdxy
    gcdxy = gcd(x, y)
print(min(a // x, b // y))
