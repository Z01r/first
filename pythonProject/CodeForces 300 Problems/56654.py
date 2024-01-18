n = int(input())
m = int(input())
mx = 0
mn = 0
a = []
for i in range(n):
    a.append(int(input()))
mx = max(a) + m
if (max(a) * n) - sum(a) > m:
    mn = max(a)
else:
    if ((sum(a) + m) % n) > 0:
        mn = ((sum(a) + m) // n) + 1
    else:
        mn = (sum(a) + m) // n
print(mn, mx)
