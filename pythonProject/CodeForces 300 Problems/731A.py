s=input()
f=0
pre='a'
for i in s:
    a=abs(ord(i)-ord(pre))
    f+=min(a,26-a)
    pre=i
print(f)
