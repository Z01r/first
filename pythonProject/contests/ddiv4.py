C = 'bcd'
V = 'ae'
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    e = ''
    res = ''
    for i in range(len(s)):
        e += s[i]
        if len(e) == 2 and e[0] in C and e[1] in V and s[i + 1] in V:
            res += e + '.'
            e = ''
        elif len(e) == 2 and e[0] in C and e[1] in V and s[i+1] in C:
            res
        elif len(e) == 3:
            res += e + '.'
            e = ''
        print(res,e)
