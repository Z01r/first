a = input().split()
b = list()
for i in range(len(a)):
    b.append(len(a[i]))
x = max(b)
for j in range(len(a)):
    if len(a[j]) == x:
        print(a[j])
        break
