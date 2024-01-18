n = int(input())
a = sorted(list(map(int, input().split())))
b = a[len(a) - 2] - a[0]
c = a[len(a) - 1] - a[1]
print(min(b, c))
