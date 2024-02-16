n, m = map(int, input().split())
s = 0
for i in range(n):
    t = input().split()
    for h in t:
        if h == 'C' or h == 'M' or h == 'Y':
            s += 1
if s > 0:
    print('#Color')
else:
    print('#Black&White')
