n = int(input())
s = input()
kol = 0
m = ''
for i in s:
    if i == 'x':
        m += i
    elif i != 'x' and len(m) > 2:
        kol += len(m) - 2
        m = ''
    elif i != 'x' and len(m) < 3:
        m = ''
if len(m) > 2:
    kol += len(m) - 2
print(kol)
