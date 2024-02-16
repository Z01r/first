a = input()
r = 0
c = '47'
for i in a:
    if i in c:
        r += 1
if r == 4 or r == 7:
    print("YES")
else:
    print("NO")
