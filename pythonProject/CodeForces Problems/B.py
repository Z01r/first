n=int(input())
o=''
kol=0
if n%2==0:
    kol=n//2
    for i in range(kol):
        o=str(o)+'2 '
elif n%2!=0:
    kol=(n-1)//2
    for j in range(kol-1):
        o+='2 '
    o+='3'
print(kol)
print(o)
