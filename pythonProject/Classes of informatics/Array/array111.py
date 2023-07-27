n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))
for j in range(n):
    if a[j]%2==1:
        a[j]*=3
print(a)
