a = input()
k = int(input())
x = 0
g = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December']
g = g * 100
flag = 0
for e in range(len(g)):
    if g[e] == a and flag == 0:
        x = e + k
        flag = 1
print(g[x])
