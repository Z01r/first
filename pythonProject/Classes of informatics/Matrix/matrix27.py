n,m=map(int,input().split())
a=[[0 for i in range(n)]for j in range(m)]
b=list()
for i in range(n):
    a[i]=list(map(int,input().split()))
    b.append(min(a[i]))
print(max(b))