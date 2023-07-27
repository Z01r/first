n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
for i in range(n):
    f = True
    if sum(l[:i]) > sum(l[i:]):
        print(i)
        f = False
        break
if f:
    print(n)
