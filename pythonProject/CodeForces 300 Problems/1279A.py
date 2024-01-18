t = int(input())
for _ in range(t):
    r, g, b = sorted(map(int, input().split()))
    res = "Yes"
    if r + g + 1 < b:
        res = "No"
    print(res)

