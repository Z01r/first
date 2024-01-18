n=int(input())
a=list(map(int,input().split()))
p=a.count(1)
q=a.count(2)
r=a.count(3)
z=(min(p,q,r))
print(z)
for i in range(z):
  print(a.index(1)+1,a.index(2)+1,a.index(3)+1)
  a[a.index(1)]=5
  a[a.index(2)]=5
  a[a.index(3)]=5
