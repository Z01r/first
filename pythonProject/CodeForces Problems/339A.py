n=input()
l=''
b=[]
z=''
for i in range(len(n)):
    if i%2==0:
        l+=str(n[i])
for j in l:
    b.append(int(j))
b.sort()
for t in range(len(b)):
    if t==(len(b)-1):
        z+=str(b[t])
    if t!=(len(b)-1):
        z+=str(b[t])+'+'
print(z)
