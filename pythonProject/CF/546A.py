h=input().split()
k=int(h[0])
n=int(h[1])
w=int(h[2])
summ=0
for i in range(1,w+1):
    summ+=i*k
if summ>n:
    print(summ-n)
else:
    print('0')
