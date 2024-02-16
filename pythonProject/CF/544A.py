k = int(input())
q = input()
a = []
s = ""
u = set()
for i in range(len(q)):
    if q[i] not in u:
        if len(s) > 0:
            a.append(s)
        s = ""
        s += q[i]
        u.add(q[i])
    else:
        s += q[i]
a.append(s)
if len(a) < k:
    print("NO")
else:
    print("YES")
    for i in range(k, len(a)):
        a[k - 1] += a[i]
    for i in range(k):
        print(a[i])
