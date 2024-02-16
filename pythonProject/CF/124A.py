n, a, b = map(int, input().split())
for i in range(a + 1, n + 1):
    if i + b >= n:
        print(n+1-i)
        exit()
