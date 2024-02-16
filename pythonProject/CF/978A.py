t = int(input())
s = input().split()
s.reverse()
a = []
for i in s:
    if i not in a:
        a.append(i)
a.reverse()
print(len(a))
print(*a)
