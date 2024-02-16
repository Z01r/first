t = int(input())
c = 'codeforces'
for _ in range(t):
    s = input()
    w = 0
    for i in range(len(s)):
        if s[i] == c[i]:
            w += 1
    print(10-w)

