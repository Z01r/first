g=int(input())
q=[]
p=0
for i in range(1,g+1):
    h=input().split()
    a=int(h[0])
    b=int(h[1])
    if a>b and (a-b)%10!=0:
        p=((a-b)//10)+1
        q.append(p)
    if a<b and (b-a)%10!=0:
        p=((b-a)//10)+1
        q.append(p)
    if a>b and (a-b)%10==0:
        p=(a-b)//10
        q.append(p)
    if a<b and (b-a)%10==0:
        p=(b-a)//10
        q.append(p)
    if a==b:
        p=0
        q.append(p)
for l in range(len(q)):
    print(q[l])
            
            
    
