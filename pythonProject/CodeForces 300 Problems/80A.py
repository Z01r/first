n, m = map(int, input().split())
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 0]
if a[a.index(n) + 1] != m:
    print('NO')
else:
    print('YES')
