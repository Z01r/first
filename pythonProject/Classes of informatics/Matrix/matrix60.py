m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
n -= 1
for i in range(m):
    matrix[i] = list(map(int, input().split()))
    for j in range((n + 1) // 2):
        p = matrix[i][j]
        matrix[i][j] = matrix[i][n - j]
        matrix[i][n - j] = p
for k in matrix:
    print(*k)
