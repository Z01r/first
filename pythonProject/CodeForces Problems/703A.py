n=int(input())
sm=0
sc=0
for i in range(1,n+1):
    g=input().split()
    if int(g[0])>int(g[1]):
        sm+=1
    if int(g[0])<int(g[1]):
        sc+=1
if sm==sc:
    print('Friendship is magic!^^')
if sm>sc:
    print('Mishka')
if sm<sc:
    print('Chris')
