t=int(input())
for i in range(t):
    w,h,n=map(int,input().split())
    if w*h&-w*h<n:
        print('NO')
    else:
        print('YES')
