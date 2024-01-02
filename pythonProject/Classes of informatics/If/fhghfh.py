s = int(input())
p = int(input())
t = 0
for i in range(1, s):
    k = int(input())
    if p > k:
        t += 1
if t > 0:
    print('False')
elif t == 0:
    print('True')
