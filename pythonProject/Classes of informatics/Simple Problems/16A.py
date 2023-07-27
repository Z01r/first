n=int(input())
a=[]
for i in range(n):
    f=int(input())
    a.append(f)
for j in range(n//2):
    print(a[j])
    print(a[n-1-j])
