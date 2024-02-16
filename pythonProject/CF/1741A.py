t = int(input())
a = ['S', 'M', 'L']
m = []
for i in range(t):
    s = input().split()
    d = s[0][len(s[0]) - 1]
    v = s[1][len(s[1]) - 1]
    if s[0] == s[1]:
        m.append('=')
    elif (a.index(d) < a.index(v)) or (a.index(d) == a.index(v) and v == 'S' and len(s[0]) > len(s[1])) or (
            a.index(d) == a.index(v) and v == 'L' and len(s[0]) < len(s[1])):
        m.append('<')
    elif (a.index(d) > a.index(v)) or (a.index(d) == a.index(v) and v == 'S' and len(s[0]) < len(s[1])) or (
            a.index(d) == a.index(v) and v == 'L' and len(s[0]) > len(s[1])):
        m.append('>')

for z in m:
    print(z)