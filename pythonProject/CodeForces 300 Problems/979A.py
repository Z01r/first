n = int(input())
n += 1
if n % 2 == 0:
    col = n // 2
elif n == 1:
    col = 0
else:
    col = n
print(col)
