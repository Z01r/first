n, l = map(int, input().split())
s = sorted(map(int, input().split()))
mx = max(s[0], l - s[-1])
for i in range(1, n):
    mx = max(mx, (s[i] - s[i - 1]) / 2)
print(mx)
