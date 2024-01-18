n, k = map(int, input().split())
a = list(map(int, input().split()))
mx = 0
x = 1
c = a[0]
for i in range(1, len(a)):
    if a[i] != c:
        x += 1
    elif a[i] == c:
        mx = max(mx, x)
        x = 1
    c = a[i]
mx = max(mx, x)
print(mx)
