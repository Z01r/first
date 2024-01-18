n,k = map(int,input().split())
a = list(map(int,input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
flag = 'no'
res = 0
while flag == 'no':
    if k % max(b) == 0:
        flag = 'yes'
        res = k//max(b)
    else:
        del b[b.index(max(b))]
print(res)