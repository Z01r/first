s = input()
e = s[::-1]
kol = 0
for i in range(len(s)//2):
    if s[i] != e[i]:
        kol += 1
if kol > 1:
    print("NO")
elif len(s) % 2 == 0 and kol == 0:
    print("NO")
else:
    print("YES")
