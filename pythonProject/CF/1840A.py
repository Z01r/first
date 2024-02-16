t = int(input())
c = []
for q in range(t):
    p = int(input())
    s = input()
    temp = s[0]
    b = ''
    for i in range(1, len(s)-1):
        print(s[i])
        if s[i] == temp:
            b += s[i]
            temp = s[i+1]
            i += 1
        print("-------------------")
    c.append(b)
for o in c:
    print(o)
