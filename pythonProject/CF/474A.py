v = input()
s = input()
a = list()
a.append("qwertyuiop")
a.append("asdfghjkl;")
a.append("zxcvbnm,./")
res = ''
if v == 'R':
    for w in range(len(s)):
        for i in range(len(a)):
            if s[w] in a[i]:
                for j in range(len(a[i])):
                    if a[i][j] == s[w]:
                        res += a[i][j - 1]
elif v == 'L':
    for w in range(len(s)):
        for i in range(len(a)):
            if s[w] in a[i]:
                for j in range(len(a[i]) - 1):
                    if a[i][j] == s[w]:
                        res += a[i][j + 1]
print(res)
