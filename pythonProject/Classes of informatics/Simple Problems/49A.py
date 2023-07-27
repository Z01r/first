n=int(input())
flag=0
b=[]
for i in range(1,n+1):
    a=int(input())
    b.append(a)
    if a!=i and flag==0:
        flag=i
if flag==0:
    print(flag)
if flag!=0:
    print(flag)
