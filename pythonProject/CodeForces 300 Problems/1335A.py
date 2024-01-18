n=int(input())
a=[]
for u in range(n):
    kol=0
    k=int(input())
    if k%2==0:
        kol=(k//2)-1
    else:
        kol=(k//2)
    a.append(kol)
for i in a:
    print(i)
