n=int(input())
k=int(input());k=k-1
l=int(input());l-=1
a=list()
for i in range(n):
    f=int(input())
    if i>l or i<k:
        a.append(f)
print(a)
