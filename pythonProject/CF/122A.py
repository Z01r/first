def Sch(l):
    l = str(l)
    e = list(set(l))
    c = ""
    for k in e:
        c += k
    if c == "74" or c == "47" or c == "4" or c == "7":
        return 1
    else:
        return 0


n = int(input())
p = 0
while p < n:
    p += 1
    b = Sch(p)
    if b == 1:
        if n % p == 0:
            print("YES")
            exit()
print("NO")