t = int(input())
for h in range(t):
    n = input()
    s = ''
    for j in range(0, len(n), 2):
        s += n[j]
    s += n[len(n) - 1]
    print(s)
