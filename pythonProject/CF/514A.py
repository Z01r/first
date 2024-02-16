x = int(input())
s = str(x)
p = ""
if s[0] != '9':
    for i in s:
        if int(i) > 4:
            p += str(9 - int(i))
        else:
            p += i
else:
    p = "9"
    for i in s[1:]:
        if int(i) > 4:
            p += str(9 - int(i))
        else:
            p += i
print(p)
