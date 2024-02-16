n=int(input())
e=[]
mx=0
mn=0
for i in range(n):
    a=int(input())
    v=input().split()
    mx=int(v[0])
    mn=int(v[0])
    for k in v:
        mx=max(mx,int(k))
        mn=min(mn,int(k))
    e.append(mx-mn)
for z in range(len(e)):
    print(e[z])
