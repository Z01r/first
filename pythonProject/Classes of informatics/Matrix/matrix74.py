m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
matrix2 = [[0 for x in range(m)] for t in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for p in range(m):
    for y in range(1, n - 1):
        matrix2[p][0] = matrix[p][0]
        if matrix[p][y-1] > matrix[p][y] < matrix[p][y+1]:
            matrix2[p][y] = 0

        else:
            matrix2[p][y] = matrix[p][y]
    matrix2[p][n-1] = matrix[p][n-1]
for b in matrix2:
    print(*b)
