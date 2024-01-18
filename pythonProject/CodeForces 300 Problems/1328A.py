n=int(input())
k=''
a=0
b=0
ost=0
cch=0
for i in range(1,n+1):
    k=input().split()
    a=int(k[0])
    b=int(k[1])
    ost=a%b
    cch=(((a-ost)//b)+1)*b
    if a>b and a%b!=0:
        print(cch-a)
    if a<b:
        print(b-a)
    if a%b==0:
        print('0')
