l=int(input())
n=input()
flag1=0
s1=0
s2=0
for i in n:
    if int(i)!=4 and int(i)!=7:
        flag1+=1
for j in range((len(n)//2)):
    s1+=int(n[j])
for y in range((len(n)//2),len(n)):
    s2+=int(n[y])
if flag1==0 and s1==s2:
    print('YES')
else:
    print('NO')
print(s1,s2)
