a=input().split()
b=input().split()
c=input().split()
d=input().split()
e=input().split()
ind1=0
ind2=0
for i in range(len(a)):
    if a[i]=='1':
        ind1=0
        ind2=i
for j in range(len(b)):
    if b[j]=='1':
        ind1=1
        ind2=j
for z in range(len(c)):
    if c[z]=='1':
        ind1=2
        ind2=z
for y in range(len(d)):
    if d[y]=='1':
        ind1=3
        ind2=y
for x in range(len(e)):
    if e[x]=='1':
        ind1=4
        ind2=x
ind1=abs(2-ind1)
ind2=abs(2-ind2)
print(ind1+ind2)
        
