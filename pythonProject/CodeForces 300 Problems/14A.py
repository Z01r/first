n, m = map(int,input().split())
mat = []
for _ in range(n):
    mat.append(input())
r1 = n - 1
r2 = 0
c1 = m - 1
c2 = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == '*':
            r1 = min(r1, i)
            r2 = max(r2, i)
            c1 = min(c1, j)
            c2 = max(c2, j)
for i in range(r1, r2 + 1):
    print(mat[i][c1: c2 + 1])
