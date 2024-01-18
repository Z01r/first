n = int(input())
s = str(n)
res = 0
while len(s) > 1:
    t = 0
    for i in s:
        t += int(i)
    s = str(t)
    res += 1
print(res)
