a=[]
n=int(input())
for i in range(n):
    m=int(input())
    a.append(m)
k=a[0]
e=a[1]
b=[]
b.append(k)
for j in range(2,n):
    if k>e and e<a[j]:
        b.append(e**2)
        k=e
        e=a[j]
    else:
        b.append(e)
        k=e
        e=a[j]
b.append(a[len(a)-1])
print(b)
