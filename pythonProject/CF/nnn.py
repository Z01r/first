t = int(input())
for _ in range(t):
    s = input()
    d = "abc"
    kol = 0
    for i in range(3):
        if s[i] != d[i]:
            kol += 1
    if kol == 2 or kol == 0:
        print("YES")
    else:
        print("NO")
# ✅
