n=int(input())
a=0
b=0
c=''
d=[]
for i in range(n):
    g=input()
    a=int(g[0])
    b=int(g[2])
    c=g[1]
    if c=='+':
        d.append(a+b)
    else:
        d.append(a-b)
for k in range(len(d)):
    print(d[k])
