file1 = open("file67t1", "w+")
file2 = open("file67t2", "w+")
with open("file67t", "r") as file:
    k = file.read()
    p = k.split()
a = list()
b = list()
for i in p:
    h = int(i[:2])
    a.append(h)
    d = int(i[3:5])
    b.append(d)
for x in a:
    file1.write(str(x))
    file1.write(" ")
for c in b:
    file2.write(str(c))
    file2.write(" ")