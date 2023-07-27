n = int(input())
s = ''
while n > 1:
    s += str(n % 2)
    n = n // 2
s += '1'
s = s[::-1]
print(s)
