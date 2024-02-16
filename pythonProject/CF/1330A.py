t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(set(a))
    b.sort()
    c = []
    for i in range(1, 202):
        if i not in b:
            c.append(i)
    if c[x] - c[x - 1] == 1:
        print(c[x - 1])
    else:
        print(c[x] - 1)
