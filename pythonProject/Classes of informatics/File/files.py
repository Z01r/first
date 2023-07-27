f = "pj.txt"
a = list(map(int, input().split()))
with open(f, "w") as file:
    for i in range(len(a)):
        file.write(str(a[i]))
        file.write(" ")
with open(f, "r") as file:
    c = file.read()
    print(c)
