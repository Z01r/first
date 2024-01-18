n=input().split()
a=int(n[0])
b=int(n[1])
s=0
while a<=b:
    a=a*3
    b=b*2
    s+=1
print(s)
