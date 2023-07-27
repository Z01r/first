a=int(input())
d=[]
z=[]
for i in range(a):
    s=int(input())
    d.append(s)
for t in range(len(d)):
    q=d.count(d[t])
    if q>1:
        z.append(d[t])
d=set(d)
z=set(z)
w=len(d)-len(z)
print(w)
