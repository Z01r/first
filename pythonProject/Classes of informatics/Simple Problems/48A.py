n=int(input())
b=[]
kol=0
mx=kol
for i in range(n):
    a=int(input())
    b.append(a)
for u in range(len(b)):
    kol=b.count(b[u])
    mx=max(mx,kol)
print(mx)
