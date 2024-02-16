n = int(input())
kol = 0
for i in range(1, n + 1):
    a = []
    for j in str(i):
        a.append(int(j))
    if len(list(set(a))) <= 2 and sum(list(set(a))) == 1:
        kol += 1
print(kol)
