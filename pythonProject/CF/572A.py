q,w = map(int,input().split())
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
kol1 = 0
kol2 = 0
p = min(len(a), len(b))
for i in range(p):
    if a[i] > b[i]:
        kol1 += 1
    elif a[i] < b[i]:
        kol2 += 1
if (kol1 >= k) and (kol2 >= m):
    print("YES")
else:
    print("NO")
print(kol1,kol2)