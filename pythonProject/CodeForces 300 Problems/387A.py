h1, t1 = map(int, input().split(':'))
h2, t2 = map(int, input().split(':'))
res = (h1 * 60 + t1 + 24 * 60 - (h2 * 60 + t2)) % (24 * 60)
if res // 60 < 10 and res % 60 < 10:
    res = "0" + str(res // 60) + ":" + "0" + str(res % 60)
elif res // 60 < 10 <= res % 60:
    res = "0" + str(res // 60) + ":" + str(res % 60)
elif res // 60 >= 10 > res % 60:
    res = str(res // 60) + ":" + "0" + str(res % 60)
else:
    res = str(res // 60) + ":" + str(res % 60)
print(res)
