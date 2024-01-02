def yy(n):
    if n > 0:
        return 1
    else:
        return -1


n = int(input())
p = int(input())
s = 0
for i in range(1, n):
    u = int(input())
    l = yy(u)
    g = yy(p)
    if l == g and s == 0:
        s = i
    p = u
print(s)
