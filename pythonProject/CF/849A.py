n = int(input())
a = input().split()
if int(a[0]) % 2 == 0 or int(a[n - 1]) % 2 == 0 or n % 2 == 0:
    print("No")
    exit()
print("Yes")
