s = input().split()
d = s[len(s)-1]
x = s[0]
kol = 0
if d == 'week':
    if x != '6' and x != '5':
        kol = 52
    else:
        kol = 53
elif d == 'month':
    if int(x) < 30:
        kol = 12
    elif int(x) == 30:
        kol = 11
    elif int(x) == 31:
        kol = 7
print(kol)