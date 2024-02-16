q = input()
a, b = map(str, input().split())
g = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
res = ""
if (q in a) and (q not in b):
    res = "YES"
elif a[1] == b[1]:
    if g.index(a[0]) > g.index(b[0]):
        res = "YES"
    else:
        res = "NO"
else:
    res = "NO"
print(res)
