s = input() + "n"
a = "aeioun"
b = "aeiou"
for i in range(len(s) - 1):
    if s[i] not in a and s[i + 1] not in b:
        print("NO")
        exit()
print("YES")
