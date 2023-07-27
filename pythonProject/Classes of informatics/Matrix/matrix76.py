m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for p in matrix:
    p.sort()
    print(*p)