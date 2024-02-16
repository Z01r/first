t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    flag='no'
    x=0
    if (n-k)%2==0 or n%2==0 or n%k==0:
        flag='yes'
    print(flag)
