n,m = map(int,input().split())
p = 0
for i in range(n):
    a = list(input())
    b = list(set(a))
    if len(b) > 1 or p == b[0]:
        print("NO")
        exit()
    p = b[0]
print("YES")