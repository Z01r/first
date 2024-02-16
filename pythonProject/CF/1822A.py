q=int(input())
for i in range(q):
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=(-1,-1)
    for i in range(n):
        if(a[i]+i<=t):
            s=max(s,(b[i],i+1))
    print(s[1])
