n = int(input())
res = 0
for i in range(6, n + 1):
    s = set()
    j = 2
    a = i
    while a != 1:
        while a % j != 0:
            j += 1
        else:
            a //= j
            s.add(j)
    if len(s) == 2:
        res += 1
print(res)
