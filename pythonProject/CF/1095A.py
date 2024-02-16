n = int(input())
s = input()
r = ''
v = ''
l = 0
p = 0
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        r += s[i - 1]
print(r + s[len(s) - 1])
