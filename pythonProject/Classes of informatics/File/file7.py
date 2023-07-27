a = list()
b = list()
sch = 0
sv = 0
with open("jkl", "r") as file:
    k = file.read()
    p = ''
    for i in k:
        if sch < 2:
            if i == " ":
                sch += 1
                a.append(int(p))
                p = ''
            else:
                p += i
    k = k[::-1]
    p = ''
    for c in k:
        if sv < 2:
            if c == " ":
                sv += 1
                p = p[::-1]
                b.append(int(p))
                p = ''
            else:
                p += c
b.reverse()
print(*a, *b)