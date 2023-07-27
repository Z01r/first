a=int(input())
n=int(input())
s=0
p=1
for i in range(1,n+1):
    s+=((a**i)*p)
print(s)
