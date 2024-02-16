s1 = input()
s2 = input()
d = ""
k = []
p = ""
for j in s1.split():
    d += j
for r in d:
    k.append(d.count(r))
for v in s2.split():
    p += v
for i in p:
    if i in d and k[d.index(i)]:
        k[d.index(i)] -= 1
    else:
        print("NO")
        exit()
print("YES")