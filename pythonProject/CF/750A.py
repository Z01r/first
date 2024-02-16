n,k=map(int,input().split())
kolv=240-k
kolz=0
sch=0
while n>sch:
    sch+=1
    if kolv-(sch*5)>=0:
        kolz+=1
        kolv-=(sch*5)
    else:
        break
print(kolz)
