q = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = []
    u = q[:k]
    s = u
    for j in range(k, n):
        s += u[j % k]
    print(s)
