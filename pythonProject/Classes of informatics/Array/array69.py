a=[]
n=int(input())
b=[]
for i in range(n):
    m=int(input())
    a.append(m)
for j in range(n):
    if j%2==1:
        b.append(a[j])
        b.append(a[j-1])
print(b)
