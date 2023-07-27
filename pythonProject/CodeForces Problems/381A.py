n=int(input())
s=list(map(int,input().split()))
se=0
di=0
for i in range(len(s)):
    if i%2==0:
        se+=max(s[0],s[len(s)-1])
    else:
        di+=max(s[0],s[len(s)-1])
    s.remove(max(s[0],s[len(s)-1]))
print(se,di)
