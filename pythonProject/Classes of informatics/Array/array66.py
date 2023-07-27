a=[]
n=int(input())
b=[]
flag=0
p=0
for i in range(n):
    m=int(input())
    a.append(m)
    if m%2==0 and flag==0:
        p=m
        flag+=1
for k in range(n):
    if a[k]%2==0:
        b.append(a[k]+p)
print(b)
