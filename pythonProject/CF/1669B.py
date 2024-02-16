t = int(input())
for q in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    l = -1
    for i in range(n - 2):
        if s[i] == s[i + 2]:
            l = s[i]
            break
    print(l)
