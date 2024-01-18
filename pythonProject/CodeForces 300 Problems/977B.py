n = int(input())
s = input()
a = []
b = []
q = s[0]
for i in range(1,len(s)):
    a.append(str(q)+s[i])
    q = s[i]
for j in a:
    b.append(a.count(j))
print(a[b.index(max(b))])