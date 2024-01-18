n = int(input())
a = list(map(int, input().split()))
res = 1
k = a[0]
p = 1
for i in range(1, len(a)):
    if a[i] > k:
        p += 1
    else:
        p = 1
    res = max(res, p)
    k = a[i]
print(res)
