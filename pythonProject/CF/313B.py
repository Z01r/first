s = input()
n = int(input())
a = []
kol = 0
a.append(kol)
for j in range(1,len(s)):
    if s[j-1] == s[j]:
        kol += 1
    a.append(kol)
for _ in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(a[r]-a[l])
print(a)