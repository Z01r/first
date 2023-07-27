n=int(input())
a=list()
for i in range(n):
    k=int(input())
    a.append(k)
for j in range(0,n-1,2):
    a.remove(a[j])
print(a)
