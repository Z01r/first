n=input().split()
h=int(n[0])
k=int(n[1])
for i in range(k):
    if h%10!=0:
        h=h-1
    elif h%10==0:
        h=h//10
    print(h)
