n = int(input())
s = 0
a = list(map(int, input().split()))
a.sort()
for i in range(0, n // 2):
    s += a[(i * 2)] - a[(i * 2) - 1]
print(abs(s))
