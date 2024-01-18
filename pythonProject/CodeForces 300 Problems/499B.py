n, m = map(int, input().split())
p = []
for _ in range(m):
    s1, s2 = map(str, input().split())
    l = [s1, s2]
    p.append(l)
s = input().split()
x = []
for j in s:
    for i in p:
        if j in i:
            if len(i[0]) <= len(i[1]):
                x.append(i[0])
            else:
                x.append(i[1])
print(*x)