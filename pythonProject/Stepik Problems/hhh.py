a = input()
b = input()
d = []
v = []
a = set(a)
b = set(b)
print(a,b)
for i in a:
    d.append(i)
for j in b:
    v.append(j)
d.sort()
v.sort()
q = 0
if len(v) == len(d):
    for g in range(len(v)):
        if v[g] != d[g]:
            q += 1
    if q == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')