m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
ind = 0
for i in range(m):
    matrix[i] = list(map(int, input().split()))
mx = matrix[0][0]
for p in range(len(matrix)):
    if mx < max(matrix[p]):
        mx = (max(matrix[p])) + mx - mx
        ind = p
for x in range(len(matrix)):
    print(*matrix[x])
    if x == ind:
        print(*matrix[ind])
