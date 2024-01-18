n = int(input())
a = sorted(list(map(int, input().split())))
mx = 0
if sum(a) % 2 == 0:
    mx = sum(a)
else:
    for i in range(n):
        if a[i] % 2 == 1:
            mx = sum(a) - a[i]
            break
print(mx)