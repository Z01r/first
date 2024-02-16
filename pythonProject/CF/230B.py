def f(n):
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
    return len(a)


n = int(input())
p = map(int, input().split())
for i in p:
    if f(i) == 3:
        print("YES")
    else:
        print("NO")
