t = int(input())
for _ in range(t):
    c = input()
    s1 = int(c[0]) + int(c[1]) + int(c[2])
    s2 = int(c[3]) + int(c[4]) + int(c[5])
    if s1 == s2:
        print("YES")
    else:
        print("NO")