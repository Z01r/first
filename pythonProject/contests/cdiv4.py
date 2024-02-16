t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    d = sum(s)
    if (d ** (1 / 2)) % 1 == 0:
        print("YES")
    else:
        print("NO")
