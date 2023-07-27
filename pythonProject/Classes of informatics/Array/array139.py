a=list()
b=list()
c=list()
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
x1=a[0]
y1=b[0]
for j in range(n):
    if a[j]>x1 or (a[j]==x1 and b[j]>y1):
        c.append(x1)
        c.append(y1)
        x1=a[j]
        y1=b[j]
    elif a[j]<x1 or (a[j]==x1 and b[j]<y1):
        c.append(a[j])
        c.append(b[j])
c.append(x1)
c.append(y1)
print(*c)
