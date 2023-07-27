n = int(input())
p = 1
ch = 1
while p <= n:
    ch += 1
    p *= ch
print(str(ch - 1) + '!')
