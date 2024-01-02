n = int(input())
a = []
a1 = int(input())
a2 = int(input())
for i in range(2, n):
    a3 = int(input())
    if a1 > a2 < a3:
        a.append(a2)
    a1 = a2
    a2 = a3
print(max(a))
