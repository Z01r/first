s=input().split()
n=int(s[0])
h=int(s[1])
kol=0
g=input().split()
for i in g:
    if int(i)>h:
        kol+=2
    if int(i)<=h:
        kol+=1
print(kol)
