n,m=map(int,input().split())
mat=[[0 for i in range(n)] for j in range(m)]
for l in range(n):
    mat[l]=list(map(int,input().split()))
for j in range(m):
    for i in range(n):
        if j%2==1:
            t = mat[i][j]
            mat[i][j] = mat[n-1-i][j]
            mat[n-1-j] = t
for v in mat:
    print(*v)
