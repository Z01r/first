n,k=map(int,input().split())
a=list(map(int,input().split()))
kol=0
for i in range(len(a)):
    if (a[i]+k)<=5:
        kol+=1
print(kol//3)
