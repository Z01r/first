n=int(input())
a=list()
k=int(input());k-=1
m=int(input())
for i in range(n):
    a.append(int(input()))
b=list()
for j in range(n):
    if j==k:
        for l in range(m):
            b.append(0)
        b.append(a[j])
    else:
        b.append(a[j])
print(b)
