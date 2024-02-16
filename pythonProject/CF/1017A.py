t=int(input())
a=[]
for i in range(t):
    b=list(map(int,input().split()))
    a.append(sum(b))
g=a[0]
a.sort()
a.reverse()
h=a.index(g)
print(h+1)
