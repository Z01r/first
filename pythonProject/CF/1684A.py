t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    v=str(n)
    if len(v)>2:
        for j in v:
            a.append(int(j))
        print(min(a))
    else:
        print(n%10)
