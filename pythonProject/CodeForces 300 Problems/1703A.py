n = int(input())
o = 'YES'
for i in range(1, n + 1):
    h = input()
    h = h.upper()
    if h != o:
        print('NO')
    else:
        print('YES')
