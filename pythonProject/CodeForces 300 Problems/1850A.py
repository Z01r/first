n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if (a + b + c) - min(a, b, c) >= 10:
        print('yes')
    else:
        print('no')
