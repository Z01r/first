t = int(input())
for _ in range(t):
    s = set()
    n = int(input())
    for i in range(1, n + 1):
        s.add(i)
    while len(list(s)) > 1:
        l = max(s) - min(s)
        s.remove(max(s))
        s.remove(min(s))
        s.add(l)
        print(s)
    print(list(s)[0])