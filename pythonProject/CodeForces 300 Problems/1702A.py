from math import log10
t = int(input())
for i in range(t):
    n = int(input())
    print(n-10**(int(log10(n))))
