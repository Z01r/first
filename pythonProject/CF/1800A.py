n = int(input())
a = []
for i in range(n):
    l = int(input())
    s = str(input())
    s = s.lower()
    flag = 0
    if s[0] != 'm':
        flag = -8
    for q in s:
        if flag == 0 and q == 'm':
            flag = 0
        if flag == 0 and q == 'e':
            flag = 1
        if flag == 1 and q == 'o':
            flag = 2
        if flag == 2 and q == 'w':
            flag = 3
        elif flag == 0 and q != 'm' and q != 'e':
            flag = -8
        elif flag == 1 and q != 'e' and q != 'o':
            flag = -8
        elif flag == 2 and q != 'o' and q != 'w':
            flag = -8
        elif flag == 3 and q != 'w':
            flag = -8
    a.append(flag)
for u in range(len(a)):
    if a[u] == 3:
        print('YES')
    else:
        print('NO')
