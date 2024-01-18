t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    y = input()
    l = []
    p = []
    for i in x:
        l.append(int(i))
    for j in y:
        p.append(int(j))
    print((sum(l)+sum(p)) - min(sum(l),sum(p)))