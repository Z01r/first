n = int(input())
a = list(map(int, input().split()))
ln = 1
kol = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i]:
        ln += 1
    elif ln > 1:
        ln += 1
        kol = max(kol, ln)
        ln = 1
    else:
        kol = max(kol,ln)
        ln = 1
print(max(kol,ln))
