s = input()
a = []
for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s not in a:
        a.append(s)
print(len(a))
