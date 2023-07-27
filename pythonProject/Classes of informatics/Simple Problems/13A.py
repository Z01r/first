n=int(input())
a=[]
for i in range(n):
    f=int(input())
    a.append(f)
a.reverse()
for j in range(1,n,2):
    print(a[j])
    
