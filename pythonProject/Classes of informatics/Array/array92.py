n=int(input())
a=list()
b=list()
for i in range(n):
    a.append(int(input()))
for j in range(n):
    if a[j]%2==0:
        b.append(a[j])
print(len(b))
print(b)
