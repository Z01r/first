import math as m

s = input()
n = eval('0b' + s)
s = 0
if n == 0 or n == 1:
    print(0)
    exit()
p = int(m.log(n, 4))
for i in range(p+1):
    s += (4**i)
    if s > n+1:
        print(i)
        exit()
print(i+1)