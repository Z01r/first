n=int(input())
q=input().split()
mx=0
kol=0
for i in q:
    mx=max(mx,int(i))
for t in q:
    kol+=(mx-int(t))
print(kol)
