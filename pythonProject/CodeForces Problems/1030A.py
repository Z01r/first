n=int(input())
flag=0
h=input().split()
for j in h:
    if int(j)==1:
        flag=1
if flag==1:
    print('HARD')
elif flag==0:
    print('EASY')
