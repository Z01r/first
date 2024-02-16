n = int(input())
s = input()
a = []
d = ''
kol = 2
if n == 1:
    print(1)
    print(s)
    exit()
if s.count('1') != s.count('0'):
    print(1)
    print(s)
    exit()
for i in range(len(s)):
    d += s[i]
    if (d.count('1') != d.count('0')) and (s[i + 1:].count('1') != s[i + 1:].count('0')):
        print(kol)
        print(d, s[i + 1:])
        exit()
    elif (d.count('1') != d.count('0')) and (s[i + 1:].count('1') == s[i + 1:].count('0')):
        a.append(d)
        d = ''
        kol += 1
    elif (d.count('1') == d.count('0')) and len(d) == 2:
        continue
