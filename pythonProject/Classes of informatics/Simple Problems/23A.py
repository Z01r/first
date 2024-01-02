n = int(input())
a = []
k = int(input())
l = int(input())
b = l - k
kol = n - b - 1
summ = 0
for i in range(n):
    f = int(input())
    a.append(f)
    if (i + 1) < k or (i + 1) > l:
        summ += 0
    else:
        summ += f
print(summ)
