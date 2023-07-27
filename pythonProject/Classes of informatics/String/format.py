a = list(map(str,input().split()))
b = list(map(int,input().split()))
for i in range(len(a)):
    info = "Name: {0}\t Age: {1}".format(a[i], b[i])
    print(info)
