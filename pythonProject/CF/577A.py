n, x = map(int, input().split())
kol = 0
for i in range(1, n + 1):
    if x % i == 0 and x / i <= n:
        kol += 1
print(kol)
