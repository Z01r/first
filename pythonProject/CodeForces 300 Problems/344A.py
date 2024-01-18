p = -1
f = -1
for i in range(int(input())):
    s = input()
    if p != s:
        f += 1
        p = s
print(f)
