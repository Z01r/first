n, k = map(int, input().split())
s = input()
c = list(map(str, input().split()))
d = ""
kol = 0
for i in s:
    if i in c:
        d += i
    else:
        for w in range(1, len(d) + 1):
            kol += len(d) // w
        d = ""
