t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if set(s[0::2]) & set(s[1::2]):
        print('NO')
    else:
        print('YES')
