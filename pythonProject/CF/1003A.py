n = int(input())
m = list(map(int, input().split()))
k = list()
for i in m:
    k.append(m.count(i))
print(max(k))
