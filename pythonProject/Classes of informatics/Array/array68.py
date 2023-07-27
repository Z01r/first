a=[]
n=int(input())
b=[]
flag=0
p=0
for i in range(n):
    m=int(input())
    a.append(m)
mx=max(a)
mn=min(a)
for j in range(n):
    if a[j]==mx:
        b.append(mn)
    elif a[j]==mn:
        b.append(mx)
    else:
        b.append(a[j])
print(b)
