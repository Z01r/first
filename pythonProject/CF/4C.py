a = {}
t = int(input())
for _ in range(t):
    s = input()
    if s not in a:
        a[s] = 1
        print('OK')
    else:
        print(s + str(a[s]))
        a[s] += 1
