n = int(input())
p = int(input())
s = 0
for i in range(1,n):
    u = int(input())
    l = u % 2
    g = p % 2
    if l == g and s == 0:
        s = u
    p = u
print(s)