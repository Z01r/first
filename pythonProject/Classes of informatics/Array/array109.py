n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
b=list()
for j in range(n):
    b.append(a[j])
    if a[j]<0:
        b.append(0)
print(b)
