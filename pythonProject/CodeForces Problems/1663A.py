t=int(input())
for i in range(t):
    n=int(input())
    print(n-n%7+7*(n%7>n%10))
