t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    s=a+b
    m=c+d
    if s>1 and m>1:
        s=2
    elif s==0 and m==0:
        s=0
    elif s<2 or m<2:
        s=1
    print(s)
    
