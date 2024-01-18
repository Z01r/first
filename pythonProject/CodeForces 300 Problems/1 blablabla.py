n = int(input())
for i in range(1, n + 1):
    l = str(i)
    l = int(l[::-1])
    if i == l:
        print(i)
