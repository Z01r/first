n, x = map(int, input().split())
st, end = -1, 10000
for i in range(n):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    st = max(a, st)
    end = min(end, b)
if st > end:
    print(-1)
elif end >= x >= st:
    print(0)
else:
    print(min(abs(st - x), abs(end - x)))
