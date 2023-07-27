m=int(input())
a=[[0 for i in range(m)]for j in range(m)]
b=list()
for i in range(m):
    a[i]=list(map(int,input().split()))
    b.append(sum(a[i])/len(a[i]))
kol=0
p=list()
for k in range(len(a)):
    for j in range(len(a[k])):
        if b[k]>a[k][j]:
            kol+=1
print(kol)