n = input()
h = input()
ch = ''
for i in range(len(n)):
    if int(n[i]) != int(h[i]):
        ch += '1'
    else:
        ch += '0'
print(ch)
