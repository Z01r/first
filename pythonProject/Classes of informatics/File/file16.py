with open("serii1", "r") as mf:
    p = ''
    k = mf.read()
    l = k.split()
    for i in range(len(l)):
        if (l[i] in p) or (l[i] not in p and len(p) == 0):
            p = p + str(l[i]) + " "
        else:
            x = "s{0}".format(i-1)
            h = open(x,"w+")
            for j in p:
                h.write(j)
                h.write(" ")
            p = l[i] + " "
    x = "s{0}".format(i)
    h = open(x, "w+")
    for j in p:
        h.write(j)
        h.write(" ")
