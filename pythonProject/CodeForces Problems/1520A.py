n=int(input())
for i in range(n):
    t=int(input())
    s=input()
    for d in range(1,len(s)):
        if s[d] in s[:d] and s[d-1]!=s[d]:
            print('NO')
            break
    else:
        print('YES')
