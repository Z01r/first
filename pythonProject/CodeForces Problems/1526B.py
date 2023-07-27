t=int(input())
a=[]
while t:
    n=int(input())
    flag='false'
    for i in range(1000):
        if (n-i)*11>=0:
            if ((n-i)*11)%111==0:
                flag='true'
    t-=1
if flag=='true':
    a.append('YES')
if flag=='flase':
    a.append('NO')
for t in range(len(a)):
    print(a[t])
