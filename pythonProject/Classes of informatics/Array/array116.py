n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
k=0
b.append(1)
c.append(a[0])
for l in range(1,n):
    if a[l]==a[l-1]:
        b[len(b)-1]+=1
    else:
        k+=1
        b.append(1)
        c.append(a[l])
print(b,c)
