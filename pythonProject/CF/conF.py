n = int(input())
a = list(map(int, input().split()))
kol = 0
for i in range(1, len(a) - 1):
    if a[i - 1] > a[i] < a[i + 1]:
        kol += 1
    elif a[i - 1] == a[i] or a[i] == a[i + 1]:
        continue
    elif a[i - 1] < a[i] < a[i + 1]:
        a[i - 1], a[i] = a[i], a[i - 1]
        kol += 1
    elif a[i - 1] > a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
        kol += 1
print(kol)
print(*a)
