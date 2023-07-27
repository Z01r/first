from math import sqrt
s=0
p=0
for i in range(1,51):
    p=i
    for j in range(52-i):
        p=sqrt(p)
    s+=p
print(s)