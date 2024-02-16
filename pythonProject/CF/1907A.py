t = int(input())
q = [1, 2, 3, 4, 5, 6, 7, 8]
w = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(t):
    a = list()
    p = input()
    s = p[0]
    n = int(p[1])
    for e in q:
        if e != n:
            a.append(s+str(e))
    for u in w:
        if u != s:
            a.append(u+str(n))
    for y in a:
        print(y)
