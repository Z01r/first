d, s = map(int, input().split())
a = [0] * d
b = [0] * d
c = [0] * d
for i in range(d):
    a[i], b[i] = map(int, input().split())
if sum(b) < s or sum(a) > s:
    print("NO")
else:
    print("YES")
    s -= sum(a)
    while s > 0:
        for i in range(d):
            if a[i] < b[i]:
                a[i] += 1
                s -= 1
            if s == 0:
                break
    print(*a)
