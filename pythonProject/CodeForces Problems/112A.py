c=0
t=0
for x in range(int(input())) : 
    a,b=map(int,input().split())
    t+=b-a 
    c=max(c,t)    
print(c)
