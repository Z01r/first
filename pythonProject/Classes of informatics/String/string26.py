n = int(input())
s = input()
if len(s) > n:
    s = s[::-1]
    while len(s) > n:
        s -= s[len(s)-1]
    s = s[::-1]
elif len(s) < n:
    s = s[::-1]
    while len(s) < n:
        s += '.'
    s = s[::-1]
print(s)