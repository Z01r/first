import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]
    for i in range(n):
        b.append(b[-1] + a[i] % 2)
    for j in range(q):
        l, r, k = map(int, input().split())
        ans = b[-1] + b[l - 1] - b[r] + k * (r - l + 1)
        print("Yes" if ans % 2 else "No")
