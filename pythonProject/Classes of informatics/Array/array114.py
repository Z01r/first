a=list()
n=int(input())
for t in range(n):
    a.append(int(input()))
k=1
while k<n:
    i=k
    while i>0 and a[i-1]>a[i]:
        a[i-1],a[i]=a[i],a[i-1]
        i-=1
    k+=1
print(a)
