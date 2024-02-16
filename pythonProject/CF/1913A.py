t = int(input())
for _ in range(t):
    s = input()
    f = 0
    for i in range(1, len(s)):
        x = int(s[0:i])
        y = int(s[i:])
        if s[i] != '0' and y > x:
            f = 1
            print(x, y)
            break
    if f == 0:
        print(-1)
# ✅