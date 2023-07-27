m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i]=list(map(int,input().split()))
for j in range(0, n):
    sum = 0
    for i in range(0, j):
        sum = sum + matrix[i][n - j + i]
    print(sum)

for j in range(n - 2, -1, -1):
    sum = 0
    for i in range(0, j):
        sum = sum + matrix[n - j + i][i]
    print(sum)