a = input()
b = input()
l = ''
v = 0
for i in range(len(a)):
    if a[i] == b[0]:
        for j in range(len(b)):
            if i + j < len(a):
                l += a[i + j]
            else:
                break
        if l == b:
            v += 1
if v > 0:
    print('YES')
else:
    print('NO')
