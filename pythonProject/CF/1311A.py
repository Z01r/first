n=int(input())
a=0
b=0
res=0
s=[]
for i in range(1,n+1):
    h=input().split()
    a=int(h[0])
    b=int(h[1])
    if a<b:
        if (b-a)%2!=0:
            res=1
        if (b-a)%2==0:
            res=2
    if a>b:
        if (a-b)%2==0:
            res=1
        if (a-b)%2!=0:
            res=2
    s.append(res)
    res=0
for h in range(0,n):
    print(s[h])
