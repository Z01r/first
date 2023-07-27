n=input()
o=''
kolz=0
kols=0
u=n.upper()
for i in range(len(n)):
    if n[i]!=u[i]:
        kols+=1
    if n[i]==u[i]:
        kolz+=1
if kolz>kols:
    n=n.upper()
else:
    n=n.lower()
print(n)
