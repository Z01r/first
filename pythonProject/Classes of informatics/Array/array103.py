n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
b=list()
i1=a.index(max(a))
i2=a.index(min(a))
for j in range(n):
    if j==i2:
        b.append(0)
        b.append(a[j])
    elif j==i1:
        b.append(a[j])
        b.append(0)
    else:
        b.append(a[j])
print(b)
