s = input().split()
z = list()
for j in s:
    l = j[0]
    k = j.replace(l, ".", )
    k = k[::-1]
    k = k[:len(k)-1]
    k += l
    k = k[::-1]
    z.append(k)
print(*z)