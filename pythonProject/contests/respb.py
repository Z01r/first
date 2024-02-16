n = int(input())
a = list(map(int, input().split()))
x = max(a)
a.remove(a[a.index(x)])
for i in a:
    if x % i == 0 and x != i:
        a.remove(i)
print(x, max(a))
