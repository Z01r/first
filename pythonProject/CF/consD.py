n, x0, y0 = map(int, input().split())
a = [abs(x0-y0)]
for _ in range(n):
    x,y = map(int,input().split())
    if abs(x-y) not in a:
        a.append(abs(x-y))
print(len(a))