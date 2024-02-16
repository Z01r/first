n = int(input())
a = []
for i in range(0, n + 1):
    s = " " * ((n - i) * 2)
    for j in range(0, i):
        s += str(j) + " "
    print(s + str(i) + s[((n-i)*2):][::-1])
    a.append(s + str(i) + s[((n-i)*2):][::-1])
a.reverse()
for q in a[1:]:
    print(q)
