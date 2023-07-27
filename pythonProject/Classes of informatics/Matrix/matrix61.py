m, n = map(int, input().split())
k = int(input())
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for p in range(len(matrix)):
    if p != k - 1:
        print(*matrix[p])
