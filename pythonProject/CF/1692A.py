for y in range(int(input())):
    a, b, c, d = map(int, input().split())
    h = [a, b, c, d]
    h.sort()
    g = h.index(a)
    print(4 - g - 1)
