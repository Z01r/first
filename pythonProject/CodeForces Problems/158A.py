h=input().split()
g=input().split()
mx=int(h[1])-1
kol=0
for i in range(len(g)):
    if int(g[i])>=int(g[mx]) and int(g[i])>0:
        kol+=1
print(kol)
