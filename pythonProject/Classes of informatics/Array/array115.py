n=int(input())
a=list()
b=list()
for z in range(n):
    a.append(int(input()))
    b.append(z)
for m in range(n+1):
    for v in range(m+1,n):
        if a[b[m]]>a[v]:
            a[b[m]],a[v]=a[v],a[b[m]]
            b[m],b[v]=b[v],b[m]
print(b)
