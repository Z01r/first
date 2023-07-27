n=int(input())
a=[]
b=[]
for i in range(n):
    s=int(input())
    a.append(s)
for u in range(n):
    b.append(int(input()))
c=[]
for x in range(n):
    mx=max(a[x],b[x])
    c.append(mx)
print(c)
