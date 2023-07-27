n=int(input())
a=0
b=0
c=0
d=0
mx1=0
mx2=0
mx3=0
mx4=0
z=[]
for i in range(1,n+1):
    h=input().split()
    a=int(h[0])
    b=int(h[1])
    c=int(h[2])
    d=int(h[3])
    mx1=max(a,b)
    mx2=max(c,d)
    mx3=max(mx1,mx2)
    mx4=max(((a+b)-mx1),((c+d)-mx2))
    if ((mx1+mx2)-mx3)<mx4:
        z.append('NO')
    if ((mx1+mx2)-mx3)>mx4:
        z.append('YES')
for i in range(len(z)):
    print(z[i])
