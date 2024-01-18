n = int(input())
s = input().split()
a = []
for i in range(n):
    a.append(int(s[i]))
b = a.index(max(a)) + a[::-1].index(min(a))
print(b - (b >= n))
