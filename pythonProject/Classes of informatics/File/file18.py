with open("file18nf", "r") as file:
    k = file.read()
    p = k.split()

a = int(p[0])
b = int(p[1])
for j in range(2, len(p)):
    if a > b and b < int(p[j]):
        print(b)
        print(j-1)
        break
    else:
        a = b
        b = int(p[j])
