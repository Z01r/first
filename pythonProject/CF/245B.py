w = ["http", "ftp"]
s = input()
k = ""
res = ""
cu = 0
cp = 0
for i in range(len(s)):
    k += s[i]
    if k in w and cp == 0:
        res += k
        res += "://"
        k = ""
        cp += 1
    if k[-2:] == "ru" and len(res) > 0 and cu == 0 and s[i+1:] != "" and len(k) > 2:
        k += s[i]
        k = k[:-3] + "." + "ru" + "/"
        res += k
        k = ""
        cu += 1
    elif k[-2:] == "ru" and len(res) > 0 and cu == 0 and s[i+1:] == "":
        k += s[i]
        k = k[:-3] + "." + "ru"
        res += k
        k = ""
        cu += 1
res += k
print(res)
