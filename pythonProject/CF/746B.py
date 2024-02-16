n = int(input())
s = input()
p = ''
for i in range(n - 2, -1, -2):
    p += s[i]
if n % 2 == 0:
    i = 1
else:
    i = 0
while i < n:
    p += s[i]
    i += 2
print(p)
