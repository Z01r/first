s = input()
n = len(s)
h = 0
for i in range(n):
    h += int(s[i]) * (2 ** (n - 1 - i))
print(h)