a, b, s = map(int, input().split())
a = abs(a)
b = abs(b)
if (s - (a + b)) % 2 == 0 and s >= (a + b):
    print("Yes")
else:
    print("No")
