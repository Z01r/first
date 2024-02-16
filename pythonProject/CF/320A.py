s = input()
w = ""
if s[0] != "1":
    print("NO")
    exit()
elif s[0] == "1" and len(s) == 1:
    print("YES")
    exit()
for i in range(len(s)-1):
    w += s[i]
    if s[i] == "1" or s[i] == "4":
        if w == "144" and s[i + 1] == "4":
            print("NO")
            exit()
        elif (w == "1" and s[i+1] == "1") or (w == "14" and s[i+1] != "4") or (w == "144"):
            w = ""
    else:
        print("NO")
        exit()
if s[i+1] != "1" and s[i+1] != "4":
    print("NO")
    exit()
print("YES")