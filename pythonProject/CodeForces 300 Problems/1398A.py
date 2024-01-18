t = int(input())
for p in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    e = 0
    v = 0
    b = 0
    m = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for z in range(j + 1, len(a)):
                if (a[i] + a[j] < a[z]) or (a[i] + a[z] < a[j]) or (a[j] + a[z] < a[i]):
                    e = 11111
                    v = i+1
                    b = j+1
                    m = z+1
                    break
    if e > 0:
        print(v, b, m)
    else:
        print(-1)
