t, s, x = map(int, input().split())
res = t
ans = "NO"
while res <= x:
    if res == x:
        ans = "YES"
        break
    res += s
    if res == x or res+1 == x:
        ans = "YES"
        break
print(ans)
