a=[]
n=int(input())
b=[]
k=int(input())
l=int(input())
for i in range(n):
    m=int(input())
    a.append(m)
i1=k-1
i2=l-1
for j in range(n):
    if (j>=i1 and j<=i2) or (j>=i2 and j<=i1):
        b.append(a[j])
b.reverse()
c=[]
if i1>i2:
    for l in range(i2):
        c.append(a[l])
    for z in range(len(b)):
        c.append(b[z])
    for x in range(i1+1,n):
        c.append(a[x])
elif i1<i2:
    for l in range(i1):
        c.append(a[l])
    for z in range(len(b)):
        c.append(b[z])
    for x in range(i2+1,n):
        c.append(a[x])
print(c)
