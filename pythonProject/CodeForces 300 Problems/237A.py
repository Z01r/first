n = int(input())
m = 1
c = 1
t = "0"
for i in range(n):
    p = input()
    if t == p:
        c += 1
        m = max(m, c)
    else:
        t = p
        c = 1
print(m)
