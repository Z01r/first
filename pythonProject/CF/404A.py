n = int(input())
s = []
for _ in range(n):
    s.append(input())
d = set()
nd = set()
res = ""
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            d.add(s[i][j])
        else:
            nd.add(s[i][j])
if len(d) == 1 and len(nd) == 1 and d.pop() != nd.pop():
    res = "YES"
else:
    res = "NO"
print(res)