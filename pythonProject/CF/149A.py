k = int(input())
a = list(map(int, input().split()))
p = 0
kol = 0
if sum(a) < k:
    print(-1)
    exit()
while p < k:
    p += max(a)
    kol += 1
    del a[a.index(max(a))]
print(kol)
