m=int(input())
a=[[0 for i in range(m)]for j in range(m)]
for i in range(m):
    a[i]=list(map(int,input().split()))
for i in range(m):
    for j in range(i,m-i):
        print(a[j][i],end=" ")
    for k in range(i+1,m-i):
        print(a[m-i-1][k],end=" ")
    for j in range(m-i-2,i-1,-1):
        print(a[j][m-i-1],end=" ")
    for p in range(m-i-2,i,-1):
        print(a[j][p],end=" ")
