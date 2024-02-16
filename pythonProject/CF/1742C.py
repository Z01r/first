t = int(input())
for _ in range(t):
    a = input()
    b = [input() for i in range(8)]
    if "R" * 8 in b:
        print("R")
    else:
        print("B")
