n=int(input())
a=[]
for i in range(n):
    f=int(input())
    a.append(f)
for j in range(n//4):
    print(a[j])
    print(a[j+1])
    print(a[n-1-j])
    print(a[n-2-j])
