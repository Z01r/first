from math import ceil
s = input()
i = 0
n = len(s)
c = 0
while i < n:
    j = i
    while j < n and s[i] == s[j]:
        j += 1
    k = j-i
    c += int(ceil(k/5))
    i = j
print(c)