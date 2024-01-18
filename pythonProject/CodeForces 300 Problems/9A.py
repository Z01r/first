n = input().split()
mx = max(int(n[0]), int(n[1]))
m = 6 - mx + 1
flag = 0
if m == 6 and flag == 0:
    print('1/1')
    flag += 1
if m % 2 == 0 and flag == 0:
    print(str(m // 2) + '/' + '3')
    flag += 1
if m % 3 == 0 and flag == 0:
    print(str(m // 3) + '/' + '2')
    flag += 1
if m % 6 == 0 and flag == 0:
    print(str(m // 6) + '/' + '1')
    flag += 1
if flag == 0:
    print(str(m) + '/' + '6')
