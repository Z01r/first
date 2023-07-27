n=int(input())
s=input().split()
a=[]
for u in s:
    a.append(int(u))
r=sum(a)
kol=0
for y in range(len(a)):
    if (r-a[y])%2==0:
        kol+=1
print(kol)
