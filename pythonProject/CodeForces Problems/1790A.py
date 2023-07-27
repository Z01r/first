n=int(input())
p='314159265358979323846264338327'
kol=0
x=[]
flag=0
for i in range(n):
    g=input()
    kol=0
    flag=0
    for j in range(len(g)):
        if g[j]==p[j] and flag==0:
            kol+=1
        if g[j]!=p[j]:
            flag=1
    x.append(kol)
for t in range(len(x)):
    print(x[t])
