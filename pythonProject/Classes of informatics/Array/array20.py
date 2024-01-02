n = int(input())
k = int(input())
l = int(input())
k -= 1
l -= 1
s = 0
u = 'false'
a = []
for i in range(n):
    r = int(input())
    a.append(r)
    if i == k:
        u = 'True'
    if k <= i <= l:
        s += r
    if i > l:
        u = 'False'
print(s)
