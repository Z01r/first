n=int(input())
h=input()
ch=''
kol=0
for i in h:
    if i=='R':
        ch+='2'
    if i=='B':
        ch+='1'
    if i=='G':
        ch+='3'
for j in range(len(ch)):
    if j!=0 and int(ch[j])==int(ch[j-1]):
        kol+=1
print(kol)
