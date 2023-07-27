n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    g=int(input())
    a.append(g)
    if i%2==0:
        b.append(g)
    else:
        c.append(g)
c.reverse()
for j in range(len(b)):
    print(b[j])
for z in range(len(c)):
    print(c[z])
