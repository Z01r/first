n = int(input())
a = list(map(int, input().split()))
kol = 0
for i in range(len(a)):
    if a.count(a[i]) == 2 and a[i] != 0:
        kol += 1
    elif a[i] == 0:
        kol += 0
    elif a.count(a[i]) >= 3:
        kol = -1
        break
if kol == -1:
    print(kol)
else:
    print(kol // 2)
