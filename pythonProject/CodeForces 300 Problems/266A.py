n = int(input())
h = input()
ch = ''
kol = 0
for j in range(len(h)):
    if j != 0 and h[j] == h[j - 1]:
        kol += 1
print(kol)
