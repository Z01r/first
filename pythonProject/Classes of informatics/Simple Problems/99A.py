s = list(input().split())
r = []
for i in range(len(s)):
    if s.count(s[i]) < 2:
        r.append(s[i])
print(*r, len(r))
