a = []
l, r = 0,0


def f(n):
    global l, r, a
    if n >= l:
        a.append(n)
    if n > r:
        return
    f((n * 10) + 4)
    f((n * 10) + 7)

l,r = map(int,input().split())
f(0)
lt = l - 1
kol = 0
a.sort()
for i in a:
    kol += max(0, min(i, r) - lt) * i
    lt = i
    if i >= r:
        break
print(kol)