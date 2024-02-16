t = int(input())
m = []
for q in range(t):
    x, y, n = map(int, input().split())
    k = 0
    if y <= n % x:
        k = n - (n % x) + y
    elif n + y >= x + (n % x):
        k = n - (n % x) - x + y
    m.append(k)
for i in m:
    print(i)
