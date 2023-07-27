s = input().split()
z = list()
for j in s:
    l = j[0]
    j = j[::-1]
    k = j.replace(l, ".", )
    k = k[::-1]
    k = k[:len(k) - 1]
    k += l
    z.append(k)
print(*z)
