for t in range(int(input())):
    a = list(map(int, input().split()))
    if sum(a) % 3 == 0 and max(a[0:3]) <= sum(a) / 3:
        print("YES")
    else:
        print("NO")
