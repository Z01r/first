l = input()
r = 0
m = 0
i = 0
a = map(int, input().split())
for x in a:
    i += 1
    m = max(m, x)
    r += m == i
print(r)