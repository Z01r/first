a=[]
n=int(input())
for i in range(n):
    m=int(input())
    a.append(m)
b=[]
c=[]
for j in range((n//2)):
    b.append(a[j])
for z in range(n//2,n):
    c.append(a[z])
print(c+b)
