n = int(input())
w = list(map(int, input().split()))
s = 0
d = 0
for i in range(len(w)):
    if i % 2 == 0:
        s += max(w[0], w[len(w)-1])
    else:
        d += max(w[0], w[len(w)-1])
    w.remove(max(w[0], w[len(w)-1]))
print(s, d)
