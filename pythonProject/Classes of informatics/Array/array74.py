a=[]
n=int(input())
b=[]
for i in range(n):
    m=int(input())
    a.append(m)
i1=a.index(max(a))
i2=a.index(min(a))
for j in range(n):
    if (j>i1 and j<i2) or (j>i2 and j<i1):
        b.append(0)
    else:
        b.append(a[j])
print(b)
