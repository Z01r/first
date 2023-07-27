n=int(input())
summ=0
for i in range(1,n+1):
    h=input()
    if h=='Tetradron':
        summ+=4
    if h=='Cube':
        summ+=6
    if h=='Octahedron':
        summ+=8
    if h=='Dodecahedron':
        summ+=12
    if h=='Icosahedron':
        summ+=20
    print(summ)
