k = int(input())
s = sorted(input())
t = s[::k] * k
if sorted(t) == s:
    print("".join(t))
else:
    print(-1)
