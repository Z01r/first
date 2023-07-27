m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
s = 0
ch = 0
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for p in range(len(matrix)):
    s += matrix[p][m - p - 1]
    ch += 1
print(s//ch)
