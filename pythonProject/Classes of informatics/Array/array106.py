n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
for j in range(0,n,2):
    a.append(a[j])
print(a)
