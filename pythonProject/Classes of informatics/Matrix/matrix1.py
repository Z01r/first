n,m=map(int,input().split())
matrix=[[0 for i in range(n)] for j in range(m)]
for i in range(n):
    matrix[i]=list(map(int,input().split()))
for k in matrix:
    print(*k)
