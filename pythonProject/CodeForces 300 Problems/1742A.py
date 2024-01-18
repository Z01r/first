n=int(input())
a=0
b=0
c=0
m=[]
for i in range(1,n+1):
    h=input().split()
    a=int(h[0])
    b=int(h[1])
    c=int(h[2])
    if (b+c==a) or (a+b==c) or (c+a==b):
        m.append('YES')
    else:
        m.append('NO')
for j in range(len(m)):
    print(m[j])
    
