t = int(input())
for i in range(t):
    s = input()
    a = s[0]
    b = ''
    if len(s) == 2 and s[0] < s[1]:
        a = s[0]
        b = s[1]
    elif len(s) == 2 and s[0] > s[1]:
        a = -1
        b = ''
    else:
        for j in range(1, len(s) - 1):
            if int(a) < int(s[j:]) and int(s[j]) != 0:
                b = s[j:]
                break
            elif int(a) < int(s[j:]) and int(s[j]) == 0:
                a += s[j]
                b = s[j:]
            else:
                a = '-1'
                b = ''
                break
    print(a, b)
