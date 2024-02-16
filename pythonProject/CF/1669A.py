n = int(input())
a = []
k = 0
for i in range(1, n + 1):
    k = int(input())
    if k >= 1900:
        a.append('Division 1')
    if 1600 <= k <= 1899:
        a.append('Division 2')
    if 1400 <= k <= 1599:
        a.append('Division 3')
    if k <= 1399:
        a.append('Division 4')
for c in range(len(a)):
    print(a[c])
