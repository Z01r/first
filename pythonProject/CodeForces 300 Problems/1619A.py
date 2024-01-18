t = int(input())
for _ in range(t):
    s = input()
    ans = "NO"
    e = ""
    f = ""
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            e += s[i]
        s = s[::-1]
        for j in range(len(s) // 2):
            f += s[j]
        f = f[::-1]
        if e == f:
            ans = "YES"
    print(ans)
