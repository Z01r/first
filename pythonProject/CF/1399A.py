t=int(input())
for i in range(t):
    m=int(input())
    a=set(map(int,input().split()))
    if max(a)-min(a)<len(a):	
            print('YES')
    else:
            print('NO')
