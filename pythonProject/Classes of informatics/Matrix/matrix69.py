m, n = map(int, input().split())
k = int(input())
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for p in range(len(matrix)):
    b = list()
    for x in range(len(matrix[p])):
        if x == k - 1:
            b.append(matrix[p][x])
            b.append('1')
        else:
            b.append(matrix[p][x])
    print(*b)
