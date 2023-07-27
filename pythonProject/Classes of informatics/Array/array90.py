n=int(input())
k=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
del(a[k-1])
print(a)
