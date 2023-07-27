n=int(input())
a=[]
k=0
for i in range(1,n+1):
    k=int(input())
    if k>=1900:
        a.append('Divishion 1')
    if k>=1600 and k<=1899:
        a.append('Divishion 2')
    if k>=1400 and k<=1599:
        a.append('Divishion 3')
    if k<=1399:
        a.append('Divishion 4')
for c in range(len(a)):
    print(a[c])
