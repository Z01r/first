t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    if n % 2 != 0:
        for i in range(n):
            a.append(1)
    else:
        a = [1, 3]
        for i in range(n - 2):
            a.append(2)
    print(*a)
