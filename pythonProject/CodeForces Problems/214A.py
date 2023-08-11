n, m = map(int, input().split())
kol = 0
a, b = 0, 0
for i in range(1, n + 1):
    if i ** 2 <= n:
        b = n - (i ** 2)
        if i + (b ** 2) == m:
            kol += 1
if n == 1 and m == 1:
    kol = 2
print(kol)

