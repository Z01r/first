n=int(input())
a=[]
mn=0
mx=0
s=0
k=0
for i in range(n):
    h=input().split()
    mx=int(h[0])
    mn=int(h[0])
    s=0
    k=0
    for j in h:
       mx=max(mx,int(j))
       mn=min(mn,int(j))
       s+=int(j)
    k=s-(mn+mx)
    a.append(k)
for u in range(len(a)):
    print(a[u])
