a=[]
n=int(input())
b=[]
for i in range(n):
    m=int(input())
    a.append(m)
for k in range(n-1,-1,-1):
    b.append(a[k])
print(b)
