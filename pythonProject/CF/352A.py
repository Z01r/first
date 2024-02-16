a = int(input())
b = input()
c = b.count('5')
d = a - c
if d > 0:
    print(int('5' * (9 * (c // 9)) + '0' * d))
else:
    print('-1')
