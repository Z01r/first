s = input()
p = ''
l = ''
k = len(s) % 2
b = ''
for i in range(0, len(s) + k, 2):
    p += s[i]
for j in range(1, len(s) - 1 + k, 2):
    l += s[j]
p = p[::-1]
b += l
b += p
print(b)
