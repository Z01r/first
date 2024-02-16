for _ in range(int(input())):
    n = int(input())
    p = 1
    rl = []
    x = []
    while n > 0:
        dig = n % 10
        r = dig * p
        rl.append(r)
        p *= 10
        n = n // 10
    for i in rl:
        if i != 0:
            x.append(i)
    print(len(x))
    print()
    print(*x)
