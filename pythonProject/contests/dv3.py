t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = ""
    q = 0
    e = "abcdefghijklmnopqrstuvwxyz"
    for i in range(n):
        if a[i] == 0:
            s += e[q]
            q += 1
        elif a[i] > 0:
            for j in s:
                if s.count(j) == a[i]:
                    s += j
                    break
    print(s)