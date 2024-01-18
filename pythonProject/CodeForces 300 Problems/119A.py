from math import gcd
*a,n=map(int,input().split())
p=1
while n:
    p^=1
    n-=gcd(a[p],n)
print('01'[p])
