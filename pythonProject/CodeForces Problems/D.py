n=int(input())
a=[]
kol=0
for i in range(n):
    g=int(input())
    b=g
    kol=0
    while b!=1:
        while b%6!=0:
            b=b*2
            kol+=1
        while b%6==0:
            b=b//6
            kol+=1
    a.append(kol)
for j in range(len(a)):
    print(a[j])
        
        
        

        
