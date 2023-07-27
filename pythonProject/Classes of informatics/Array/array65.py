a=[]
n=int(input())
k=int(input())
b=[]
k=k-1
for i in range(n):
    a.append(int(input()))
p=a[k]
for k in range(n):
    b.append(a[k]+p)
print(b)
