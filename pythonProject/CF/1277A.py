t = int(input())
for i in range(t):
    n = input()
    b = len(n)
    n = int(n)
    c = int('1' * b)
    d = n // c
    print(d + (9 * (b - 1)))
