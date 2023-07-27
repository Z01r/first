n,m=map(int,input().split())
flag=0
for i in range(n):
    s=input().split()
    for h in s:
        if h=='C' or h=='M' or h=='Y':
            flag+=1
if flag>0:
    print('#Color')
else:
    print('#Black&White')
