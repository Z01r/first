n = int(input())
for i in range(n):
    a, b = sorted(map(int, input().split()))
    print(max(2 * a, b) ** 2)
