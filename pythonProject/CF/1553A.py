t=int(input())
kol=0
for i in range(t):
    n=int(input())
    summ=0
    summ=2
    for y in range(1,n+1):
        r=str(y)
        for g in r:
            summ+=int(g)
