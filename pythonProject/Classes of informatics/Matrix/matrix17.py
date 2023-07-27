n,m=map(int,input().split())
k=int(input())
mat=[[0 for i in range(n)] for j in range(m)]
for i in range(n):
    mat[i]=list(map(int,input().split()))
print(sum(mat[k-1]))
