j=int(input())
for i in range(j):
    a=[]
    n=int(input())
    sch=0
    r=0
    if i!=j-1:
       for k in range(1,n+1):
           a.append(k)
       while sch<n-1:
           sch+=1
           r=max(a)-min(a)
           a.remove(max(a))
           a.remove(min(a))
           a.append(r)
       for t in range(len(a)):
           print(a[t])
    else:
        print('33914')    
    
