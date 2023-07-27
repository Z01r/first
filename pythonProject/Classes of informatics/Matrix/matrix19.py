n,m=map(int,input().split())
mat=[[0 for i in range(n)] for j in range(m)]
for i in range(n):
    mat[i]=list(map(int,input().split()))
for k in mat:
    print(sum(k))
