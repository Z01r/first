t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    p = 4*(n-1)
    if k > p:
        print(p//2+(k-p))
    else:
        print((k+1)//2)
