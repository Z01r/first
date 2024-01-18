n = int(input())
t = 0
while n >= 0:
    t += 1
    n -= t * (t + 1) / 2
print(t - 1)
