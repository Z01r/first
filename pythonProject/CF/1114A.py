x,y,z=map(int,input().split())
a,b,c=map(int,input().split())
if (a<x or a-x+b<y or a-x+b-y+c<z):
    print('NO')
else:
    print('YES')
