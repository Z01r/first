n = int(input())
a = []
h = 'Timur'
v = []
for q in h:
    v.append(q)
v.sort()
for i in range(n):
    j = int(input())
    s = input()
    l = []
    for j in s:
        l.append(j)
    l.sort()
    if l == v:
        a.append('YES')
    elif l != v:
        a.append('NO')
for w in a:
    print(w)
