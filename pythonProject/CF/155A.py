n = int(input())
h = input().split()
mx = int(h[0])
mn = int(h[0])
kol = 0
for i in h:
    if int(i) > mx:
        mx = int(i)
        kol += 1
    if int(i) < mn:
        mn = int(i)
        kol += 1
print(kol)
