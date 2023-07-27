filey = open("filea", "w+")
filex = open("fileb", "w+")
p = list()
with open("fi11", "r") as file:
    k = file.read()
    p = k.split()
a = list()
b = list()
for o in range(len(p)):
    if o % 2 == 1:
        a.append(p[o])
    elif o % 2 == 0:
        b.append(p[o])
for k in a:
    filex.write(k)
    filex.write(" ")
for v in b:
    filey.write(v)
    filey.write(" ")