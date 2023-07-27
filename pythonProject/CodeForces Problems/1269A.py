c=int(input())
for i in range(1,1000000001):
    flag=0
    s=c+i
    flag2=0
    for u in range(1,s+1):
        if s%u==0 and u!=s and u!=1:
            flag+=1
    if flag>0:
        q=s+c
        for p in range(1,q+1):
            if q%p==0 and p!=q and p!=1:
                flag2+=1
        if flag2>0:
            print(q,s)
            break
    
