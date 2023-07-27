a=[]
n=int(input())
b=[]
flag=0
p=0
c=[]
for i in range(n):
    m=int(input())
    a.append(m)
    if m%2==1:
        c.append(m)
p=c[len(c)-1]
for k in range(n):
    if a[k]%2==1:
        b.append(a[k]+p)
print(b)
