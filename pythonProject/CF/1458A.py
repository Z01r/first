import math

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
z = []
for j in range(m):
    k = b[j] + a[0]
    for i in range(1,len(a)):
        k = math.gcd(k,b[j]+a[i])
    z.append(k)
print(*z)