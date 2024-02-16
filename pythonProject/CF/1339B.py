t = int(input())
for i in range(t):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = []
    while a:
        b.append(a.pop(len(a)//2))
    print(*b)