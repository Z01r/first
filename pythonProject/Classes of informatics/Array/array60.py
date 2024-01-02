a = []
n = int(input())
b = []
for i in range(n):
    a.append(int(input()))
for j in range(n):
    s = 0
    for k in range(j + 1, n + 1):
        s += k
    b.append(s)
print(b)
