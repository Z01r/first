t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if (s % 4 == 0) or (s % 2 == 0 and 1 in a):
        print('YES')
    else:
        print('NO')
