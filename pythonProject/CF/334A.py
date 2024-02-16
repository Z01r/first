n = int(input())
g = n * n
b = []
for i in range(1, g + 1, n//2):
    a = []
    for z in range(n//2):
        a.append(i+z)
        a.append(g-i+1-z)
    b.append(a)
for j in range(len(b)//2):
    print(*b[j])
