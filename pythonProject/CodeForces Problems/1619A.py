z=int(input())
for w in range(1,z+1):
    q=input()
    p=''
    c=''
    if len(q)%2!=0:
        print('No')
    if len(q)%2==0:
        for i in range(len(q)//2):
            p+=q[i]
        q=q[::-1]
        for u in range(len(q)//2):
            c+=q[u]
        c=c[::-1]
        if p==c:
            print('Yes')
        else:
            print('No')
