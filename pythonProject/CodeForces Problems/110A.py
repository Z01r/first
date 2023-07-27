n=int(input())
g=str(n)
flag=0
j=len(g)
l=str(j)
summ=0
for i in l:
    summ+=int(i)
if summ%4!=0 and summ%7!=0:
    print('NO')
if summ%4==0 or summ%7==0:
    print('YES')
    
        
