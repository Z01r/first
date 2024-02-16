s = input()
kolm = 0
kolb = 0
for i in s:
    if i.islower():
        kolm += 1
    else:
        kolb += 1
if kolm > kolb:
    print(s.lower())
else:
    print(s.upper())
