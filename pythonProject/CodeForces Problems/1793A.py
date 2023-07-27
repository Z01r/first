t=int(input()) 
for i in range(t):
    a,b = map(int,input().split(" "))
    x,y = map(int,input().split(" "))
    q=x//(y + 1)
    r=x-q*(y + 1)
    print(q*min(a*y,b*(y+1))+r*min(a,b))
