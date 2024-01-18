t = int(input())
a = []
k = ''
for i in range(1, 10):
    k = ''
    for j in range(1, 5):
        k += str(i)
        a.append(int(k))
for d in range(t):
    n = int(input())
    l = a.index(n)
    l = l + 1
    if l % 4 == 1:
        print(((l // 4) * 10) + 1)
    elif l % 4 == 2:
        print(((l // 4) * 10) + 3)
    elif l % 4 == 3:
        print(((l // 4) * 10) + 6)
    else:
        print(((l // 4) * 10))
