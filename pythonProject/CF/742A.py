n = int(input())
w = ["8","4","2","6"]
if 4 >= n > 0:
    print(w[n-1])
elif n == 0:
    print("1")
elif n % 4 == 1:
    print("8")
elif n % 4 == 2 or (n == 3):
    print("4")
elif n % 4 == 3:
    print("2")
elif n % 4 == 0:
    print("6")