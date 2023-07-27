s = input()
a = list()
k = ''
p = '+-'
z = '1234567890'
for i in s:
    if i in z:
        k += i
    elif i in p:
        a.append(int(k))
        a.append(i)
        k = ''
a.append(k)
c = int(a[0])
for i in range(1, len(a) - 1):
    if a[i] == '+':
        c = c + int(a[i + 1])
    elif a[i] == '-':
        c = c - int(a[i + 1])
print(c)

