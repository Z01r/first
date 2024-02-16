t = int(input())
for j in range(t):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    b.reverse()
    for i in range(k):
        if b[i] > a[i]:
            a[i] = b[i]
    print(sum(a))
