n=int(input())
kol=n
a=[]
q=0
for i in range(n):
    f=int(input())
    a.append(f)
for j in range(n):
    for d in range(j+1,n):
        if a[j]==a[d]:
            q=a.count(a[j])
            kol=kol-q
print(kol)
