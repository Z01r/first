t=int(input())
for j in range(t):
    n = int(input())
    s = input()
    ss = sorted(s)
    cnt = 0
    for i in range(len(s)):
        if(s[i]!=ss[i]):
            cnt+=1
    print(cnt)
