l=[0]*7
n=int(input())
for i in range(n):
    x=input()
    for j in range(7):
        l[j]+=int(x[j])
print(max(l))
