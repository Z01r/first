a = int(input())
b = int(input())
c = int(input())
res = a + b + c
res = max(res, a * (b + c), a * b * c, (a + b) * c)
print(res)
