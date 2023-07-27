f1 = 1
f2 = 1
f3 = 1
n = int(input())
p = 3
if n > 2:
    g = [1] * 3
else:
    g = [1] * n
j = 0
while p < n:
    p += 1
    j = f1 + f2 + f3
    g.append(j)
    f1 = f2
    f2 = f3
    f3 = j
print(*g)
