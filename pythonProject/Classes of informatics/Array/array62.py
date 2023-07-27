a=[]
b=[]
c=[]
n=int(input())
for i in range(n):
    k=int(input())
    a.append(k)
    if k>0:
        b.append(k)
    else:
        c.append(k)
print(len(b),b)
print(len(c),c)
