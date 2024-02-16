s, n = map(int, input().split())
x = []
for _ in range(n):
    p, m = map(int, input().split())
    l = [p,m]
    x.append(l)
x.sort()
for i in x:
    if s > i[0]:
        s += i[1]
    else:
        print("NO")
        exit()
print("YES")