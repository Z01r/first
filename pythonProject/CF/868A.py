s = input()
n = int(input())
z = []
k = ''
for _ in range(n):
    h = input()
    z.append(h)
    k += h
flag = 0
flag2 = 0
if s in z:
    print("YES")
    exit()
elif (s[0] not in k) or (s[1] not in k):
    print("NO")
    exit()
else:
    for i in z:
        if i[0] == s[1]:
            flag += 1
        if i[1] == s[0]:
            flag2 += 1
    if flag >= 1 and flag2 >= 1:
        print("YES")
        exit()
    else:
        print("NO")
        exit()