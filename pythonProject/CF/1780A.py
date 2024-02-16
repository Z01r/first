n=int(input())
s=0
flag=0
a=[]
z=[]
sd=''
for i in range(n):
    h=input().split()
    s=0
    flag=0
    sd=''
    for j in range(len(h)):
        for b in range(j+1,len(h)):
            for g in range(b+1,len(h)):
                s=s+int(h[j])+int(h[b])+int(h[g])
                if s%2==1 and flag==0:
                    flag=1
                    sd=sd+str(j+1)+' '+str(b+1)+' '+str(g+1)
                    z.append(sd)
    if flag==1:
        a.append('YES')
    else:
        a.append('NO')
for q in range(len(a)):
    if a[q]=='YES':
        print('YES')
        print(z[q])
    else:
        print('NO')
        
                
                    
