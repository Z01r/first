n = int(input())
a = [int(x) for x in input().split()]
i = 0
while True:
    n -= a[i]
    if n <= 0:
        print(i + 1)
        break
    i = (i + 1) % 7
