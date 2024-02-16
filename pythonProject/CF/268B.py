n = int(input())
kol = n
for i in range(1, n):
    kol += (n - i) * i
print(kol)
