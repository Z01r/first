n = int(input())
for i in range(n):
    s = input()
    d = input()
    h = input()
    p = [s, d, h]
    t = ''
    e = 'ABC'
    ans = ''
    for j in p:
        j = sorted(j)
        if '?' in j:
            for y in j:
                t += y
        t = sorted(t)
    for x in range(3):
        if e[x] != t[x]:
            ans = e[x]
    print(ans)
