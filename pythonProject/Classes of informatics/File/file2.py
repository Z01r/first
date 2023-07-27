s = input()
n = int(input())
y = open(s, "w+")
for i in range(1,n+1):
    y.write(str(i*2))
    y.write(" ")