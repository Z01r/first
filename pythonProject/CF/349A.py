n = int(input())
a = list(map(int, input().split()))
kassa = []
for i in a:
    if i == 25:
        kassa.append(i)
    elif i == 50 and kassa.count(25) > 0:
        del kassa[kassa.index(25)]
        kassa.append(50)
    elif i == 100 and (kassa.count(25) > 0 and kassa.count(50) > 0) or (kassa.count(25) > 1 and kassa.count(50)==0):
        del kassa[kassa.index(25)]
        del kassa[kassa.index(50)]
        kassa.append(100)
    else:
        print("NO")
        exit()
print("YES")
