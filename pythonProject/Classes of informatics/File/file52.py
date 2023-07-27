s0 = input()
n = int(input())
mf = open(s0, "w+")
mf.write(str(n))
mf.write(" ")
a = [[0 for i in range(n)] for j in range(n)]
for e in range(n):
    x = "s{0}".format(e + 1)
    p = open(x, "w+")
    a[e] = list(map(int, input().split()))
    mf.write(str(len(a[e])))
    mf.write(" ")
mf.write("\n")
for d in a:
    for h in d:
        mf.write(str(h))
        mf.write(" ")
    mf.write("\n")