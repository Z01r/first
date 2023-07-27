n = int(input())
s = 0
if n % 2 == 0:
    for i in range(2, n + 1, 2):
        s += i
else:
    for j in range(1, n + 2, 2):
        s += i
print(s)
