n = int(input())
a = str(input())
b = str(input())
kol = 0
for i in range(n):
    q = int(a[i])
    p = int(b[i])
    c = min(q, p)
    k = max(q, p)
    kol += min(abs(p - q), 10 + c - k)
print(kol)
