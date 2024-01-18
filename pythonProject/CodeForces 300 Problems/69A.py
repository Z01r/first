t = int(input())
a = 0
b = 0
c = 0
for i in range(t):
    x, y, z = map(int, input().split())
    a += x
    b += y
    c += z
res = ""
if a == b == c == 0:
    res = "YES"
else:
    res = "NO"
print(res)
