n = int(input())
s = input()
a = s.count('1')
b = s.count('2')
c = s.count('3')
d = s.count('4')
print(d + c + (b * 2 + max(0, a - c) + 3) // 4)
