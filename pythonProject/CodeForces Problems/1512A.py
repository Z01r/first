t=int(input())
a=[]
l=0
ind=0
for i in range(1,t+1):
    g=int(input())
    h=input().split()
    for z in range(len(h)):
        l=h.count(h[z])
        if l==1:
            ind=z+1
    print(ind)
        
