a = list(input().split())
print(*a)
n = int(input())
for i in range(n):
    km, nm = input().split()
    a.remove(a[a.index(km)])
    a.append(nm)
    print(*a)
