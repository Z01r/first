t=int(input())
for i in range(t):
    n=int(input())
    b=len(str(n))
    k=(b-1)*9
    m=n//int('1'*b)
    print(k+m)
    
