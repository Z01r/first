n = int(input())
l = str(n)
o = l.count('0')
g = l.count('9')
if o > g:
    print('0')
elif 0 < g:
    print('9')
