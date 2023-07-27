def daler(n):
    sch=1
    flag=0
    while sch<=n:
        sch+=1
        if n%sch==0:
            flag+=1
    if flag<=2:
        return 'TRUE'
    else:
        return 'FALSE'
n=int(input())
print(daler(n))
