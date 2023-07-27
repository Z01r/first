s = input()
a = "abcdefghijklmnopqrstuvwxyz"
b = "1234567890"
flag = 0
s = s.lower()
for i in s:
    if (i not in a) and (i not in b):
        flag += 1
if flag > 0:
    print("FALSE")
else:
    myfile = open(s,"w+")
    print("TRUE")
