n = int(input())
k = int(input())
s = input()
file = open(s, "w+")
for i in range(n):
    file.write('*' * k)
    file.__enter__('k')
