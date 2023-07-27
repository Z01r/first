m, n = map(int, input().split())
kol = 0
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[i] = list(map(int, input().split()))
for val in matrix:
    check = 1
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if val[j] == val[k]:
                check = 0
                break
        if check == 0:
            break
    kol += check
print(kol)
