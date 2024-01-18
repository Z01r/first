t = int(input())
j = []
for e in range(t):
    f = int(input())
    a = list(map(int, input().split()))
    kol = 0
    p = 0
    for i in range(len(a)):
        if a[i] == 0:
            p += 1
        elif a[i] == 1:
            kol = max(kol, p)
            p = 0
    kol = max(kol, p)
    j.append(kol)
for m in j:
    print(m)
