n=int(input())
a=[]
for i in range(n):
    a.append(input())
k=0
for i in range(n):
    if a[i].count('1')>1:
        k+=1
print(k)
