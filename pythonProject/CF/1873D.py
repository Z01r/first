t = int(input())
a = []
for i in range(t):
    n, k = map(int, input().split())
    s = input()
    c = 0
    j = 0
    while j < n:
        if s[j] == "B":
            c += 1
            j += k
        else:
            j += 1
    a.append(c)
for e in a:
    print(e)
