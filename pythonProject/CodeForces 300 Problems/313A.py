s = input()
print(max(int(s), int(s[:len(s) - 1]), int(s[:len(s) - 2] + s[len(s) - 1])))
