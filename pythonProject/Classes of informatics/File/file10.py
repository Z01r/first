file2 = open("file2", "w+")
p = list()
with open("fi10", "r") as file:
    k = file.read()
    p = k.split()
p.reverse()
for b in p:
    file2.write(b)
    file2.write(" ")
