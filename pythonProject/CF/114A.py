l = int(input())
n = int(input())
res = "YES"
resk = 0
while n != l:
    if n % l != 0:
        print("NO")
        exit()
    n //= l
    resk += 1
print(res)
if res == "YES":
    print(resk)
