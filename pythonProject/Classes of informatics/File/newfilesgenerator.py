s = input()
myfile = open(s,"w+")
a = list(map(str,input().split()))
for i in a:
    myfile.write(str(i))
    myfile.write(" ")