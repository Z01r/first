n = int(input())
a = []
b = []
for i in range(n):
    s = input()
    a.append(s)
for j in a:
    if j not in b:
        b.append(j)
if len(b) > 1:
    mx = max(a.count(b[0]), a.count(b[1]))
    if mx == a.count(b[0]):
        res = b[0]
    else:
        res = b[1]
    print(res)
else:
    print(b[0])
