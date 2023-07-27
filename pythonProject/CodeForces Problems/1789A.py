from math import gcd as nod
n=int(input())
b=[]
for q in range(n):
    u=int(input())
    a = sorted(list(map(int, input().split())))
    s=[]
    for i in range(len(a)-1):
        for j in range(i+1,u):
            s+=[nod(a[i],a[j])]
    if min(s)<=2:
        b.append('yes')
    else:
        b.append('no')
for c in range(len(b)):
    print(b[c])
            
