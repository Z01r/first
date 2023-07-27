import os
s = input()
m = '1234567890'
b = 0
for filename in os.listdir("."):
    if filename == s:
        with open(filename,"r") as file:
            p = file.read()
            for i in p:
                if i in m:
                    b+=1
if b==0:
    print("-1")
else:
    print(b)