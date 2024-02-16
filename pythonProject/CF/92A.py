n,m=map(int,input().split())
p=0
while 1!=2:
    for i in range(1,n+1):
        if m>=i:
            m-=i
        else:
            p=1
            break
    if p==1:
        break
print(m)
