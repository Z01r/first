b = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = []
    res = 1
    for j in s:
        a.append(ord(j))
    mx = max(a)
    res += b.index(chr(mx))
    print(res)
