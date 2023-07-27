n = int(input())
p = str(n)[0]
ps = n % 10
k = str(n)
k=k[:len(k)-1]
k = k[::-1]
k += str(p)
print(int(k))
k = k[::-1]
k=k[:len(k)-1]
k+=str(ps)
print(int(k))