a=list()
n=int(input())
for i in range(n):
    a.append(int(input()))
for j in range(n):
    for l in range(j+1,n):
        if a[j]>a[l]:
            a[j],a[l]=a[l],a[j]
print(a)
