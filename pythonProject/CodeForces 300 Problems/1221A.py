t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = "YES"
    b = []
    for i in a:
        if i <= 2048:
            b.append(i)
    if sum(b) < 2048:
        res = "NO"
    print(res)