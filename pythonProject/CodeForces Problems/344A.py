p=0
f=0
for i in range(int(input())):
    s=input()
    if p!=s:
        f+=1
    p=s
print(f)
