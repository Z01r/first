s = input()
s = s[::-1]
p = ''
flag = 0
for i in s:
    if i == '.' and flag == 0:
        flag += 1
    if flag > 0:
        p += i
    if i == '/' and flag > 0:
        break
p = p[:len(p) - 1]
p = p[::-1]
p = p[:len(p) - 1]
print(p)
