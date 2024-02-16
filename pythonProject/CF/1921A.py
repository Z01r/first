t = int(input())
for _ in range(t):
    x = [0] * 4
    y = [0] * 4
    x[0], y[0] = map(int, input().split())
    x[1], y[1] = map(int, input().split())
    x[2], y[2] = map(int, input().split())
    x[3], y[3] = map(int, input().split())
    x.sort()
    y.sort()
    a = max(x[3] - x[0], y[3] - y[0])
    print(a * a)
