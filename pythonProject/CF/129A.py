n = int(input())
a = list(map(int,input().split()))
s = sum(a)
kol = 0
for y in range(len(a)):
    if (s - a[y]) % 2 == 0:
        kol += 1
print(kol)
