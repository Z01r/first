from math import lcm

a = []
t = int(input())
for q in range(t):
    l, r = map(int, input().split())
    p = [-1, -1]
    for x in range(l, r + 1):
        for y in range(x + 1, r + 1):
            if l <= lcm(x, y) <= r:
                p[0] = x
                p[1] = y
                break
    a.append(p)

for c in a:
    print(*c)
