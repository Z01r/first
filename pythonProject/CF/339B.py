n, m = map(int, input().split())
s = 0
p = 1
l = list(map(int,input().split()))
for v in l:
    s += (v - p) % n
    p = v
print(s)
