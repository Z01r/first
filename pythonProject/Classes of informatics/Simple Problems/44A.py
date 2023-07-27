n=int(input())
a=[]
d=[]
n1=0
n2=0
for i in range(n):
    s=int(input())
    a.append(s)
q=a
a=set(a)
for t in range(len(a)):
    if a[t]!=q[t]:
        d.append(q[t])
for h in range(1,len(a)+1):
    if a[h] in d and n1==0:
        n1=h
    if a[h] in d and n1!=0 and n2==0:
        n2=h
print(n1,n2)
