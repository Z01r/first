n = input()
l = sorted(map(int, input().split()))
s = 0
res = 0
while s <= sum(l):
    s += l.pop()
    res += 1
print(res)
