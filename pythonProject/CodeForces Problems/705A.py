n=int(input())
m=''
for i in range(1,n+1):
    if i%2!=0 and i!=n:
        m+='I hate it that '
    if i%2==0 and i!=n:
        m+='I love it that '
    if i%2==0 and i==n:
        m+='I love it'
    if i%2!=0 and i==n:
        m+='I hate it'
print(m)
