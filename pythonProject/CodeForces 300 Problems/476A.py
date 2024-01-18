n, m = map(int, input().split())
f = m
if n < m:
    print(-1)
    exit()
while 1 != 2:
    if m * 2 >= n >= m:
        print(m)
        exit()
    m += f
print(-1)
# ✅
