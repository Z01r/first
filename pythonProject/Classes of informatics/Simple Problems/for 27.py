import math

x=float(input())
n=int(input())
s=x
p=1
q=1
for i in range(2,(2*n)+2,2):
    p=p*(i-1)
    q=q*i
    s = s + p * (x**(i+1))/(q*(i+1))
print(s)
print(math.asin(x))
