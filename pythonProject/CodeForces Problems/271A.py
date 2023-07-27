n=int(input())
a=''
b=''
c=''
d=''
flag=0
k=n+1
res=0
while 1!=2:
    k=str(k)
    a=k[0]
    b=k[1]
    c=k[2]
    d=k[3]
    if a==b or a==c or a==d or b==c or b==d or c==d:
        flag=0
        k=int(k)+1
    else:
        res=int(k)
        break
print(res)
        
