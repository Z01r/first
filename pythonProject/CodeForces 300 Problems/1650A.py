n=int(input())
for i in range(n):
    s=input()
    r=input()
    if r in s[::2]:
        print('YES')
    else:
        print('NO')
