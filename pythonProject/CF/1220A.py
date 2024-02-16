k = int(input())
s = sorted(input())
z = s.count('z')
e = s.count('e')
o = s.count('o')
r = s.count('r')
n = s.count('n')
w = 'true'
p = ''
while w == 'true':
    if o > 0 and n > 0 and e > 0:
        p += '1 '
        o -= 1
        n -= 1
        e -= 1
    else:
        w = 'false'
w = 'true'
while w == 'true':
    if o > 0 and r > 0 and e > 0 and z > 0:
        p += '0 '
        o -= 1
        r -= 1
        e -= 1
        z -= 1
    else:
        w = 'false'
print(p)
