a1, a2, a3, a4 = map(int, input().split())
s = input()
summ = 0
l = list()
for q in s:
    l.append(q)
for i in l:
    if i == '1':
        summ += a1
    elif i == '2':
        summ += a2
    elif i == '3':
        summ += a3
    elif i == '4':
        summ += a4
print(summ)