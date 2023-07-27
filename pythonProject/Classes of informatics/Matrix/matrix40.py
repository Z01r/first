m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
b = list()
c = list()
for val in range(len(matrix)):
    mx = 0
    check = 0
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if matrix[val][j] == matrix[val][k]:
                check += 1
            if matrix[val][j] != matrix[val][k] and mx < check:
                mx = check
    b.append(mx)
    c.append(val + 1)
p = b.index(max(b))
print(c[p])
