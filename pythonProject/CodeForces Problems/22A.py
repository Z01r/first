n=int(input())
l=list(map(int,input().split()[:n]))
l.sort()
x=min(l)
flag=1
for i in l:
    if i!=x:
        print(i)
        flag=0
        break
if flag==1:
    print("NO")
