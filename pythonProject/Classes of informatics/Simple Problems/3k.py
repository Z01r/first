def isp(n):
    sch = 0
    kol = 0
    while sch <= n:
        sch += 1
        if n % sch == 0:
            kol += 1
    return kol


a = list()
for i in range(100, 1000):
    p = isp(i)
    if p == 2:
        a.append(i)
print(*a)
