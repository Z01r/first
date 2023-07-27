a,b = map(int,input().split());c="a"
for i in range(a):
    z = set(input())
    if len(z)>1 or c==z :
        print("NO")
        exit()
    c=z
print("YES")    
