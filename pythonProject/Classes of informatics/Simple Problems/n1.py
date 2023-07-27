n = int(input())
a = list()
sch = 1
while sch <= n:
    if n % sch == 0:
        a.append(sch)
    sch += 1
print('s=',*a,sep='+')
print('s=',*a,sep='*')