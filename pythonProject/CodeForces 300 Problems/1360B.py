n = int(input())
mn = 0
o = []
for i in range(n):
    a = int(input())
    h = input().split()
    mn = 123456789999909999999999999
    if a != 2:
        for d in range(a):
            for c in range(d + 1, a):
                mn = min(mn, abs(int(h[d]) - int(h[c])))
    else:
        mn = (abs(int(h[0]) - int(h[1])))
    o.append(mn)
for y in range(len(o)):
    print(o[y])
