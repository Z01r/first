n, m = map(int, input().split())
a = input().split()
b = set()
for i in range(n):
    b.add(a[~i])
    a[~i] = len(b)
for _ in range(m):
    l = int(input())
    print(a[l - 1])
