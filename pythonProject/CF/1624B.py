t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    a2 = b - (c - b)
    b2 = a + (c - a) / 2
    c2 = a + 2 * (b - a)
    if (a2 >= a) and (a2 % a == 0) and (a2 != 0):
        print("YES")
        continue
    elif (b2 >= b) and (b2 % b == 0) and (b2 != 0):
        print("YES")
        continue
    elif (c2 >= c) and (c2 % c == 0) and (c2 != 0):
        print("YES")
        continue
    else:
        print("NO")
