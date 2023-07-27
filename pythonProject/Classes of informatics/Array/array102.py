n=int(input())
a=list()
k=int(input());k-=1
for i in range(n):
    a.append(int(input()))
b=list()
for j in range(n):
    b.append(a[j])
    if j==k:
        b.append(0)
print(b)
