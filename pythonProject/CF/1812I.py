u='bdfhklt'
d='gjpqy'
I=input
for m in range(int(I())):
    s=I()
    k,y=0,True
    for c in s:
        if c in u:
            k+=1
        elif c in d:
            k-=1
        if k<0:
            y=False
            break
    print('YES'if y and k==0 else 'NO')
