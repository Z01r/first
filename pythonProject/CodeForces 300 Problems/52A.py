n = int(input())
s = input().split()
o = s.count('1')
d = s.count('2')
t = s.count('3')
print(n - max(o, d, t))
