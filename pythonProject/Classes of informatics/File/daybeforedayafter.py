def vis(y):
    if y % 4 == 0:
        if y % 400 != 0:
            return 'yes'
        elif y % 100 == 0:
            return 'no'
        else:
            return 'yes'
    else:
        return 'no'


def sled(s):
    d = int(s[:2])
    m = int(s[3:5])
    y = int(s[6:])
    p = vis(y)
    q = ['4', '6', '9', '11']
    w = ['1', '3', '5', '7', '8', '10', '12']
    if m != 2 and d < 30:
        d += 1
        d = str(d)
    elif m == 2 and d == 28 and p == 'yes':
        d += 1
        d = str(d)
    elif m == 2 and d == 28 and p == 'no':
        d = '01'
        m = '03'
    elif m == 12 and d == 31:
        d = '01'
        m = '01'
        y = str(y + 1)
    elif d == 30 and (m in w):
        d = '31'
    elif d == 30 and (m in q):
        d = '01'
        m = str(m + 1)
    elif d == 31:
        d = 1
        m += 1
    elif m == 2 and d < 27:
        d += 1
    d = str(d)
    m = str(m)
    y = str(y)
    if len(str(d)) == 1:
        d = str('0' + str(d))
    if len(str(m)) == 1:
        m = str('0' + str(m))
    return d + '/' + m + '/' + y


def prev(s):
    d = int(s[:2])
    m = int(s[3:5])
    y = int(s[6:])
    p = vis(y)
    q = ['4', '6', '9', '11']
    w = ['1', '3', '5', '7', '8', '10', '12']
    if d > 1:
        d -= 1
        d = str(d)
    elif m == 3 and d == 1 and p == 'yes':
        d = 29
        d = str(d)
        m = 2
        m = str(m)
    elif m == 3 and d == 1 and p == 'no':
        d = '28'
        m = '02'
    elif m == 1 and d == 1:
        d = '31'
        m = '12'
        y = str(y - 1)
    elif d == 1 and ((m - 1) in q):
        d = '30'
        m = m - 1
        m = str(m)
    elif d == 1 and ((m - 1) in w):
        d = '31'
        m = str(m - 1)
    d = str(d)
    m = str(m)
    y = str(y)
    if len(str(d)) == 1:
        d = str('0' + str(d))
    if len(str(m)) == 1:
        m = str('0' + str(m))
    return d + '/' + m + '/' + y


f1 = open("pred", "w+")
f2 = open("sled", "w+")
with open("file67t", "r") as file:
    k = file.read()
    p = k.split()
for i in p:
    h = sled(i)
    g = prev(i)
    f1.write(g)
    f1.write(" ")
    f2.write(h)
    f2.write(" ")
