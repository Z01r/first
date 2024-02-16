s = input()
kol = 0
p = s[::-1]
for i in range(len(s)):
    if s[i] != p[i]:
        kol += 1
if kol <= 1:
    print("YES")
else:
    print("NO")