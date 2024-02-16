s = input()
a = []
res = ""
for _ in range(10):
    a.append(input())
for i in range(0, 71, 10):
    if s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5] + s[i + 6] + s[i + 7] + s[i + 8] + s[i + 9] in a:
        res += str(a.index(
            s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5] + s[i + 6] + s[i + 7] + s[i + 8] + s[i + 9]))
print(res)
