s = input()
b = input()
file1 = open(s, "w+")
a = list(map(float, input().split()))
for i in a:
    file1.write(str(i))
    file1.write(" ")
file1.close()
file2 = open(b, "w+")
o1 = ''
o2 = ''
with open(s, "r") as file:
    k = file.read()
    d = k.split()
    o1 = d[0]
    o2 = d[len(d)-1]
with open(b, "w") as filer:
    filer.write(o1)
    filer.write(" ")
    filer.write(o2)