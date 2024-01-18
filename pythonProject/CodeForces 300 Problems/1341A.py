t = int(input())
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    if (c - d) / (a + b) <= n <= (c + d) / (a - b):
        print('yes')
    else:
        print('no')
