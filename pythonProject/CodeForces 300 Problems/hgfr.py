t = int(input())
w = []
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    o = abs((max(s)*(n-1)) - sum(s))
    w.append(o)
for q in w:
    print(q)