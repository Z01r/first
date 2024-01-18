n = int(input())
s = input()
s = s.lower()
q = 'abcdefghijklmnopqrstuvwxyz'
flag = 0
for i in q:
    if i in s:
        flag += 1
    else:
        flag -= 1
if flag >= len(q):
    print('YES')
if flag < len(q):
    print('NO')
