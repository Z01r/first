def fact1(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
s=0
for i in range(1,n+1):
    k=fact1(i)
    s=s+k
print(s)
