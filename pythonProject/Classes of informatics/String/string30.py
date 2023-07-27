c = input()
s = input()
s0 = input()
p = ''
for i in s:
    p += i
    if i == c:
        p += s0
print(p)
