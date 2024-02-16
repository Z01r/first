n = int(input())
a = []
for _ in range(n):
    b = []
    s = input().split()
    b.append(int(s[0]))
    b.append(int(s[1]))
    a.append(b)
p = int(input())
for i in range(len(a)):
    if a[i][0] <= p <= a[i][1]:
        print(n - i)
        exit()
