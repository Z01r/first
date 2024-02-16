n = int(input())
s = input().split()
a = []
for y in s:
    a.append(int(y))
x = 0
r = 0
for t in a:
    x += t
    r += x < 0
    x += x < 0
print(r)
