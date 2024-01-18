import math
a, m = map(int, input().split())
r = math.log2(m)
s = 0
for i in range(1,int(r)+1):
    if a*(2 ** i) % m == 0:
        s += 1
print("Yes" if s > 0 else "No")