numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
d = []
for q in numbers:
    r = []
    e = 1
    while e <= q:
        if q % e == 0:
            r.append(e)
        e += 1
    d.append(r)
result = {numbers[i]: d[i] for i in range(len(numbers))}
print(result)
