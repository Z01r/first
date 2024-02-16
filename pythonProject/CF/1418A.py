t = int(input())
for i in range(t):
    x, y, k = map(int, input().split())
    print(((y + 1) * k - 1 + x - 2) // (x - 1) + k)
