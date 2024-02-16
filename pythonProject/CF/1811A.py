t=int(input())
for i in range(t):
    n,d=map(int,input().split())
    s=input()
    i=0
    while i<len(s) and d<=int(s[i]):
        i+=1
    print(s[:i]+str(d)+s[i:])
