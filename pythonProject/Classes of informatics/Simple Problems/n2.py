def ND(n):
    a = list()
    sch = 1
    while sch <= n:
        if n % sch == 0:
            a.append(sch)
        sch += 1
    return *a,'k=',len(a)


for i in range(10,31):
    print(i,':',ND(i))