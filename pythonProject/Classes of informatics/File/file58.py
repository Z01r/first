with open("file58t", "r") as file:
    k = file.read()
    p = k.index(" ")
    l = k[:p]
with open("file58t", "w+") as file1:
    file1.write(l)
