c = 'codeforces'
t = int(input())
r = list()
for _ in range(t):
    s = input()
    kol = 0
    for i in range(len(s)):
        if s[i] != c[i]:
            kol += 1
    r.append(kol)
for j in r:
    print(j)