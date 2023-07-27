n = int(input())
s = 0
k = ''
for i in range(1, n + 1):
    k += str(i)
    s += int(k)
    k = str(k)
print(s)



