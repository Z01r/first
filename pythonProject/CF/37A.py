n = int(input())
a = list(map(int, input().split()))
b = []
mx = 0
for i in a:
    mx = max(mx, a.count(i))
    if i not in b:
        b.append(i)
print(mx, len(b))
