n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
b=list()
for j in range(n):
    if a[j]>0:
        b.append(0)
        b.append(a[j])
    else:
        b.append(a[j])
print(b)
