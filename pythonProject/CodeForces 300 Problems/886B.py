n = input()
a = input().split()
b = {}
for i in range(len(a)):
    b[a[i]] = i
print(a[min(b.values())])
