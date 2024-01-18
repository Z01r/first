s = input()
a = []
l = ["B", "u", "l", "b", "a", "s", "r"]
for i in l:
    a.append(s.count(i))
a[1] = a[1] // 2
a[4] = a[4] // 2
print(min(a))
