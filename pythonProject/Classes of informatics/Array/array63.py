a=[]
b=[]
c=[]
for i in range(5):
    l=int(input())
    a.append(l)
    c.append(l)
for j in range(5):
    m=int(input())
    b.append(m)
    c.append(m)
c.sort()
print(c)
