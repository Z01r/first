n = int(input())
a = list(map(int, input().split()))
c = []
r = 1
for k in a:
    c += [r] * int(k)
    r += 1
m = input()
b = list(map(int, input().split()))
for j in b:
    print(c[int(j) - 1])
