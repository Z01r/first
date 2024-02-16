n, m = map(int, input().split())
g = list(map(int, input().split()))
kol = 0
l = 0
for i in g:
    if l + i <= m:
        l += i
    else:
        kol += 1
        l = i
print(kol+1)