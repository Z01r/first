t=int(input())
a=input().split()
n=int(input())
b=input().split()
c=[]
flag=0
s=0
for i in a:
    for j in b:
        if (str(int(i)+int(j)) not in a) and (str(int(i)+int(j)) not in b) and flag==0:
            flag=1
            c.append(int(i))
            c.append(int(j))
print(c[0],c[1])
