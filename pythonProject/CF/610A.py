n = int(input())
if n % 2 != 0:
    print(0)
    exit()
else:
    if n % 4 == 0:
        print((n//4)-1)
    else:
        print(n//4)
