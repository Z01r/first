t = int(input())
for _ in range(t):
    n = int(input())
    d = 1
    m = 3*n
    print((n+1)//2)
    for i in range((n+1)//2):
        print(d,m)
        d += 3
        m -= 3
