for y in range(int(input())):
    a,b,c,d=map(int,input().split())
    h=[]
    h.append(a)
    h.append(b)
    h.append(c)
    h.append(d)
    h.sort()
    g=h.index(a)
    print(4-g-1)
