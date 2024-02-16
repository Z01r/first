t=int(input())
for u in range(t):
    s=input()
    if s[0]=='0':
        print(0)
    elif s[0]=='?':
        print(9*pow(10,s.count('?')-1))
    else:
        print(pow(10,s.count('?')))
