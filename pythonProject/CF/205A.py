n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
res = ""
if n == 1:
   res = "1"
elif b[0] != b[1] or n == 1:
    res = str(a.index(b[0]) + 1)
else:
    res = "Still Rozdil"
print(res)
