n=input().split()
s=int(n[1])
n=int(n[0])
result=s//n
if s%n==0:
  print(result)
else:
  print(result+1)
