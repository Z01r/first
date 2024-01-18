n = int(input())
flag = 0
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        flag += 1
if flag > 0:
    print("Happy Alex")
else:
    print("Poor Alex")