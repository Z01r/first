n = int(input())
p = 3
kol = 0
a = list(map(int, input().split()))
for i in a:
    if i == p and p != 3:
        i = 0
    elif i == 3 and p != 3:
        i -= p
    if i == 0:
        kol += 1
    p = i
print(kol)
