m, n = map(int, input().split())
b = list()
c = list()
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
    for x in matrix[i]:
        b.append(x)
        c.append(i)
o = b.index(min(b))
s = c[o]
for p in range(len(matrix)):
    if p != s:
        print(*matrix[p])
