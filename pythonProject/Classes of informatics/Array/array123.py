n=int(input())
a=list()
b=list()
r=list()
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for m in range(n):
    for j in range(n):
        if m==j:
            continue
        for h in range(n):
            if h==j:
                continue
            k=0
            k+=(((a[j]-a[m])**2)+((b[j]-b[m])**2))**(0.5)
            k+=(((a[h]-a[j])**2)+((b[h]-b[j])**2))**(0.5)
            k+=(((a[m]-a[h])**2)+((b[m]-b[h])**2))**(0.5)
            r.append(k)
print(max(r))
            
            
