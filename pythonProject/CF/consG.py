t = int(input())
for w in range(t):
    a, b, q = map(int, input().split())
    kol = 0
    k = []
    for _ in range(q):
        l, r = map(int, input().split())
        if (r - l) % 2 == 0:
            for x in range(1, ((r - l) // 2)+1):
                p = x % a
                v = x % b
                if (p % b) != (v % a):
                    kol += 1
                p = (r - x + 1) % a
                v = (r - x + 1) % b
                if (p % b) != (v % a):
                    kol += 1
                print(kol)
        else:
            for x in range(1, ((r - l) // 2)):
                p = x % a
                v = x % b
                if (p % b) != (v % a):
                    kol += 1
                p = (r - x + 1) % a
                v = (r - x + 1) % b
                if (p % b) != (v % a):
                    kol += 1
            f = (r - l) // 2
            p = f % a
            v = f % b
            if (p % b) != (v % a):
                kol += 1
        k.append(kol)
        kol = 0
    print(*k)
