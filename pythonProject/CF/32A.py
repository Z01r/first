a, d = map(int, input().split())
b = list(map(int, input().split()))
kol = 0
for i in range(a):
    for j in range(a):
        if abs(b[i] - b[j]) <= d and i != j:
            kol += 1
print(kol)
