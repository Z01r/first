s = input().upper()
a = "AEUOIYU"
b = "QWRTPSDFGHJKLZXCVBNM"
res = ""
for i in range(0,len(s)):
    if s[i] in b:
        res += "." + s[i]
res = res.lower()
print(res)
