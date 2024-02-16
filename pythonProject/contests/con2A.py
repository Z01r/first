t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    kol = 0
    for i in range(len(p) - 1, 2):
        if p[i + 1] < p[i]:
            kol += 1
    print(kol)
