m, n = map(int, input().split())
ind=-9
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for p in range(n):
    ch = 1
    for x in range(m):
        if matrix[x][p] <= 0:
            ch = 0
            break
    if ch==1 and ind<0:
        ind=p
for u in range(len(matrix)):
    b = list()
    for a in range(len(matrix[p])):
        if a == ind:
            b.append('1')
        b.append(matrix[u][a])
    print(*b)

