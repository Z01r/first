n = int(input())
a = list(map(int, input().split()))
b = []
mx = 0
for i in a:
    if len(b) > 0:
        if b[len(b) - 1] <= i:
            b.append(i)
        else:
            mx = max(mx, len(b))
            b = [i]
    else:
        b.append(i)
    print(b)
mx = max(len(b), mx)
print(mx)
