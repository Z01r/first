n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
for j in range(n):
    if a[j]%2==0:
        a.append(a[j])
print(a)
