s = input()
flag = 0
for i in s:
    if i == 'H' or i == 'Q' or i == '9' and flag == 0:
        flag = 1
if flag == 0:
    print('NO')
else:
    print('YES')
