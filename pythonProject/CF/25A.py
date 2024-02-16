n = int(input())
a = list(map(int, input().split()))
b = []
c = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        c.append(i+1)
    else:
        b.append(i+1)
if len(c) > len(b):
    print(b[0])
else:
    print(c[0])