a = int(input())
b = int(input())
c = a + b
a = str(a)
b = str(b)
c = str(c)
na = ""
nb = ""
nc = ""
for i in a:
    if i != "0":
        na += i
for j in b:
    if j != "0":
        nb += j
for m in c:
    if m != "0":
        nc += m
na = int(na)
nb = int(nb)
nc = int(nc)
res = ""
if na + nb == nc:
    res = "YES"
else:
    res = "NO"
print(res)
