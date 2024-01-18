n, k = map(int, input().split())
mx = -999999999999999999
for i in range(n):
    f, t = map(int, input().split())
    if t > k:
        f -= (t - k)
    mx = max(mx, f)
print(mx)
