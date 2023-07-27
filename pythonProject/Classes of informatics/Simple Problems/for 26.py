x=float(input())
n=int(input())
s=0
p=1
for i in range(1,n+2,2):
    s+=((x**i)/i)*p
    p*=(-1)
    print(s)
    
