n = int(input())
m = ''
for i in range(1, n):
    if i % 2 == 0:
        m += 'I love that '
    else:
        m += 'I hate that '
if n % 2 == 0:
    m += 'I love it'
else:
    m += 'I hate it'
print(m)
