n=int(input())
kol=0
a=[]
for i in range(1,n+1):
    s=input().split()
    h=int(s[0])
    m=int(s[1])
    if h!=23:
        kol=(60-m)+((24-h-1)*60)
        a.append(kol)
    if h==23:
        kol=60-m
        a.append(kol)
for j in range(len(a)):
    print(a[j])
        
    
