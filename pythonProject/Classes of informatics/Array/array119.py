n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=list()
d.append(a[0])
k=0
b.append(1)
c.append(a[0])
for l in range(1,n):
    if a[l]==a[l-1]:
        b[len(b)-1]+=1
        d.append(a[l])
    else:
        d.append(a[l-1])
        d.append(a[l])
        k+=1
        b.append(1)
        c.append(a[l])
f=d[len(d)-1]
d.append(f)
print(d)
