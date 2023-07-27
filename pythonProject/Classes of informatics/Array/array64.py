nA=int(input())
nB=int(input())
nC=int(input())
a=[]
b=[]
c=[]
d=[]
for i in range(nA):
    v=int(input())
    a.append(v)
    d.append(v)
for j in range(nB):
    l=int(input())
    b.append(l)
    d.append(l)
for p in range(nC):
    m=int(input())
    c.append(m)
    d.append(m)
d.sort()
d.reverse()
print(d)
