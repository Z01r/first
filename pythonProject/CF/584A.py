n, t = map(int, input().split())
res = 0
s = (10 ** (n-1))
e = (10 ** n)
for i in range(s, e):
    if i % t == 0:
        print(i)
        exit()
print(-1)